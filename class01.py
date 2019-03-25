# write a program that takes number of range and print sum of them
# i, odd number ii, even number iii, list input iv, list odd index v, list even index
sum = 0
for i in range(0,10):
   sum = sum + i
print(sum)
# odd sum
sum1 = 0
for i in range(10):
    if i%2 == 1:
        sum1 = sum1 + i
print('odd sum', sum1)

# even sum
sum2 = 0
for i in range(10):
    if i%2 == 0:
        sum2 = sum2 + i
print('even sum: ', sum2)

# list odd sum
sum3 = 0
for i in [1,2,3,4,5,6,7,8,9]:
    if i%2 == 1:
        sum3 = sum3 + i
print('list odd sum: ',sum3)

# list even sum
sum4 = 0
for i in [1,2,3,4,5,6,7,8,9,10,45,78,60]:
    if i%2 == 0:
        sum4 = sum4 + i
print('list even sum: ',sum4)

# list even index aita pari na
list = [4,8,9,7,6,4,8,2,6,7,9,8,4,6]

#  string len
string = 'my name is subena'
print('Lenth of string: ',len(string))

#  string reverse
print(string[::-1])

number = 2
string = 'subena'





