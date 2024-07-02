""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 4  # Replace the assignment with a positive integer to test your code.
lst = [1, 2, 3, 4, 5, 6, 7]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 1 below here.
count=0
for i in range(0,len(lst)):
    if lst[i]%a==0:
        count +=1
        if count==3:
            print(i)
if count<3:
    print(-1)

# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
lst2 = ['rick', 'and', 'morty']
# Replace the assignment with other lists of strings (str) to test your code.


# Write the code for question 2 using a for loop below here.
leng=len(lst2)
total=0
for elem in lst2:
    total += len(elem)
avg=total/leng
counter2=0
for elem in lst2:
    if len(elem)>avg:
        counter2 +=1
print('the number of strings longer than the average is:', counter2)
# Write the code for question 2 using a while loop below here.
leng2=len(lst2)
total2=0
counter22=0

while counter22<len(lst2):
    counter22 +=1
    total2 += len(lst2[counter22-1])
avg2=total2/leng2

new_lst2=[]
counter23=0
counter24=0
while counter24<len(lst2):
    counter24 += 1
    if len(lst2[counter24-1])>avg2:
        counter23 += 1

print('the number of strings longer than the avergae is:' , counter23)


# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

lst3 = [0, 1, 4, 3]  # Replace the assignment with other lists to test your code.


# Write the rest of the code for question 3 below here.
if len(lst3)<=1:
    print('0')
else:
    value=[]
    for n in range(1,len(lst3)):
        value.append(abs(lst3[n]-(lst3[n-1])))
    SUM=0
    for i in range(0,len(value)):
        SUM += value[i]
    print(SUM)



# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

lst4 = [1, 3, 0, 2]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 4 below here.
new_lst4=[lst4[0], lst4[1]]
max=abs(lst4[0]*lst4[1])
for n in range(2,len(lst4)):
    if abs(lst4[n-1]*lst4[n])>max:
        max= abs(lst4[n-1]*lst4[n])
        new_lst4.append(lst4[n])
    else:
        max=max
print(new_lst4)


# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaadddefffgg'  # Replace the assignment with other strings to test your code.
k = 3  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.
high='0'
for i in range(0,len(my_string)):
    if my_string.count(my_string[i]) >= k:
        if my_string.count(my_string[i]*k)>=1 and my_string[i]>high:
            high=my_string[i]
if my_string.count(high)<k:
    print("did't find a substring of lenght" , k)
else: print('For lenght', k , ", found the substring " + high*k , "!")

# End of code for question 5
