
def binary_search(collection, value, left=0, right=None):
    """
    recursive binary search
    """
    if right is None:
        right = len(collection)-1

    if collection[left:right+1]:
        mid = (left + right)//2
        if collection[mid] == value:
            return mid
        elif collection[mid]>value:
            return binary_search(collection, value, left, mid-1)
        else:
            return binary_search(collection, value, mid+1, right)
    
    return None


assert binary_search([0,1,2,3,4,5,6,7,8,9], 0) == 0
assert binary_search([0,1,2,3,4,5,6,7,8,9], 9) == 9
assert binary_search([0,1,2,3,4,5,6,7,8,9], 1) == 1
assert binary_search([0,1,2,3,4,5,6,7,8,9], 8) == 8
assert binary_search([0,1,2,3,4,5,6,7,8,9], 3) == 3
assert binary_search([0,1,2,3,4,5,6,7,8,9], 7) == 7
assert binary_search([0,1,2,3,4,5,6,7,8,9], 5) == 5