[Adelfa_Lumiib_Activity4.md](https://github.com/user-attachments/files/31948078/Adelfa_Lumiib_Activity4.md)
import math

##  Hypotenuse Calculator

##  Purpose
The purpose of this program is to calculate the hypotenuse
##  How to run
Input the two sides of the triangle and the program can calculate it
##  Input needed
Put the two sides of the triangle into the chat and just wait for it to calculate
##  Sample output
side a:8
side b:9
The output will be "The Hypotenuse is: 12.041594578792296"

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
