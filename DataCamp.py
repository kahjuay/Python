'''
# Addition and subtraction
print(5 + 5)
print(5 - 5)

# Multiplication and division
print(3 * 5)
print(10 / 2)

# Exponentiation
print(4 ** 2)

# Modulo
print(18 % 7)

# How much is your $100 worth after 7 years?
print (100 * 1.1 ** 7)

#print(dir())

#Lists
lista = [1, 3, 4, 2]
listb = [[1, 2, 3], [4, 5, 7]]
listc = [1 + 2, "a" * 5, 3]


print(lista)
print(listb)
print(listc)


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Elements start from 0!
# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3]+areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)

# Slicing includes the start index but not the end index!
# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print (upstairs)


# Subsetting lists of lists
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
print(x[2][0])
print(x[2][:2])


# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]
print(areas)

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
print(areas_1)

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage",15.45]
print(areas_2)


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
#areas_copy = areas
areas_copy = areas [:]
print(areas_copy)

# Change areas_copy
areas_copy[0] = 5.0
print(areas_copy)

# Print areas
print(areas)
print(areas_copy)


# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second
print(full)

# Sort full in descending order: full_sorted
full_sorted = sorted(full,reverse = True)

# Print out full_sorted
print(full_sorted)


# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()

# Print out room and room_up
print(room);print(room_up)

# Print out the number of o's in room
print(room.count("o"))
print(room_up.count("o"))


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20))

# Print out how often 14.5 appears in areas
print(areas.count(14.5))

# Use append twice to add poolhouse and garage size
areas.append(24.5);areas.append(15.45)


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

'''
# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2*math.pi*r

# Calculate A
A = math.pi*math.pow(r,2)

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))


# Definition of radius
r = 192500

# Import radians function of math package instead of all functionality
from math import radians as radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)


print ("This is the end of the file")