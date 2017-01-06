def heapsort(num_list):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). 


  '''
 

  for start in range((len(num_list)-2)/2, -1, -1):
    siftdown(num_list, start, len(num_list)-1)
 
  for end in range(len(num_list)-1, 0, -1):
    num_list[end], num_list[0] = num_list[0], num_list[end]
    siftdown(num_list, 0, end - 1)
  return num_list