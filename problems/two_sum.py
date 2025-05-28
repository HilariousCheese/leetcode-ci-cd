def two_sum( nums, target):
    dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict:
            return [i, dict[complement]]
        dict[nums[i]] = i
    return []
