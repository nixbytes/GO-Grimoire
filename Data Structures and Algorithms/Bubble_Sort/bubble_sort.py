#!/bin/python
from random import randint

def bubble_sort(numbers):
    """
	describe from wiki
	https://en.wikipedia.org/wiki/Bubble_sort


	Data structure	Array
	Worst-case performance	{\displaystyle O(n^{2})} O(n^{2})
	Best-case performance	{\displaystyle O(n)} O(n)
	Average performance	{\displaystyle O(n^{2})} O(n^{2})
	Worst-case space complexity
    
    """
    changed = True
    while changed:
        changed = False
        for i in xrange(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                changed = True
    return numbers
 
if __name__ == "__main__":
   """Sample usage and simple test suite"""
   print("==============================")
   n = '10aweaweqd'
   sample_list = [randint(0, 9) for num in range(0, n)]
   print("example list: ",sample_list)
   print("==== result ==================")
   print(bubble_sort(sample_list))
