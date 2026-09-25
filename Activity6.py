#Dan Rey G. Lumiib
#8-Adelfa

print("<===========================>")
print("Payment Method Checker")
print("<===========================>")
#This is the only things that is allowed to be a valid payment method
valid_payment_method = ["GCASH","Cash","Card"]
#Get the user input for the payment method
payment_method = input("Enter payment method whether it is GCASH, Cash or Card: ")
#Check if the user's payment method is in the valid methods
if payment_method in valid_payment_method:
    print("Valid payment method")
else:
    print("Invalid payment method")

print("<===========================>")
print("Grade Checker")
print("<===========================>")
#Get the user's grade
student_grade = int(input("Enter student grade: "))
#To check if the grade of the student is in the valid number from 0 to 100
if 0 <= student_grade <= 100:
    print("Valid Grade.")
else:
    print("Invalid Grade.")

print("<===========================>")
print("Student ID checker")
print("<===========================>")
#To get the re
import re
#To get the user's student id
student_id = input("Enter student id: ")
#This will be the pattern the student will need to follow
pattern = r"\d{4}-\d{4}"
#To check if what the user tried to input is in the correct pattern
if re.fullmatch(pattern, student_id):
    print("Valid Student Id")
else:
    print("Invalid Student Id")

print("<===========================>")
print("PIN Validator")
print("<===========================>")
#To get the user's pin/password
pin = input("Enter a 6-digit password: ")
#To check if the pin is within 6 digits and to check if there are no letters involved
if len(pin) == 6 and pin.isdigit:
    print("Valid password.")
else:
    print("Invalid password.")

print("<===========================>")
print("Student Score Entry")
print("<===========================>")
#To get the user's examination score
score = int(input("Enter examination score: "))
#Check if the score is within 0 to 100 range and to check if it's a digit
if 0 <= score <= 100 and score.isdigit:
    print("Valid score")
else:
    print("Invalid score. Please enter a number")