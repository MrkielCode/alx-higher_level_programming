#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if (count == 0):
        print("{}".format(0))
    elif (count == 1):
        print("{}".format(sys.argv[1]))
    else:
        sum = 0
        for i in range(count):
            sum = sum + int(sys.argv[i + 1])
        print("{}".format(sum))
