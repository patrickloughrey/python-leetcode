# Given an array of integers, return the indices of the two numbers such
# that they add up to a specific targe. You may assume that each input would
# have exactly one solution.

class Sum():
    def __init__(self):
        pass

    def two_sum(self, nums, target):
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(nums[i], nums[j])
                    return [i, j]

        return "No two indices add up to the specified target"

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 19
    leet = Sum()
    leet.two_sum(nums, target)
