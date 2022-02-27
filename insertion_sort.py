#insertion sort
import random
def insertionSort(A):
    
    for i in range(1, len(A)): 
        temp = A[i] 
        flag = i-1

        for j in range(i-1, -1, -1):

            if temp<A[j]:           
                A[j+1] = A[j]         
                flag = j            
            
            else:
                break               

        A[flag] = temp  
    
    print(f"Sorted Array {A}")



def main():
    X = [random.randint(-100,100) for i in range(10)]
    print(X)
    insertionSort(X)

if __name__ == '__main__':
    main()