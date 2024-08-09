
def x(nums: list[int], k: int) -> int:
    left = answer = 0
    curr = 1
    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1
        answer += right - left + 1