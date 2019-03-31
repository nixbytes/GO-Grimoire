#!/usr/bin/env pytohn3

def reverse(text):
        if text is None:
            return 'Missing String Value {}'
        elif len(text) == 0:
            return text
        else:
            return reverse(text[1:]) + text[0]

# print(reverse())
print(reverse())
