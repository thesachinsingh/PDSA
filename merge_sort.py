#merge sort 
import random
def merge(A, B):
    (m,n) = (len(A), len(B))
    (C,i,j,k) = ([],0,0,0)
    while(k < m+n):
        if i == m:
            C.extend(B[j:])
            k = k + (n-j)
        elif j == n:
            C.extend(A[i:])
            k = k + (m-i)
        elif A[i] < B[j]:
            C.append(A[i])
            (i,k) = (i+1,k+1)
        else:
            C.append(B[j])
            (j,k) = (j+1,k+1)

    return (C) 

def mergeSort(A):
    n = len(A)
    if n<=1:
        return(A)
    L = mergeSort(A[:n//2])
    R = mergeSort(A[n//2:])
    B = merge(L, R)
    return (B)

def main():
    arr = [random.randint(0,95) for i in range(10)]
    print(f'arr before : {arr}')
    print(mergeSort(arr))
    

if __name__ == '__main__':
    main()