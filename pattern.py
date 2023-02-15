rows = 6


#     The first for loop (for i in range(1, rows + 1):) runs rows number of times,
#     where rows is equal to 6 in this case. 
#     This outer loop is responsible for creating each row of the pattern.

for i in range(1, rows + 1):

# The inner loop (for j in range(rows - i ):) generates the spaces in each row. 
# The number of spaces in each row is equal to rows - i, where i is the current iteration of the outer loop.
    for j in range(rows - i ):
        print(" ", end='')

# The next inner loop (for j in range(1, i-1):) generates the first half of the numbers in each row.
#  The number of numbers generated in each row is equal to i - 1, where i is the current iteration of the outer loop.

    for j in range(1, i-1):

        print(j, end="")

# Finally, the last inner loop (for j in range(i - 1, 0, -1):) generates the second half of the numbers in each row. 
# The numbers are generated in reverse order from i - 1 to 1, inclusive.

    for j in range(i - 1, 0, -1):

        print(j, end="")

# The print() statement outside the loops is used to create a new line after 
# each row is generated, making the pattern look like a pyramid.
    print()












