def is_palindrome(word):
    return word == word[::-1]


try:
  assert is_palindrome("level") == True
  assert is_palindrome("sagas") == True
  assert is_palindrome("hero") == False
  assert is_palindrome("drama") == False

except AssertionError:
  print("Неверно, проверьте функцию на разных значениях")

else:
  print("Все хорошо, все работает")