
# 13 1

# nums_sum = []
# nums = [965, 582, 23, 8, 695210]
#
# def sum_nums(nums):
#     for i in nums:
#         sum = 0
#         while i != 0:
#             last = i % 10
#             sum = sum + last
#             i = i // 10
#         nums_sum.append(sum)
#     return nums_sum
#
#
# print(sorted(sum_nums(nums)))


# 13 2
# x = float(input('Enter number: '))
#
#
# def func(result):
#     if x <= -2:
#         result = 1 - (x + 2)**2
#     elif -2 < x <= 2:
#         result = -1 * (x / 2)
#     elif x > 2:
#         result = (x - 2)**2 + 1
#     return result
#
#
# print(func(x))

# 13 3
# nums = [852, 85, 784, 58]
#
#
# def div_nums(nums):
#     iter = 1
#     while iter < len(nums)+1:
#
#         if nums[len(nums)-iter] % 2 != 0:
#             del nums[len(nums)-iter]
#         else:
#             nums[len(nums)-iter] = nums[len(nums)-iter]//2
#             iter += 1
#
#     return nums
#
#
# print(div_nums(nums))
