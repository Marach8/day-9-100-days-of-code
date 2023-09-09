a = int(input('Enter your birth year!: '))
print()
if 1883 <= a <= 1990:
  print('Hey! you belong to the Lost Generation!')
elif 1901 <= a <= 1927:
  print('Hey ! you belong to the Greatest Generation!')
elif 1928 <= a <=1945:
  print('Hey! you belong to the Silent Generation!')
elif 1946 <= a <= 1964:
  print('Hey! you belong to the Baby Boomers')
elif 1965 <= a <= 1980:
  print('Hey! you belong to Generation X!')
elif 1981 <= a <= 1996:
  print('Hey! You are Millenials!')
elif 1997 <= a <= 2012:
  print('Hey! You belong to Generation Z!')
elif a >= 2012:
  print('Hey! you belong to Generation Alpha!')
else:
  print('You must be an ancestor!🤣😂')