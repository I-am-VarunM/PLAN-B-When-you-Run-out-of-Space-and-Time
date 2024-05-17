#!/bin/bash

# CSV file to store signal and leakage values
csv_file="leakage.csv"
# File to store timing information
timing_file="timing.txt"

# Header for CSV file (uncomment if you want to add headers)
# echo "Signal,Leakage" > $csv_file
circuit_name="fa2"
#./${circuit_name}_simulate.sh ../verilog_files/$circuit_name.v 150 0
# Loop from 10 to 1000 with a step of 10
./firstclean.sh
for i in {5..1000..5}
  do
  # Form the command with the current value of $i
    #if [ "$i" -eq 150 ]; then
     #  ./${circuit_name}_simulate.sh ../verilog_files/$circuit_name.v 150 0
    #else
    # Subtract 5 from i
     # new_i=$((i - 5))
      # ./${circuit_name}_simulate.sh ../verilog_files/$circuit_name.v $i $new_i
    #fi 
  command="python3 run_plan.py ../verilog_files/$circuit_name.v 2 ${circuit_name}_simulate.sh $circuit_name -n $i -r trial"

  # Run the command and automatically answer "Y"
  echo "Y" | $command

  # Extract signal and leakage values from leaks.txt and append to CSV
  while IFS=, read -r signal leakage; do
    # Append to CSV file
    echo "$signal,$leakage" >> $csv_file
  done < results/trial/$circuit_name/leaks${i}.txt

  # Extract time taken and append to timing file
  time_taken=$(grep "Total time taken" results/trial/$circuit_name/time${i}.txt | cut -d ' ' -f 4)
  echo "$time_taken" >> $timing_file

  # Optionally, print a separator between iterations
  echo "===================="
done

# Run prediction script
#cx = "python3 run_plan.py ../verilog_files/$circuit_name.v 170 ${circuit_name}_simulate.sh $circuit_name -n 1000 -r trial"
#echo "Y" | $cx
#python3 predict.py

