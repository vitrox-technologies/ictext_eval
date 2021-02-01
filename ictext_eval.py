import random
import numpy as np
from coco import COCO
from cocoeval import COCOeval

def evaluate(test_annotation_file, user_submission_file, aesthetic):
    print("Starting Evaluation.....")
    if not aesthetic:
        print("Evaluating for Task 1")

        # use pycocotools
        aesthetic = False
        cocoGT = COCO(test_annotation_file)
        cocoDt = cocoGT.loadRes(user_submission_file, aesthetic=aesthetic)
        cocoEval = COCOeval(cocoGT, cocoDt, 'bbox')
        cocoEval.params.multi_label = aesthetic
        cocoEval.evaluate()
        cocoEval.accumulate()
        cocoEval.summarize()
        stats = cocoEval.stats
        output = {
            "AP": stats[0],
            "AP IOU@0.5": stats[1],
            "AP IOU@0.75": stats[2]
        }
        # To display the results in the result file
        print("Completed evaluation for Task 1\n")

    else:
        print("Evaluating for Task 2")

        # use pycocotools
        aesthetic = True
        cocoGT = COCO(test_annotation_file)
        cocoDt = cocoGT.loadRes(user_submission_file, aesthetic=aesthetic)

        cocoEval = COCOeval(cocoGT, cocoDt, 'bbox')
        cocoEval.params.multi_label = aesthetic
        cocoEval.params.beta = 2.0
        cocoEval.evaluate()
        cocoEval.accumulate()
        cocoEval.summarize()
        stats = cocoEval.stats
        output = {
            "AP": stats[0],
            "AP IOU@0.5": stats[1],
            "AP IOU@0.75": stats[2],
            "Multi-Label Precision": stats[12],
            "Multi-Label Recall": stats[13],
            "Multi-Label F-2 Score (IOU@0.5)": stats[14]
        }
        # To display the results in the result file
        print("Completed evaluation for Task 2\n")

    return output

if __name__ == '__main__':
    test_annotation_file = 'gt_json_file'
    user_submission_file = 'prediction_json_file'
    aesthetic = True
    output = evaluate(test_annotation_file, user_submission_file, aesthetic)
