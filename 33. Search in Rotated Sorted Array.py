class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        pivoted = False

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while start < end:
            pivot_left = False
            pivot_right = False

            mid = math.floor((end + start) / 2)

            if nums[mid] == target:
                return mid
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end

            if start == mid or end == mid:
                return -1

            if nums[start] > nums[mid]:
                pivot_left = True
            if nums[mid] > nums[end]:
                pivot_right = True

            if pivot_left and (target > nums[start] or target < nums[mid]):
                end = mid
            elif pivot_right and (target > nums[mid] or target < nums[end]):
                start = mid
            elif target > nums[mid]:
                start = mid
            else:
                end = mid
