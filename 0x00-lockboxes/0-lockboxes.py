#!/usr/bin/python3
""" Lockboxes interview task """


def canUnlockAll(boxes):
    """ Write a method that determines if all the boxes can be opened. """
    keyMatch = 0
    allBoxes = len(boxes)

    for box in range(len(boxes)):
        if keyMatch == box:
            print(f"{keyMatch} before unlocking")
            keyMatch += 1
            print(f"{keyMatch} after unlocking")
        if boxes[box] == [] and boxes[-1] != []:
            print(f"{keyMatch} box couldnt be unlock")
            break
    print(f"{keyMatch} vs {allBoxes}")
    if keyMatch == allBoxes:
        return True
    else:
        return False
