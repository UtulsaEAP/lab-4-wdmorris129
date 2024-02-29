"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name:
Lab Time:
"""

# def brute_eq():
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     d = int(input())
#     e = int(input())
#     f = int(input())

#     # YOUR CODE HERE
#     for x in range [-10,10]:
#         for y in range [-10,10]:
#             if a * x + b * y == c and d * x + e * y == f:
#                 print(f"x = {x}, y = {y}")
#                 return        
    
# print("There is no solution")
    
# if __name__ == "__main__":
#     brute_eq()

def brute_eq():
    a1 = int(input())
    b1 = int(input())
    c1 = int(input())
    a2 = int(input())
    b2 = int(input())
    c2 = int(input())

    for x in range(-10, 11):
        for y in range(-10, 11):
            if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2:
                print(f"x = {x}, y = {y}")
                return

    print("There is no solution")

if __name__ == "__main__":
    brute_eq()

