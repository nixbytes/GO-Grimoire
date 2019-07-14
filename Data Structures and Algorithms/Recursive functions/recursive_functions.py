'''
“The following code should demonstrate the difference between recursion and iteration.
Both these functions simply print out numbers between low and high,
the first one using iteration and the second using recursion:”
Excerpt From: Benjamin Baka. “Python Data Structures and Algorithms.” iBooks.

'''


def interTest(low, high):
    while low <= high:
        print(low)
        low = low + 1


def recurTest(low, high):
    if low <= high:
        print(low)
        recurTest(low + 1, high)


if __name__ == '__main__':
    interTest(1, 5)
    recurTest(1, 5)
