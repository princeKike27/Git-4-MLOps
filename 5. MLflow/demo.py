# import modules
import os
import mlflow
import argparse
import time 




# MAIN function
def main(input1, input2):
    # set experiment
    mlflow.set_experiment('Demo_Experiment_27')

    # start run
    # with mlflow.start_run(run_name='Example Demo27'):
    with mlflow.start_run():
        # set tag
        mlflow.set_tag('version', '1.0.0')

        # log inputs as parameters
        mlflow.log_param('param1', input1)
        mlflow.log_param('param2', input2)
        
        # metric to log
        metric = eval(param1=input1, param2=input2)
        # log metric
        mlflow.log_metric('Eval_Metric', metric)

        # make dir
        os.makedirs('ex_27', exist_ok=True)

        # create file and open it n write mode
        with open('ex_27/example_27.txt', 'wt') as f:
            f.write(f'Artifact created at: {time.asctime()}') 

        # log everything inside dir ex_27
        mlflow.log_artifacts('ex_27')




# EVAL function
def eval(param1, param2):
    # output metric
    output_metric = param1**2 + param2**2
    return output_metric



# receive inputs from command line
if __name__ == '__main__':
    # create parser
    args = argparse.ArgumentParser()
    # read input from user
    args.add_argument('--param1', "-p1", type=int, default=5)
    args.add_argument('--param2', "-p2", type=int, default=10)
    # parsed arguments
    parsed_args = args.parse_args() # access param 1 >> parsed_args.param1
    # pass inputs from command line to main function
    main(parsed_args.param1, parsed_args.param2)