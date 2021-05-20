from data_structures import LinkedList
import logging
from functools import reduce

logging.basicConfig()

def bubble_sort(array, n=None):
    """IMplementatoin of bubble sort of
    properties: 
        Adaptive: Yes, (Forced). If sorted, it won't process it beyond n comparisons (forced adaptive, bot by nature).
        Stable: if 2 comapred elements are similar, it won't swap.
        Time Complexity: 
            O(n**2): Worst Case
            O(n): Best Case
        K Passes: useful. explained in use_cases.
    use_cases:
        Best use case: when i smallest or largest number are required from a very large array. we can only run i passes.
    doctest:
    >>> bubble_sort([2,7,5,8,4,6,1,3])
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    # variable to hold number of elements
    if not n:
        n = len(array)
    logger = logging.getLogger('bubble_sort')
    logger.setLevel(logging.DEBUG)
    # variable to hold if array is sorted, in which case no need to do further passes
    is_sorted = True
    # for the purpose of debugging, storing number of passes and comparisons
    n_passes = 0
    n_comparisons = 0
    n_swaps = 0
    # for n elements, we'd need n-1 passes
    for pass_ in range(n-1):
        # becase the USP of the algorithm is that it puts i largest elements to the end after completing ith pass.
        # we can reduce 1 more comparison from below loop.
        n_passes += 1
        for i in range(n-1-pass_):
            n_comparisons += 1
            if array[i] > array[i+1]:
                n_swaps += 1
                is_sorted = False
                array[i], array[i+1] = array[i+1], array[i]
        # break the pass loops if the array is already sorted
        if is_sorted:
            break
    logger.debug('passes:%s, comparisons:%s, swaps:%s', n_passes, n_comparisons, n_swaps)
    return array
        
def insertion_sort(array, n=None):
    """implmementation of insertion sort for
    Definition:
        we can think of this as. in an array of items n.
        pop an element (usually starting from 0+1 position).
        compare it with each element before it (i-1, i-2 ... untill i-n <0)
    properties: 
        Adaptive: Yes, by nature. if sorted, it'll not process it beyond a single comparison .
        Stable: if 2 comapred elements are similar, it won't swap.
        Time Complexity: 
            O(n**2): Worst Case
            O(n): Best Case
        K Passes: not useful. untill completion, it can't be said by certainity that a index element is in sorted position.
    use_cases:
        Best use case: Sorting in Linked List, doesn't need to shift elements.
    doctest:
    >>> insertion_sort([2,7,5,8,4,6,1,3])
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    # variable to hold number of elements
    if not n:
        n = len(array)
    logger = logging.getLogger('insertion_sort')
    logger.setLevel(logging.DEBUG)
    # for the purpose of debugging, storing number of passes and comparisons
    n_passes = 0
    n_comparisons = 0
    n_swaps = 0
    # for insertion sort, we pick second element, and then look for a place to insert it,
    # so the range will start from 1st position, not 0th
    for i in range(1, n):
        n_passes += 1
        # for each pass, keep going in reverse direction. to implement. call i-1 as j.
        # keep swapping numbers at jth and (j-1)th location
        j = i-1
        # we have to pop the element to exhibit the nature of insertion sort, 
        # but we can do it without that as well, by reffering array[i]
        x = array[i]
        # keep moving the jth element to ith location. if array[j] > x (x is the original element at ith for this pass).
        # while array[j] > array[j+1] and j >= 0:
        n_comparisons += 1
        while array[j] > x and j >= 0:
            # array[j],  array[j+1] = array[j+1], array[j]
            array[j+1] = array[j]
            n_swaps += 1
            # decrease index of j by 1 after every comparison
            j -= 1
        # technically, it's not a swap. but still putting an extra condition to void it.
        # my hunch is that if we remove the condition, it'll be faster. as anyway
        # integers would point to same object. but the situation might be different with floats.
        # need to test.
        if i != j + 1:
            n_swaps += 1
            array[0] = x
    logger.debug('passes:%s, comparisons:%s, swaps:%s', n_passes, n_comparisons, n_swaps)
    return array

