''' Exercise #1 '''

#########################################
# Question 1 - do not delete this comment
#########################################
S = 220.0 # Replace ??? with a positive float of your choice.
AB = 20.0 # Replace ??? with a positive float of your choice.
BC = 10.0 # Replace ??? with a positive float of your choice.
AD = 15.0 # Replace ??? with a positive float of your choice.
DC = 35.0 # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 1 below here.


perimeter= AB+BC+AD+DC
print("Perimeter is:" , perimeter)

EF=(AB+DC)/2
print("Midsegment is:", EF)

h=S/EF
print('Height is:', h)



#########################################
# Question 2 - do not delete this comment
#########################################
my_name = 'roy' # Replace ??? with a string of your choice.
# Write the rest of the code for question 2 below here.

print("Hello "+ my_name.upper()[0] + my_name[1:] + "!!")




#########################################
# Question 3 - do not delete this comment
#########################################
number  = '-17' # Replace ??? with a string of your choice.
# Write the rest of the code for question 3 below here.

if int(number) % 13 > 0:
    print("I am " , number , " and I cannot be divided by 13")

else:
    print("I am " , number , " and I am divisible by 13")




#########################################
# Question 4 - do not delete this comment
#########################################
text = 'tom' # Replace ??? with a string of your choice.
copies = 3  # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.


odds = text[1::2]
even = text[0::2]
output_str = (odds + even) * copies
print (output_str)





#########################################
# Question 5 - do not delete this comment
#########################################
name = 'kciRytroM' # Replace ??? with a string of your choice.
r = 4 # Replace ??? with a int of your choice.
# Write the rest of the code for question 5 below here.



lenght= len(name)
if r<0:
    print("error: not a legal input!")
elif not r<lenght:
    print("error: not a legal input!")
elif lenght==0:
    print("error: not a legal input!")
else:

    sub1= name[0:r]
    sub2= name[r:] 
    sub1= sub1[::-1]
    sub2= sub2[::-1]
    print(sub1 + " " + sub2)

