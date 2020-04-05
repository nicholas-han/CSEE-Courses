from cs50 import get_string
from sys import argv


def main():
    # take command line arguments
    while len(argv) != 2:
        exit("Usage: python bleep.py dictionary")

    fileName = argv[1]

    # take user input string
    text = get_string("What message would you like to censor?\n")

    # load dictionary
    badWords = set()
    file = open(fileName, "r")
    for line in file:
        badWords.add(line.rstrip("\n"))
    file.close()

    # check and print
    for word in text.split():
        if word.lower() in badWords:
            for i in range(len(word)):
                print("*", end="")
        else:
            print(word, end="")
        print(" ", end="")
    print()


if __name__ == "__main__":
    main()
