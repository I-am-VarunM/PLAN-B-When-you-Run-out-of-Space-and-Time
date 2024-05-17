import time
import subprocess
start_time = time.time()
circuit_name = "c432"
#subprocess.run(['./' + f"{circuit_name}_simulate.sh",f"../verilog_files/{circuit_name}.v", str(210)])
subprocess.run('./'+"run_commands.sh")
end_time = time.time()
print("Total Time Taken for prediction is")
print(end_time - start_time)
