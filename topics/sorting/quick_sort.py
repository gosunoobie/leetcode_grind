nums = [7,6,10,5,9,2,1,15,7]

# partition logic
def partition(arr, lb, ub):
    pivot = lb
    while lb <= ub+1:
        if lb > ub: 
            arr[pivot], arr[ub] = arr[ub], arr[pivot]
            break
        if arr[pivot] >= arr[lb]:
            lb+= 1
        elif arr[pivot] < arr[ub]:
            ub -= 1
        else : 
            arr[lb],arr[ub] = arr[ub], arr[lb]
    return ub

#recursive function
def quicksort(arr, lb,ub):
    if (lb < ub):
        pivot_location = partition(arr,lb,ub)
        quicksort(arr, lb, pivot_location-1)
        quicksort(arr, pivot_location+1, ub)
    
quicksort(nums,0,len(nums)-1)
print(nums)

    