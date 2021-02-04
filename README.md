# ICText Eval

This repo contains the code to evaluate [Task 1 and 2](https://eval.ai/web/challenges/challenge-page/756) in ICText challenge.

Setup this repo by:
```sh
$ pip install -r requirements.txt
```
The main evaluation code is at ictext_eval.py.

The core eval algo is taken from pycocotools with a few changes:
1. Polygon coordinates [x1,1,...,x4,y4] will be used to replace bbox [x,y,w,h] for evalution.
2. Reject submission with empty aesthetic labels, length of aesthetic labels != 3 and not one hot encoded. Please find the relevant code under the function 'loadRes' in coco.py.
3. Multi-label score will be calculated based on the matching criteria of IoU>0.5, all area regions and matched based on ground truth to prediction. Please find the relevant code under the function 'evaluateImg' in cocoeval.py.
4. Ground truth with aesthetic labels of [0,0,0] will be skipped and a default value of [0,0,0] will be given if there is no detection for the ground truth. Please find the relevant code under the function 'evaluateImg' in cocoeval.py.
5. We will use F-2 score instead of F-1 score as we want to prioritize recall more than precision. Please find the relevant code under the function 'accumulate' in cocoeval.py.
