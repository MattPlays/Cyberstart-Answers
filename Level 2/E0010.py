# CHALLENGE 1: Create an empty array called numbers.
numbers = []
# CHALLENGE 2: Write a while loop that will add 100 numbers to the
#              array, starting from the number 100 and incrementing by
#              2 each time. For example, start from 100, then the next
#              number added will be 102, then 104 and so on.
for x in range(100, 301, 2):
  numbers.append(x)
# CHALLENGE 3: Write a for loop that will look through your numbers
#              array and print out each value in the array.
for x in numbers:
  print(x)