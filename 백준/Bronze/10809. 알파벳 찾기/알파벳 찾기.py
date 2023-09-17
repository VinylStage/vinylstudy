from string import ascii_lowercase

s = input()
print(' '.join([str(s.find(i)) if i in s else '-1' for i in ascii_lowercase]))