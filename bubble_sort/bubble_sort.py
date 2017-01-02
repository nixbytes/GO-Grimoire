#!/bin/python
    
def bubble_sort(numbers):
    """
    Inefficiently sort the mutable numbersuence (list) in place.
       numbers MUST BE A MUTABLE numbersUENCE.
 
       As with list.sort() and random.shuffle this does NOT return 
    
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
   sample_list = [12,5,123,987,07,21,34]
   print(sample_list)
   print(bubble_sort(sample_list))