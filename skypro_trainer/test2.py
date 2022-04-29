# print("Enter the array:\n")
# new_string = input().splitlines()
# print(new_string)

import sys
userInput = sys.stdin.readlines()
new_lst = [x[:-1] for x in userInput]
print(new_lst)
