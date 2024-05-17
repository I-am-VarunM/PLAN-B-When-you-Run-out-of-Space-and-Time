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
for i in unique_signals:
    leakage_scores = []
# Open the CSV file and read the data
    if i != '':

        with open('leakage.csv', mode='r') as file:
            reader = csv.reader(file)
            
            # Counter to track the occurrences of 'c17.N16'
            count = 0
            
            # Loop through each row in the CSV file
            for row in reader:
                # Check if the row exactly matches 'c17.N16'
                if row[0] == i:
                    # Extract the leakage score and append it to the list
                    leakage_scores.append(float(row[1]))
                    
                    # Increment the count
                    count += 1
                    
                    # Check if we have found the first 25 occurrences
                    if count == 10:
                        break

        # Print the extracted leakage scores
        print("Extracted leakage scores:", leakage_scores)
        leakage_series = pd.Series(leakage_scores)


        # Assume you have already extracted the leakage scores from the CSV file and stored them in the leakage_scores variable
        # leakage_scores = [score1, score2, ..., score25]

        # Fit auto_arima model to find optimal (p, d, q) values
        

        try:
    # Fit ARIMA model with the best parameters
            model = pm.auto_arima(leakage_series, seasonal=False, trace=False, n_jobs = -1, information_criterion = 'aic')

# Assume leakage_scores is your list of leakage scores

# Fit auto_arima model to find optimal (p, d, q) values

# Extract best model parameters
            best_p, best_d, best_q = model.order
            arima_model = pm.ARIMA(order=(best_p, best_d, best_q))
            arima_model.fit(leakage_scores)

    # Predict the next 200 iterations
            forecast = arima_model.predict(n_periods=158)
            if forecast[-1] < 0:
                relu = 0
            else:
                relu = forecast[-1]
            if forecast[-1] > 1:
                relu = 1
    # Print the forecast
            print("Predicted leakage scores for the next 200 iterations:", relu)
        except UserWarning:
    # If a warning is encountered, take the average of leakage_scores and print
            avg_leakage_score = sum(leakage_scores) / len(leakage_scores)
            print("Warning: ARIMA model fitting failed. Taking average of leakage_scores:", avg_leakage_score)
            relu = avg_leakage_score    
        print("Predicted leakage score for the 200th iteration: G", relu)
        my_dict[f"{i}"] = relu
        sorted_sigwise = dict(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True))
end_time = time.time()
print(end_time - start_time)
with open(leaks_file_path, "w") as f:
        f.write("Signal,Leakage\n")
        for x in sorted_sigwise:
            f.write("%s,%.4f\n" %(x, sorted_sigwise[x]))
        f.write("\n")
