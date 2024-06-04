#!/usr/bin/python3

"""
    Lockboxes Problem open all boxes
"""


def canUnlockAll(boxes):
    """
        Check on the boxes can be unlocked
        return true if they all opend
        return False if they can't be all opend
    """
    if not isinstance(boxes, list):
        return False
    elif (len(boxes)) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
