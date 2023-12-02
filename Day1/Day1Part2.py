# take input from input.txt and scan through each line printing each line in the input.txt file
file = open('input.txt', 'r')

# create a dictionary to store the int representation of each number spelled out with letters
# ex. "one" = 1, "two" = 2, etc.
numberDictionary = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

# create an array to store the sum of each line in the input.txt file
sumArray = []

# Part 2

# take each line (which is a string of alphanumerical characters) and split it into an array of numbers pulling
# go through each character in the string and see if it is a digit. If it is, add it to the array of numbers
# we also have to check if there are any words in the string that are in the dictionary.
# If there are, we add the value of the key matching the word to the array of numbers
# we also have to keep track of the index of each number in the string, so we can sort the array of numbers later

for line in file:
    numbers = []

    for (i, character) in enumerate(line, start=0):
        if character.isdigit():
            numbers.append([i, character])

    # append all the indexes of the words in the dictionary that are in the string to the array of numbers
    for word in numberDictionary:
        if word in line:
            numbers.append([line.index(word), str(numberDictionary[word])])
            # find the other indexes of the word in the string and append them to the array of numbers
            for i in range(line.count(word)-1):
                numbers.append([line.index(word, numbers[-1][0]+1), str(numberDictionary[word])])

    # sort the array of numbers by first index of each element in the array rows
    numbers.sort(key=lambda x: x[0])

    # check the length of each element in the array of numbers. If the length is 1, then the number is a single digit number and we multiply the value by 11
    if len(numbers) == 1:
        sumArray.append(int(numbers[0][1]) * 11)

    # if the length is greater than 1, then we take the first index [0] and last index [-1] of the array and combine them into a two digit number
    elif len(numbers) > 1:
        sumArray.append(int(numbers[0][1]+numbers[-1][1]))

print("Day 1 Part 2 Answer:", sum(sumArray))
