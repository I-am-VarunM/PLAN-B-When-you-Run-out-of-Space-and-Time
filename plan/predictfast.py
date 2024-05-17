import operator
import concurrent.futures
import csv
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import pmdarima as pm
from statsmodels.tsa.stattools import adfuller
import operator
import time
import multiprocessing
signals = set()  # Use a set to store unique signal names
leaks_file_path = 'leakagepredict1000.txt'
# Open the leakage.csv file
start_time = time.time()
with open('leakage.csv', mode='r') as file:
    # Flag to indicate whether we are in the relevant section
    in_section = False
    
    # Read each line in the file
    for line in file:
        # Strip leading/trailing whitespaces and split the line by comma
        parts = line.strip().split(',')
        
        # Check if we are in the relevant section
        if "Signal" in parts[0] and "Leakage" in parts[1]:
            in_section = True
            continue  # Skip this line
        
        # If we are in the relevant section and the line is not empty
        if in_section and line.strip():
            # Extract the signal name from the first part and add it to the set
            signals.add(parts[0])
        else:
            # Break out of the loop if we have reached the end of the relevant section
            break

# Convert the set to a list and print the extracted signal names
unique_signals = list(signals)
# Assuming signals is the list containing the signal values
signals = [...]  # Your list of signals

# Iterate over the list starting from the second element
for i in range(1, len(signals)):
    # Calculate the average of the values from the previous indices
    avg = sum(signals[:i]) / (i+1)
    # Update the current value with the calculated average
    signals[i] = avg

# Print the updated signals list
print("Updated signals list:", signals)

print("Extracted unique signal names:", unique_signals)
my_dict = {}
def process_signal(signal):
    leakage_scores = []
    
    if signal != '':
        with open('leakage.csv', mode='r') as file:
            reader = csv.reader(file)
            count = 0
            for row in reader:
                if row[0] == signal:
                    leakage_scores.append(float(row[1]))
                    count += 1
                    if count == 10:
                        break

        print("Extracted leakage scores for signal", signal, ":", leakage_scores)
        leakage_series = pd.Series(leakage_scores)

        try:
            model = pm.auto_arima(leakage_series, seasonal=False, trace=False, n_jobs=-1, information_criterion='aic')
            best_p, best_d, best_q = model.order
            arima_model = pm.ARIMA(order=(best_p, best_d, best_q))
            arima_model.fit(leakage_series)
            forecast = arima_model.predict(n_periods=158)
            if forecast[-1] < 0:
                relu = 0
            elif forecast[-1] > 1:
                relu = 1
            else:
                relu = forecast[-1]
            print("Predicted leakage scores for signal", signal, ":", relu)
        except UserWarning:
            avg_leakage_score = sum(leakage_scores) / len(leakage_scores)
            print("Warning: ARIMA model fitting failed for signal", signal, ". Taking average of leakage_scores:", avg_leakage_score)
            relu = avg_leakage_score
        print("Predicted leakage score for the 200th iteration of signal", signal, ":", relu)
        return (signal, relu)
       
# Define your unique_signals list
unique_signals = [...]

# Dictionary to store signal-wise predictions
my_dict = {}

# Execute the loop concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(process_signal, signal) for signal in unique_signals]
    for future in concurrent.futures.as_completed(futures):
        signal, prediction = future.result()
        my_dict[signal] = prediction

# Sort the dictionary by predicted values
sorted_sigwise = dict(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True))
end_time = time.time()
print(end_time - start_time)
with open(leaks_file_path, "w") as f:
        f.write("Signal,Leakage\n")
        for x in sorted_sigwise:
            f.write("%s,%.4f\n" %(x, sorted_sigwise[x]))
        f.write("\n")