def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    if walk.count("w") == walk.count("e") and walk.count("n") == walk.count("s"):
        return True
    return False


# def isValidWalk(walk):
#     return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')