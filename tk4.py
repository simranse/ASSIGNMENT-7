# A = Array 
# s = start index
# e = end index
# p = pivot index
# g = greater than pivot boundary index

def swap(A,i1,i2):
  A[i1], A[i2] = A[i2], A[i1]

def partition(A,g,p):
    # O(n) - just one for loop that visits each element once
    for j in range(g,p):
      if A[j] <= A[p]:
        swap(A,j,g)
        g += 1
      
    swap(A,p,g)
    return g
    
def _quicksort(A,s,e):
    # Base case - we are sorting an array of size 1
    if s >= e:
      return
    
    # Partition current array
    p = partition(A,s,e)
    _quicksort(A,s,p-1) # Left side of pivot
    _quicksort(A,p+1,e) # Right side of pivot

# Wrapper function for the recursive one
def quicksort(A):
    _quicksort(A,0,len(A)-1)

A = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,-1]

print(A)
quicksort(A)
print(A)
