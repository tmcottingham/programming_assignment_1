# Tara Cottingham
# Course: CS151, Dr. Simari
# Date: Feb 10, 2020
# Programming Assignment #1
# Program inputs: length in feet, width in feet, height in feet
# Program outputs: total area to be painted (in square feet), amount of paint and primer (in gallons)

# Program purpose
print('This program will calculate the total area to be painted (in square feet) and determine the amount of paint and'
      'primer (in gallons) needed')

# ask user for length (in feet)
length = input('Please enter the length (in feet): ')
length = int(length)

# ask user for width (in feet)
width = input('Please enter the width (in feet): ')
width = int(width)

# ask user for height (in feet)
height = input('Please enter the height (in feet): ')
height = int(height)

# measure total distance of room
total_distance = (length+width)*2

# measure wall area of room
wall_area = total_distance*height

# compute area of ceiling
ceiling_area = length*width
ceiling_area = int(ceiling_area)

# compute the overall area of the room (including ceiling)
overall_wall_area = wall_area + ceiling_area
overall_wall_area = int(overall_wall_area)

# output total area of room (including ceiling)
print('The total area to be painted is: ', overall_wall_area)

# output amount of paint (in gallons)
gallons_paint = overall_wall_area/350
print('The amount of paint (in gallons) needed is: ', gallons_paint)

# output amount of primer (in gallons)
gallons_primer = overall_wall_area/200
print('The amount of primer (in gallons) needed is: ', gallons_primer)

# thank the user for using the program
print('Thank you for using the program!')
