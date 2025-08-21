#!/usr/bin/python3
"""Lockboxes interview task"""
  

def canUnlockAll(boxes):
    """Determines if all boxes can be opened"""
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    opened = set([0])
    keys = boxes[0].copy()

    while keys:
        key = keys.pop()
        if key < n and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == n 
