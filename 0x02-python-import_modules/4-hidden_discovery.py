#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    list_name = dir(hidden_4)
    for i in list_name:
        if i[:2] == "__":
            continue
        else:
            print(i)
