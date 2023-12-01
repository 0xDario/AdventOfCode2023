# take input from input.txt and scan through each line printing each line in the input.txt file
file = open('input.txt', 'r')

# create a dictionary to store the int representation of each number spelled out with letters
# ex. "one" = 1, "two" = 2, etc.
numberDictionary = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
                    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

# create an array to store the sum of each line in the input.txt file
sumArray = []

for line in file:
    # take each line (which is a string of alphanumerical characters) and split it into an array of numbers pulling
    # go through each character in the string and see if it is a digit. If it is, add it to the array of numbers
    numbers = []
    for character in line:
        if character.isdigit():
            numbers.append(character)

    print(numbers)

    # check the length of each element in the array of numbers. If the length is 1, then the number is a single digit number and we multiply the value by 11
    if len(numbers) == 1:
        sumArray.append(int(numbers[0]) * 11)

    # if the length is greater than 1, then we take the first and last element of the array and combine them into a two digit number
    elif len(numbers) > 1:
        sumArray.append(int(numbers[0]+numbers[-1]))

    print(sum(sumArray))


print("Part 1 Answer:", sum(sumArray))