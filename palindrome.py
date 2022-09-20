def is_palindrome(word):
  rword = str(word)[::-1]
  if str(word) == rword:
    return True
  return False

n = 'rotator'

print(is_palindrome(n))