
# ## New iteration #1 my code
# b = 1
# a = 1
# result = 0
# for i in range(100):
# 	b, a = a, (a + b)
# 	if a % 2 == 0 and a < 4000000:
# 		print(f"Adding {a} to result: {result} => {result + a}")
# 		result += a
# print(result)


## New iteration #1 my code
# b = 1
# a = 1
# result = 0
# while True:
# 	b, a = a, (a + b)
# 	if a < 4000000 :
# 		if a % 2 == 0:
# 			print(f"Adding {a} to result: {result} => {result + a}")
# 			result += a
# 	else :	
# 		break
# print(result)

# Aly code

def getEvenFibonacciSumUnderN(n: int):
	"""
	Returns the sum of all even fibonacci numbers less than `n`.

	Fibonacci numbers: 1 1 2 3 5 8 13 21 34 55 89 144

	>>> getEvenFibonacciSumUnderN(10)
	10  # 2 + 8
	>>> getEvenFibonacciSumUnderN(20)
	10  # 2 + 8
	>>> getEvenFibonacciSumUnderN(50)
	44  # 2 + 8 + 34
	"""
	num1, num2 = 1, 1
	evenFibSum = 0

	while True:
		newNum = num1 + num2
		if newNum >= 4000000:
			break
		elif newNum % 2 == 0:
			evenFibSum += newNum
		num1 = num2
		num2 = newNum

	return evenFibSum


evenFibSumUnder4Million = getEvenFibonacciSumUnderN(4000000);
print(f"Sum of even fibonacci nums under 4 mil: {evenFibSumUnder4Million}")


