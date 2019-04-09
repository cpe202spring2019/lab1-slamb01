
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
	    return None
    max_val = 0
    for i in range(len(int_list)):
        if int_list[i] > max_val:
            max_val = int_list[i]
        
    return max_val
def reverse_rec(int_list, spot = 0):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError
    middle = len(int_list)//2
    pos = len(int_list) - 1 - spot
    if spot != middle:
        a = int_list[spot]
        b = int_list[pos]
        int_list[spot] = b
        int_list[pos] = a
    else: 
        return int_list
    return reverse_rec(int_list, spot +1)
def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list == None:
        raise ValueError
    middle = (low + high)//2
    if middle == low and low !=0:
        middle +=1
    if middle > len(int_list) - 1 or middle < 0:
        return None
    if int_list[middle]==target:
        return middle
    if int_list[middle] > target:
        high = middle
        if high == low:
            return None
        return bin_search(target, low, high, int_list)
    if int_list[middle] < target:
        low = middle
        return bin_search(target, low, high, int_list)