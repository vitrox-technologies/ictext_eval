import random
import argparse
from coco import COCO
from cocoeval import COCOeval


def evaluate(test_annotation_file, user_submission_file, aesthetic, fps = None, mem = None):
    print("\n----------Starting Evaluation----------\n")
    cocoGT = COCO(test_annotation_file)
    cocoDt = cocoGT.loadRes(user_submission_file, aesthetic=aesthetic)
    cocoEval = COCOeval(cocoGT, cocoDt, 'bbox')
    cocoEval.params.multi_label = aesthetic
    cocoEval.evaluate()
    cocoEval.accumulate()
    cocoEval.summarize()
    stats = cocoEval.stats
    score = 0

    if not aesthetic:
        output = {
            "AP": stats[0],
            "AP IOU@0.5": stats[1],
            "AP IOU@0.75": stats[2],
        }
        score = stats[0]

    else:
        output = {
            "AP": stats[0],
            "AP IOU@0.5": stats[1],
            "AP IOU@0.75": stats[2],
            "Multi-Label Precision": stats[12],
            "Multi-Label Recall": stats[13],
            "Multi-Label F-2 Score (IOU@0.5)": stats[14],
        }
        score = stats[14]


    if fps != None and mem != None:
        output["3S"] = calculate_final(score, fps, mem)
    print("\n----------Completed Evaluation----------\n")

    return output


def calculate_final(norm_score, fps, mem):
    fps = fps/30
    mem = mem/4000
    norm_spd = min(fps, 1)
    norm_size = min(mem, 1)
    final_score = 0.2 * norm_spd + 0.2 * (1 - norm_size) + 0.6 * norm_score
    print("Speed: {} | Size: {} | Score: {} | 3S: {}".format(
        norm_spd, (1 - norm_size), norm_score, final_score))
    return final_score
