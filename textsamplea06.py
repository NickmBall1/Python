'''Use nested for loops to print triangles with ***'''
#nested for loops
n = 1
m = 10
for x in range(n, m+1):
       for y in range(1, x):
              print('*', end = ' ')
       print('\n')
'''How to use for loop with list'''
sum = 0
numbers = [2, 3, 12, 34, 19]
for x in numbers:
       if x%3 == 0:
              print(x)
'''How to check for vowels in a string'''
count = 0
text = "This is to count the number of vowels"
for x in text:
       if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
              count = count + 1
print(count)
       

       