# def insertion_sort_ll(head: LinkedList, n=None):
#     """implmementation of insertion sort for
#     Definition:
#         we can think of this as. in an array of items n.
#         pop an element (usually starting from 0+1 position).
#         compare it with each element before it (i-1, i-2 ... untill i-n <0)
#     properties: 
#         Adaptive: Yes, by nature. if sorted, it'll not process it beyond a single comparison .
#         Stable: if 2 comapred elements are similar, it won't swap.
#         Time Complexity: 
#             O(n**2): Worst Case
#             O(n): Best Case
#         K Passes: not useful. untill completion, it can't be said by certainity that a index element is in sorted position.
#     use_cases:
#         Best use case: Sorting in Linked List, doesn't need to shift elements.
#     doctest:
#     >>> insertion_sort(reduce(lambda x,i:x.next_node = LinkedList(i), [2,7,5,8,4,6,1,3], LinkedList()))
#     [1, 2, 3, 4, 5, 6, 7, 8]
#     """
#     logger = logging.getLogger('insertion_sort_ll')
#     logger.setLevel(logging.DEBUG)
#     # variable to hold number of elements
#     # for the purpose of debugging, storing number of passes and comparisons
#     n_passes = 0
#     n_comparisons = 0
#     n_swaps = 0
#     # for insertion sort, we pick second element, and then look for a place to insert it,
#     # so the range will start from 1st position, not 0th
#     sorted_ll = None
#     while head:
#         n_passes += 1
#         cur_node = LinkedList(head)
#         if not sorted_ll or cur_node.value <= sorted_ll.value:
#             n_comparisons += 1
#             # if the element is smaller than sorted_ll. make head of sorted_ll as next_node to cur_node
#             cur_node.next_node = sorted_ll
#             sorted_ll = cur_node
#         else:
#             sorted_ll_head = sorted_ll
#             while True:
#                 n_comparisons += 1
#                 if cur_node.value <= sorted_ll.value:
#                     cur_node.next_node = sorted_ll
#                     sorted_ll = cur_node
#                     n_swaps += 1
#                     break
#                 elif not sorted_ll.next_node:
#                     n_comparisons += 1
#                     n_swaps += 1
#                     cur_node.next_node = None
#                     sorted_ll.next_node = cur_node
#                     break
#                 else:
#                     sorted_ll = sorted_ll.next_node
#                     raise ValueError('something is seriously wrong')
#             sorted_ll = sorted_ll_head
#         head = head.next_node

            
#     logger.debug('passes:%s, comparisons:%s, swaps:%s', n_passes, n_comparisons, n_swaps)
#     return sorted_ll_head
            
def selection_sort(array, n=None):
    """implmementation of selection_sort for
    Definition:
        we can think of this as. in an array of items n.
        go to index 1, and then traverse the array to find the smallest number
        we can do this by keep looking for next smallest element, untill we reach end of list.
    properties: 
        Adaptive: No. if sorted, it'll still process it completely .
        Stable: No. if 2 comapred elements are similar, it WILL swap.
        Time Complexity: 
            O(n**2): Worst Case
            O(n): Best Case
        K Passes: useful. if k passes are completed, we'll have k sorted elements.
    use_cases:
        - when i smallest or largest number are required from a very large array. we can only run i passes.
        - when

    doctest:
    >>> selection_sort([2,7,5,8,4,6,1,3])
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    if not n:
        n = len(array)

    logger = logging.getLogger('selection_sort')
    logger.setLevel(logging.DEBUG)
    n_passes = 0
    n_comparisons = 0
    n_swaps = 0

    for i in range(n-1):
        n_passes += 1
        smallest_loc = i
        for j in range(i+1, n):
            n_comparisons += 1
            if array[smallest_loc] > array[j]:
                smallest_loc = j
        n_swaps += 1
        array[i], array[smallest_loc] = array[smallest_loc], array[i]
    logger.debug('passes:%s, comparisons:%s, swaps:%s', n_passes, n_comparisons, n_swaps)
    return array
        

def quick_sort(array, lower=0, n=None):
    """implmementation of quick_sort for
    Definition:
        we can think of this as. in an array of items n.
        go to index 1, and then traverse the array to find the smallest number
        we can do this by keep looking for next smallest element, untill we reach end of list.
    properties: 
        Adaptive: No. if sorted, it'll still process it completely .
        Stable: No. if 2 comapred elements are similar, it WILL swap.
        Time Complexity: 
            O(n**2): Worst Case
            O(n): Best Case
        K Passes: not useful. if k passes are completed, we'll not have k sorted elements..
    use_cases:
        - ??

    doctest:
    >>> quick_sort([2,7,5,8,4,6,1,3])
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    if n is None:
        n = len(array)

    logger = logging.getLogger('quick_sort')
    logger.setLevel(logging.DEBUG)
    n_passes = 0
    n_comparisons = 0
    n_swaps = 0

    def create_partition(lower, n):
        pivotal = lower
        i = lower + 1
        j = n-1
        while True:
            while array[i] <= array[pivotal]:
                    i += 1
            while array[j] > array[pivotal]:
                    j -= 1
            if i > j:
                break
            else:
                array[i], array[j] = array[j], array[i]
        array[j], array[pivotal] = array[pivotal], array[j]
        return j
    if lower < n-1:
        partition_at = create_partition(lower, n)
        quick_sort(array, lower, partition_at+1)
        quick_sort(array, partition_at+1, n)

    return array

def merge_sort(array, n=None):
    pass

def radix_sort(array, n=None):
    pass

if __name__ == '__main__':
    large_ll = LinkedList(2)
    cur_node = large_ll
    for i in  [7,5,8,4,6,1,3]:
        cur_node.next_node = LinkedList(i)
        cur_node = cur_node.next_node

    unsorted_large_array = [2,7,5,8,4,6,1,3]
    sorted_large_array = list(range(2<<20))
    # bubble_sort(unsorted_large_array.copy())
    # bubble_sort(sorted_large_array.copy())
    # insertion_sort(unsorted_large_array.copy())
    # insertion_sort(sorted_large_array.copy())
    # insertion_sort_ll(large_ll)
    # selection_sort(unsorted_large_array.copy())
    # assert sorted_large_array == selection_sort(sorted_large_array.copy())
    print(quick_sort(unsorted_large_array.copy()))
    print(quick_sort(sorted_large_array.copy()))
