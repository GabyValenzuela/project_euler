"""Solution to problem 1 P. Euler, using WHILE loop"""

threshold = 1000

i = 0
lst= []
sum_i = 0
limit = (threshold - 1)
        
while i < limit: 
    i += 1
    if i%3 == 0:
        lst.append(i)
        sum_i = sum(lst)
    elif i%5 ==0:
        lst.append(i)
        sum_i = sum(lst)
    else:
        continue
    
print("Total: ", sum_i)





"""Solution to problem 1 P. Euler, using FOR loop"""

total = 0

for n in range(1000):  #RANGE() is exclusive by default, meaning that it won't consider the last value, in this case, 1,000.
    if n%3 == 0:
        total += n
    elif n%5 == 0 :
        total += n
    else:
        continue

print("Total: ", total)





"""
#Solution to problem 1 P. Euler, using WHILE loop w/COMMENTS

threshold = 1000  # Change or play with this threshold to test a smaller number than the current one

i = 0
lst= []
sum_i = 0

#This limit ensures that the threshold number is not considered, as the addition happens after the 
#condition that checks the limit. For this example, if we had placed 'threshold' instead of 'limit', 999 would
#pass the condition of being smaller than 1,000 but then 1,000 would be considered in the calculation, giving us an 
#error in the final sum of the natural numbers that are divisible by 3 and 5.
limit = (threshold - 1)
        
while i < limit: 
    i += 1
    if i%3 == 0:
        lst.append(i)
        sum_i = sum(lst)
        #print(sum_i)     # I left this print here in case someone needs to test the code and see how the sum accumulates with every number added to the list
    elif i%5 ==0:
        lst.append(i)
        sum_i = sum(lst)
        #print(sum_i)     # Same comment as above
    else:
        continue
    
#print(lst) #I left this print in case this code gets tested for a smaller number and someone wants to see the result of all the numbers added
print("Total: ", sum_i)

"""