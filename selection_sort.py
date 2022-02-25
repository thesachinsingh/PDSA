#Selection sort
import random
def selectionSort(A):
    for i in range(len(A)):
        min, index = A[i], i
        for j in range (i+1, len(A)):
            if A[j]<min:
                min, index = A[j], j
        A[index], A[i] = A[i], min
    return A


def main():
    X = []
    for i in range(20):
        X.append(random.randint(0, 2000))
    print(f'Initial Array : {X}')
    X = selectionSort(X)
    print(f'Final Array : {X}')

if __name__ == '__main__':
    main()