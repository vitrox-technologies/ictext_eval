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
<pre>
.
├── <a href="data">data</a> <b>(Folder to store model related data here)<b>
│   └── <a href="data/.gitkeep">.gitkeep</a>
├── <a href="evaluation">evaluation</a> <b>(Contains Evaluation code)<b>
│   ├── <a href="evaluation/Dockerfile">evaluation/Dockerfile</a>
│   ├── <a href="evaluation/coco.py">evaluation/coco.py</a>
│   ├── <a href="evaluation/cocoeval.py">evaluation/cocoeval.py</a>
│   ├── <a href="evaluation/gt.json">evaluation/gt.json</a>
│   ├── <a href="evaluation/ictext_eval.py">evaluation/ictext_eval.py</a>
│   ├── <a href="evaluation/main.py">evaluation/main.py</a>
│   └── <a href="evaluation/requirements.txt">evaluation/requirements.txt</a>
├── <a href="output">output</a> <b>(Output of the model should be saved here as result.json)<b>
│   ├── <a href="output/.gitkeep">output/.gitkeep</a>
│   └── <a href="output/result.json">output/result.json</a>
├── <a href="tensorflow">tensorflow</a> <b>(Sample folder to store code)<b>
│   ├── <a href="tensorflow/Dockerfile">tensorflow/Dockerfile</a>
│   └── <a href="tensorflow/main.py">tensorflow/main.py</a>
├── <a href="timer">timer</a> <b>(Contains code to get FPS and used GPU memory size for task 3 evaluation)<b>
│   ├── <a href="timer/Dockerfile">timer/Dockerfile</a>
│   └── <a href="timer/main.py">timer/main.py</a>
├── <a href="torch">torch</a> <b>(Sample folder to store code)<b>
│   ├── <a href="torch/Dockerfile">torch/Dockerfile</a>
│   └── <a href="torch/main.py">torch/main.py</a>
├── <a href="utilization">utilization</a> <b>(Contains log file to keep track of GPU usage every seconds)<b>
│   └── <a href="utilization/log.csv">utilization/log.csv</a>
├── <a href="README.md">README.md</a>
├── <a href="run_task1_2.sh">run_task1_2.sh</a>
└── <a href="run_task3.sh">run_task3.sh</a>
</pre>

# Main changes
You can find the main evaluation code at evaluation/ictext_eval.py. The evaluation algorithm is taken from pycocotools with a few changes:
1. Polygon coordinates [x1,1,...,x4,y4] will be used to replace bbox [x,y,w,h] for evalution.
2. Reject submission with empty aesthetic labels, length of aesthetic labels != 3 and not one hot encoded. Please find the relevant code under the function 'loadRes' in coco.py.
3. Multi-label score will be calculated based on the matching criteria of IoU>0.5, all area regions and matched based on ground truth to prediction. Please find the relevant code under the function 'evaluateImg' in cocoeval.py.
4. Ground truth with aesthetic labels of [0,0,0] will be skipped and a default value of [0,0,0] will be given if there is no detection for the ground truth. Please find the relevant code under the function 'evaluateImg' in cocoeval.py.
5. We will use F-2 score instead of F-1 score as we want to prioritize recall more than precision. Please find the relevant code under the function 'accumulate' in cocoeval.py.
6. We set the default FPS to 30 and default GPU memory to 4000MB. For the calculation of 3S score, refer to the following formula:
3S = 0.2 x normalised speed + 0.2 x (1-normalised size) + 0.6 x normalised score
