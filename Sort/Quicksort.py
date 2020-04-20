def partition(A, p, q):
    j = p+1
    for i in range(p+1, q):
        if A[i] < A[p]:
            A[i], A[j] = A[j], A[i]
            j += 1

    A[p], A[j-1] = A[j-1], A[p]
    return j-1

def quicksort(A):
    def quicksort_util(A, p, q):
        if p < q:
            m = partition(A, p, q)
            quicksort_util(A, p, m-1)
            quicksort_util(A, m+1, q)
    n = len(A)
    quicksort_util(A, 0, n)


A = [2, 8, 7, 1, 3, 5, 6, 4, 10]
quicksort(A)
print(A)