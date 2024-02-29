"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name:
Lab Time:
"""

# def brute_eq():
#     #Read in first equation, ax + by = c 
#     a = int(input())
#     b = int(input())
#     c = int(input())

#     #Read in second equation, dx + ey = f
#     d = int(input())
#     e = int(input())
#     f = int(input())

#     # YOUR CODE HERE
#     for x in range [-10,10]:
#         for y in range [-10,10]:
#             if a * x + b * y == c and d * x + e * y == f:
#                 return x , y
#         return None
    
# if __name__ == "__main__":
#     brute_eq()

def find_integer_solution(a1, b1, c1, a2, b2, c2):
    for x in range(-10, 11):
        for y in range(-10, 11):
            if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2:
                return x, y

    return None

if __name__ == '__main__':
    # Get coefficients from the user
    a1 = int(input("Enter coefficient a1: "))
    b1 = int(input("Enter coefficient b1: "))
    c1 = int(input("Enter coefficient c1: "))
    a2 = int(input("Enter coefficient a2: "))
    b2 = int(input("Enter coefficient b2: "))
    c2 = int(input("Enter coefficient c2: "))

    # Find the integer solution using brute force
    solution = find_integer_solution(a1, b1, c1, a2, b2, c2)

    # Output the result
    if solution:
        print(f"x = {solution[0]}, y = {solution[1]}")
    else:
        print("There is no solution")