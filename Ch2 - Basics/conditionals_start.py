#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x is the same as y"
    else:
        result = "x is greater than y"

    print(result)

    # conditional statements let you use "a if C else b"
    result = "x is less than y" if x < y else "x is greater or equal y"
    print(result)

    # match-case makes it easy to compare multiple values: Need Python 3.10.0
    value = "one"

if __name__ == "__main__":
    main()
