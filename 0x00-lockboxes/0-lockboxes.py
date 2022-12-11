#!/usr/bin/python3
""" Lockboxes interview task """


def canUnlockAll(boxes):
    """ Write a method that determines if all the boxes can be opened. """
    keyMatch = 0
    matched = False

    for box in range(len(boxes)):
        if keyMatch == box:
            keyMatch += 1
            matched = True
        if boxes[box] == [] and boxes[-1] != []:
            matched = False
            break
    if matched is False:
        return False
    else:
        return True
