#!/usr/bin/python3
""" Lockboxes interview task """


def canUnlockAll(boxes):
    """ Write a method that determines if all the boxes can be opened. """
    keyMatch = 0
    allBoxes = len(boxes)

    for box in range(len(boxes)):
        if keyMatch == box:
            keyMatch += 1
        if boxes[box] == [] and boxes[-1] != []:
            break
    if keyMatch == allBoxes:
        return True
    else:
        return False
