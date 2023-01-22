# Homework 1
#
# How much building material is needed to cover the entire floor? 
# How much baseboard material is needed to be installed into the room?
#
# user inputs longest lenght of the room in inches in case room is irregular. Inches will be converted to feet
length = int(input("What is the largest length of the subject room in total inches? "))
# user inputs largest width of the room in inches in case room is irregular. Inches will be converted to feet
width = int(input("What is the largest width of the subject room in total inches? ")) 
# square footage equation for flooring materials           
floor_area = length*width/12
# equation for total footage of required baseboards
perimeter = (length+width)*2/12
# line space
print()
# final calculations statement
print ("You need ", floor_area, " square feet of flooring materials and ", perimeter, "feet of baseboards for the  subject room.")