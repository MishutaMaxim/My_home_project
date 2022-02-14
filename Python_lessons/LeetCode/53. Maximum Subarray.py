def maxSubArray(nums) -> int:
    l = len(nums)
    if l == 1:
        return nums[0]
    maxSub = nums[0]
    for i in range(1, l):
        nums[i] = max(nums[i], nums[i] + nums[i-1])
        maxSub = max(nums[i], maxSub)

    return maxSub


a = [1,2]
b = [-2,1,-3,4,-1,2,1,-5,4]
c = [-1,-2]
d = [-2,-1]
e = [31,-41,59,26,-53,58,97,-93,-23,84]

assert maxSubArray(a) == 3
assert maxSubArray(b) == 6
assert maxSubArray(c) == -1
assert maxSubArray(d) == -1
assert maxSubArray(e) == 187
