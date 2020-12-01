# This py file holds all of the sorting algorithms

def bubble_sort(arr, arr_size):
    for i in range(arr_size - 1):
        for j in range(arr_size - i - 1):
            if(arr[j] > arr[j+1]):
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                # Maintains the array so that it can be displayed on the plot
                yield arr


# # Helper function for Selection_Sort function
# def partition(arr, low, high):
#     # Put element value to the right 
#     pivot = arr[high]

#     # Index of the smaller element 
#     i = (low - 1)

#     for j in range(low, high):
#         # if current element is smaller than pivot then swap 
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
            
#     arr[i+1], arr[high] = arr[high], arr[i+1] 
#     print(i+1)
#     return (i + 1) 

# def quick_sort(arr, low, high):
#     if len(arr) == 1:
#         return arr
    
#     if low < high:
#         # Get the actual pibot
#         pi = partition(arr, low, high)
#         yield pi

#         yield from quick_sort(arr, low, pi - 1)
#         yield from quick_sort(arr, pi + 1, high)


def swap(A, i, j):
    a = A[j]
    A[j] = A[i]
    A[i] = a

def quick_sort(arr,p,q):
    if(p>=q):
        return
    piv = arr[q]
    pivindx = p
    for i in range(p,q):
        if(arr[i]<piv):
            swap(arr,i,pivindx)
            pivindx+=1
        yield arr
    swap(arr,q,pivindx)
    yield arr

    yield from quick_sort(arr,p,pivindx-1)
    yield from quick_sort(arr,pivindx+1,q)

def merge_sort(arr,lb,ub):
    if(ub<=lb):
        return
    elif(lb<ub):
        mid =(lb+ub)//2
        yield from merge_sort(arr,lb,mid)
        yield from merge_sort(arr,mid+1,ub)
        yield from merge(arr,lb,mid,ub)
        yield arr

def merge(arr,lb,mid,ub):
    new = []
    i = lb
    j = mid+1
    while(i<=mid and j<=ub):
        if(arr[i]<arr[j]):
            new.append(arr[i])
            i+=1
        else:
            new.append(arr[j])
            j+=1
    if(i>mid):
        while(j<=ub):
            new.append(arr[j])
            j+=1
    else:
        while(i<=mid):
            new.append(arr[i])
            i+=1
    for i,val in enumerate(new):
        arr[lb+i] = val
        yield arr