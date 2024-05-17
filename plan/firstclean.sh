# Script to clean up temporary files created from previous simulation
echo "Cleaning all temporary files created from previous simulations"
rm -rf vcd/*
rm -rf modules/*
rm -rf pkl/*
rm txtfile
rm dumpfile
rm sigArray.pkl
rm timing.txt
rm leakage.csv
rm leakagepredict1000.txt
