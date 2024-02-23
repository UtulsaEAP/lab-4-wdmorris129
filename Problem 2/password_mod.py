"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Will Morris
Lab Time: Friday Afternoon
"""

def password_mod(password):
    oldPassword = input()
    password = ''
    # Type your code here.
    password = oldPassword.replace('i', '1').replace('a','@').replace('m','M').replace('b','8').replace('s','$')
    word += '!'
    return password

password = password_mod(oldPassword)

if __name__ == "__main__":
    password_mod()