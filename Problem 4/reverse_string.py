"""
Complete the following python code to reverse the string entered by the user.

Name: 
Lab Time:
"""

def reverse_string():
    while True:
        forwardLine = input()
        
        if forwardLine.lower() in ['done', 'd']:
            break      
    
        backwardLine = forwardLine[::-1]
        print(backwardLine)
    


if __name__ == "__main__":
    reverse_string()