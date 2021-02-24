import requests
import argparse
import pandas as pd
from ictext_eval import evaluate
import os
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluation method for task 3')

    parser.add_argument('-t',
                        '--task',
                        type= str,
                        choices= ["1","2","3.1","3.2"],
                        help='Pick from Task 1, 2, 3.1 and 3.2')

    parser.add_argument('-g',
                        '--gt',
                        type= str,
                        help='Groundtruth JSON path')

    parser.add_argument('-s',
                        '--sub',
                        type= str,
                        help='Submission JSON path')

    args = parser.parse_args()

    aesthetic = False
    fps = None
    mem = None

    print("\nRunning Evaluation of Task {}".format(args.task))

    if args.task == "2" or args.task == "3.2":
        aesthetic = True

    if args.task == "3.1" or args.task == "3.2":
        response = requests.get("http://timer:5000/time")
        total_time = float(response.content.decode("utf-8"))
        resp = requests.get("http://timer:5000/exit")

        utilization = pd.read_csv("/utilization/log.csv")
        gpu_memory = utilization["mem_util"].max()

        with open(args.gt, "r") as f:
            gt = json.load(f)
            images_count = len(gt["images"])

        print("\nTotal Inference Duration = {} secs\nUsed GPU Memory = {} MB".format(total_time, gpu_memory))
        fps = images_count/total_time
        mem = gpu_memory

    output = evaluate(
        args.gt,
        args.sub,
        aesthetic,
        fps,
        mem
    )

    print(output)
