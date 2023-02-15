# num_rows = int(input("Enter the number of rows"));
# for i in range(0, num_rows):
# 	for j in range(0, num_rows-i-1):
# 		print(end=" ")
# 	for j in  range(0, i+1):
# 		print("*", end=" ")
# 	print()

n=5
def factorial(n):

    if n ==1:
        return 1
    else:
        return n* factorial(n-1)


