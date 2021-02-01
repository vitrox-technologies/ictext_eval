# ICText Eval

This repo contains the code to evaluate task 1 and task 2 in ICText challenge.

Setup this repo by:
```sh
$ pip install -r requirements.txt
$ python setup.py install
```
You can run the test case using test.py and the main eval code is at ictext_eval.py.

The core eval algo is taken from pycocotools. The 'ignore' flag and 'iscrowd' bug is fixed based on this [pull request](https://github.com/cocodataset/cocoapi/pull/465).

Do note that there are a few major changes on pycocotools.
1. Reject submission with empty aesthetic labels, length of aesthetic labels != 3 and not one hot encoded. Please find the relevant code under the function 'loadRes' in coco.py.
2. Multi-label score will be calculated based on the matching criteria of IoU>0.5, all area regions and matched based on ground truth to prediction. Please find the relevant code under the function 'evaluateImg' in cocoeval.py.
3. Ground truth with aesthetic labels of [0,0,0] will be skipped and a default value of [0,0,0] will be given if there is no detection for the ground truth. Please find the relevant code under the function 'evaluateImg' in cocoeval.py.
4. We will use F-2 score instead of F-1 score as we want to prioritize recall more than precision. Please find the relevant code under the function 'accumulate' in cocoeval.py.
