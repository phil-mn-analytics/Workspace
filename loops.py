
#ranged for loops
for i in range(3):
  print(i)

for i in range(10):
  print(i)

#nested for loop
teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
for team in teams:
  for name in team:
    print(name)

#while loops
i = 1
while i < 6:
  print(i)
  i += 1

# for loop
nums = [3, 4, 16]
 
print('This is an example of for loops')

for num in nums:
   print(num ** 2)
 
# while loop
i = 3

print('This is an example of while loops')

while i < 258:
   print(i)
   i = i ** 2