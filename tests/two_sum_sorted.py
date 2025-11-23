def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return left, right
        if s < target:
            left += 1
        else:
            right -= 1
    return None

if __name__ == "__main__":
    nums = [2, 7, 11, 15, 16]
    target = 9
    print(two_sum_sorted(nums, target))