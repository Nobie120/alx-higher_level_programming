#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def infinite_add(*numbers):
        result = 0
        for i in range(len(sys.argv) - 1):
            result += int(sys.argv[i + 1])
        print(result)
    infinite_add()
