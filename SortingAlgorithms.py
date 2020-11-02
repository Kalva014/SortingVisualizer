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

def selection_sort(arr):
