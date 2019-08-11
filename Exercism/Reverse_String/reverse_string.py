#!/usr/bin/env pytohn3


def reverse(text):
    try:
        if len(text) == 0:
            return text
        else:
            return reverse(text[1:]) + text[0]
    except ValueError as e:
        return "Missing String Value".format(e)


# print(reverse())
print(reverse("cat"))
