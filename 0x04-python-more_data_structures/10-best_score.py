#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    else:
        sorting = sorted(a_dictionary.items(), key= lambda x : x[1])
        return sorting[-1][0]
