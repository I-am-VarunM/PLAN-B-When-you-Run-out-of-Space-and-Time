def main(input_file_path, simulation_script, key_value, leaks_file_path, time_file_path):
    start_time = time.time()
    subprocess.run(['./' + simulation_script, input_file_path, 200])
    

if __name__ == '__main__':
    # creating the argument parser
    my_parser = argparse.ArgumentParser(description='Pre-silicon power side-channel analysis using PLAN')

    # adding the arguments
    my_parser.add_argument('InputFilePath',
                           metavar='input_file_path',
                           type=str,
                           help='path to the input Verilog file to be analyzed')
    my_parser.add_argument('KeyValue',
                           metavar='key_value',
                           type=int,
                           help='secret value in input Verilog file')
    my_parser.add_argument('SimulationScript',
                           metavar='simulation_script',
                           type=str,
                           help='path to script used for behavioral simulation')
    my_parser.add_argument('Design',
                           metavar='design',
                           type=str,
                           help='name of the design being analysed')
    my_parser.add_argument('-n',
                           '--num-iterations',
                           type=int,
                           action='store',
                           help='number of iterations in behavioral simulation, default value = 1000')
    my_parser.add_argument('-r',
                           '--results-path',
                           type=str,
                           action='store',
                           help='name of directory within results/ directory to store results, default value = current timestamp')

    # parsing the arguments
    args = my_parser.parse_args()

    input_file_path = args.InputFilePath
    key_value = args.KeyValue
    simulation_script = args.SimulationScript
    design = args.Design

    num_iterations = args.num_iterations
    if not num_iterations:
        num_iterations = 1000

    results_path = args.results_path
    if results_path:
        results_path = 'results/' + results_path + '/' + design + '/'
    else:
        results_path = 'results/' + datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + '/' + design + '/'

    if not os.path.isdir(results_path):
        os.makedirs(results_path)

    leaks_file_path = results_path + f"leaks{num_iterations}.txt"
    time_file_path = results_path + f"time{num_iterations}.txt"

    if not os.path.isdir('vcd/'):
        os.makedirs('vcd/')

    if not os.path.isdir('pkl/'):
        os.makedirs('pkl/')

    if not os.path.isdir('modules/'):
        os.makedirs('modules/')

    #print("Note: Please check that:")
    #print("1. the simulation script ({}) given as argument has the correct line numbers, variable names, max range to generate random values".format(simulation_script))
    #print("2. the secret key ({}) given as argument is same as that in the input Verilog file ({}) - please refer to PLAN.md for guidance".format(key_value, input_file_path))
    #print("3. this script (run_plan.py) has the correct functions to load data and compute oracle (in the first few lines) - please refer to PLAN.md for guidance")
    #print()
    #print("If you are sure that the above details are correct, and wish to continue, press Y/y (and enter)")
    #print("To stop, press any other key (and enter)")
    user_input = input()
    if user_input == 'y' or user_input == 'Y':
        main(input_file_path, simulation_script, num_iterations, key_value, leaks_file_path, time_file_path)