#!/usr/bin/python3
if __name__=="__main__":
    import hidden_4

    for item in sorted(dir(hidden_4)):
        if item[:2] != '__':
            print("{}".format(item))
