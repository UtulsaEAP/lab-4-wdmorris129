"""
Complete the following python code to reverse the string entered by the user.

Name: 
Lab Time:
"""

def reverse_string():
# YOUR CODE HERE
    while True:
        forwardLine = input("")
        
        if  forwardLine.lower() in ['done', 'd']:
            break      
    
        backwardLine = forwardLine[::-1]
        print(backwardLine)
    


if __name__ == "__main__":
    reverse_string()

# def reverse_input():
#     while True:
#         # Get input from the user
#         line = input("Enter a line of text (or 'Done' to exit): ")

#         # Check if the user wants to exit
#         if line.lower() in ['done', 'd']:
#             break

#         # Print the reversed line of text
#         reversed_line = line[::-1]
#         print(reversed_line)

# if __name__ == '__main__':
#     reverse_input()