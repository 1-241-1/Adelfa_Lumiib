import math

#Hypotenuse Calculator

#Ask the user for the length of the two shorter side
side_a = float(input('Enter the length of Side A: '))
side_b = float(input('Enter the length of Side B: '))

#Square the two side length
a_squared = math.pow(side_a, 2)
b_squared = math.pow(side_b, 2)

#Add all the side values together
sum_of_squares = a_squared + b_squared

#Use math.sqrt to calculate for the hypotenuse
hypotenuse = math.sqrt(sum_of_squares)

#Display the Hypotenuse
print(f'The Hypotenuse is: {hypotenuse}')
