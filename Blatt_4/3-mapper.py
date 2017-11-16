import sys

def main():
    for line in sys.stdin:
        splitted = line.split(",")
        apps = ",".join(splitted[:4])
        counts = ",".join(splitted[4:])
        return_string = apps + "/" + counts
        print(return_string)

if __name__ == "__main__":
    main()