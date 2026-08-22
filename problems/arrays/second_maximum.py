# Write second_largest(nums) returning the second-largest distinct value, or None if there isn't one. No sorting allowed — single pass.


def find_second_maximum(nums: list) -> int:
    maximum = 0
    second_maximum = 0
    for num in nums:
        if num > maximum: 
            second_maximum = maximum
            maximum = num
        if num > second_maximum and num < maximum:
            second_maximum = num
    
    return second_maximum