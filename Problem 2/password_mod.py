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
    
    if "a" in oldPassword:
        password = password.replace("a", "@")
    
    if "b" in oldPassword:
        password = password.replace("b", "8")
    
    if "m" in oldPassword:
        password = password.replace("m", "M")
    
    if "s" in oldPassword:
        password = password.replace("s", "$")

    password += '!'


    return password



if __name__ == "__main__":
    modified_password = password_mod()
    print(modified_password)