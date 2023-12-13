# take input from input.txt and scan through each line printing each line in the input.txt file
file = open('input.txt', 'r')

# create a dictionary to store the max nummers of coloured cubes in a match
# ex. "red": 12, "blue": 14, "green": 13
MaxNumberOfCubes = {"red": 12, "green": 13, "blue": 14 }

# create a variable to store the sum of the game numbers that have valid matches
sum = 0

for line in file:
    # take each line a split into 2 parts using the : as the delimiter
    parts = line.split(':')

    # get the game number
    game = parts[0].split(' ')
    gameNumber = int(game[1])
    
    # create a variable to store the validity of the game
    isValid = True
    print('Game #' + str(gameNumber))


    # get the bags in the game
    RecordOfMatches = parts[1]
    
    # split the bags into an array of bagMatches using the ; as the delimiter
    # remove the leading whitespace from each bag mach using the strip() function
    print('Record of matches: ' + RecordOfMatches)

    # take each match in the record of matches
    # and split them using the ; as the delimiter
    # store the matches in an array
    matches = RecordOfMatches.split(';')

    # loop through each match in the matches array unless there is a match that is invalid
    # this invalid match will be triggerd by the isValid variable
    # if the isValid variable is false, the loop will break
    # if the isValid variable is true, the loop will continue
    # this is done to prevent the loop from continuing if there is an invalid match
    for match in matches:
        if isValid == False:
            break

        match = match.strip()
        # print('Bag pull: ' + match)
        # split each match by the, delimiter into an array
        cubes = match.split(',')
        
        # get the colour of the bag
        for cube in cubes:
            cube = cube.strip()
            # print('Cube: ' + cube)
            
            # split the cube into the colour and the number of that colour cube
            cubeParts = cube.split(' ')
            numberOfCubes = cubeParts[0]
            colour = cubeParts[1]
            # print('Number of cubes: ' + numberOfCubes)
            # print('Colour: ' + colour)
                
            # check if the number of cubes is greater than the max number of cubes for that colour
            if int(numberOfCubes) > MaxNumberOfCubes[colour]:
                isValid = False
                break
            # else:
            #     print('Bag ' + match + ' is valid')
        
    if isValid == True:
        print('Game #' + str(gameNumber) + ' is valid\n\n')
        sum += gameNumber
    else:
        print('Game #' + str(gameNumber) + ' is invalid\n\n')

print('Sum of valid games: ' + str(sum))
    