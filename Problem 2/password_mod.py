"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Will Morris
Lab Time: Friday Afternoon
"""

def password_mod():
    oldPassword = input()
    # password = ' '
    # Type your code here.
    password = oldPassword

    if "i" in oldPassword:
        password = password.replace("i", "1")
    if "I" in oldPassword:
        password = password.replace("I", "1")
    if "a" in oldPassword:
        password = password.replace("a", "@")
    if "A" in oldPassword:
        password = password.replace("A", "@")
    if "b" in oldPassword:
        password = password.replace("b", "8")
    if "B" in oldPassword:
        password = password.replace("B", "8")
    if "m" in oldPassword:
        password = password.replace("m", "M")
    if "s" in oldPassword:
        password = password.replace("s", "$")
    if "S" in oldPassword: 
        password = password.replace("S", "$")
    
    
    password += '!'

    print(password)



if __name__ == "__main__":
    password_mod()
