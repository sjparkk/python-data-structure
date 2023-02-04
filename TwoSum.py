"""
https://leetcode.com/problems/two-sum/
정수 숫자와 정수 대상의 배열이 주어졌을 때, 두 숫자의 인덱스가 목표값에 합산되도록 반환한다.
각 입력에 정확히 하나의 솔루션이 있다고 가정할 수 있으며, 동일한 요소를 두 번 사용할 수 없습니다.
답변은 임의의 순서로 반환할 수 있습니다.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(nums, target):
    # O(nlogn)
    nums.sort()
    l, r = 0, len(nums) - 1

    # O(n)
    while l < r:
        if target > nums[l] + nums[r]:
            l += 1
        elif target < nums[l] + nums[r]:
            r -= 1
        else:
            return True

    return False

# nlogn + n -> O(nlogn)

print(twoSum([1, 3, 7, 16, 5, 4, 9], 14))
