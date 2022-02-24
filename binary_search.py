#Implementing Binary Search - Iterative Method
def binarySearch(A, x, H):
    L = 0
    while(L<=H):
        mid = (L+H)//2
        if x>A[mid]:
            L = mid + 1
        elif x<A[mid]:
            H = mid - 1
        else:
            return mid
        
    return -1
    
    


def main():
    A = []
    A = [1, 2, 5, 7, 9, 61, 101, 115, 120, 199, 294, 1050, 2000]
    print(f'Array : {A}')
    x = int(input("Enter element to be searched : "))
    index = binarySearch(A, x, len(A)-1)
    if index!=-1:
        print(f'Element found at index {index}')
    else:
        print("Element not found")



if __name__ == '__main__':
    main()