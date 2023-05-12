# n=1000
# a=3
# b=5

# --- sum up
# --- write that

# n/3 or n/5 = sum 

# z=0

# 	n+1
# 	list  = ()
# 	break 1001


total = 0
for n in range(1000):
	if n%3 == 0 :
		total += n #----- total = total + 1
	if n%5 == 0 and n%3 !=0 :
		total += n
print("Total: ", total)

