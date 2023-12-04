#!/usr/bin/phyton3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        a = len(sentence)
        b = sentence[0]
        return (a, b)
