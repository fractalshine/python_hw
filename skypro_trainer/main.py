def lost_time(*nums):
    return sum(nums)


# Не удаляйте код ниже, он нужен для проверки

numbers = [int(x) for x in input().split(" ")]
print(lost_time(*numbers))
