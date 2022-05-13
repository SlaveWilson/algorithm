from typing import List

def binary_search(nums: List[int], low: int, high: int, target: int) -> int:
    mid = int((high + low) / 2)
    
    if nums[mid] == target:
        return mid
    if low >= high:
        return None
    
    if target < nums[mid]:
        return binary_search(nums, low, mid - 1,target)
    else:
        return binary_search(nums, mid + 1, high, target)

def main():
    nums = [2,3,5,7,9]
    target = 5
    output = binary_search(nums, 0, len(nums) - 1, target)
    print(output)

if __name__ == "__main__":
    main()