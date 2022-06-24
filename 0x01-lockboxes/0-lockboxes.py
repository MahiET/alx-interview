#!/usr/bin/python3
"""A module for checks locked boxes """


def canUnlockAll(boxes):
    """ Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked. """

    if boxes == 0:
        return False

    if not isinstance(boxes, list):
        return False

    if len(boxes) == 0:
        return False

    check = [0]
    list_ing = [i for i in range(len(boxes))]

    for in_check in check:
        for in_boxes in boxes[in_check]:
            if in_boxes not in check and in_boxes in list_ing:
                if in_boxes >= len(boxes):
                    return False
                check.append(in_boxes)

    if len(check) == len(boxes):
        return True
    else:
        return False
