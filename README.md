ICText Local Test Kit
---

# Introduction
This repo contains the evalaution code for [Task 1 and 2](https://eval.ai/web/challenges/challenge-page/756) and [Task 3](https://eval.ai/web/challenges/challenge-page/757) in ICText challenge.

# Running
Setup and run this repo for Task 1 and 2 by:
```sh
$ bash run_task1_2.sh
```

Make sure docker is setup to use GPU through [nvidia docker](https://github.com/NVIDIA/nvidia-docker) and run this for Task 3:
```sh
$ bash run_task3.sh
```

The flow of evaluation for Task 3 is as follows:
1. Start Timer
2. Start Algorithm in TensorFlow or PyTorch
3. Start Evaluation when Algorithm finishes 

They will be running in parallel through command chaining.

# Folder Structure
.
├── [data/](data)                                        # Folder to store model related data here
│   └── [.gitkeep](data/.gitkeep)
├── [evaluation/](evaluation)                            # Contains Evaluation code
│   ├── [Dockerfile](evaluation/Dockerfile)
│   ├── [coco.py](evaluation/coco.py)
│   ├── [cocoeval.py](evaluation/cocoeval.py)
│   ├── [gt.json](evaluation/gt.json)
│   ├── [ictext_eval.py](evaluation/ictext_eval.py)
│   ├── [main.py](evaluation/main.py)
│   └── [requirements.txt](evaluation/requirements.txt)
├── [output/](output)                                    # Output of the model should be saved here as result.json
│   ├── [.gitkeep](output/.gitkeep)
│   └── [result.json](output/result.json)
├── [tensorflow/](tensorflow)                            # Sample folder to store code
│   ├── [Dockerfile](tensorflow/Dockerfile)
│   └── [main.py](tensorflow/main.py)
├── [timer/](timer)                                      # Contains code to get FPS and used GPU memory size for task 3 evaluation
│   ├── [Dockerfile](timer/Dockerfile)
│   └── [main.py](timer/main.py)
├── [torch/](torch)                                      # Sample folder to store code
│   ├── [Dockerfile](torch/Dockerfile)
│   └── [main.py](torch/main.py)
├── [utilization/](utilization)                          # Contains log file to keep track of GPU usage every seconds
│   └── [log.csv](utilization/log.csv)
├── [readme.md](readme.md)
├── [run_task1_2.sh](run_task1_2.sh)
└── [run_task3.sh](run_task3.sh)

# Main changes
You can find the main evaluation code at evaluation/ictext_eval.py. The evaluation algorithm is taken from pycocotools with a few changes:
1. Polygon coordinates [x1,1,...,x4,y4] will be used to replace bbox [x,y,w,h] for evalution.
2. Reject submission with empty aesthetic labels, length of aesthetic labels != 3 and not one hot encoded. Please find the relevant code under the function 'loadRes' in coco.py.
3. Multi-label score will be calculated based on the matching criteria of IoU>0.5, all area regions and matched based on ground truth to prediction. Please find the relevant code under the function 'evaluateImg' in cocoeval.py.
4. Ground truth with aesthetic labels of [0,0,0] will be skipped and a default value of [0,0,0] will be given if there is no detection for the ground truth. Please find the relevant code under the function 'evaluateImg' in cocoeval.py.
5. We will use F-2 score instead of F-1 score as we want to prioritize recall more than precision. Please find the relevant code under the function 'accumulate' in cocoeval.py.
6. We set the default FPS to 30 and default GPU memory to 4000MB. For the calculation of 3S score, refer to the following formula:
3S = 0.2 x normalised speed + 0.2 x (1-normalised size) + 0.6 x normalised score
