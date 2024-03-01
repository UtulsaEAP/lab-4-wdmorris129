"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Will Morris
Lab Time: Friday Afternoon

"""


def reverse_binary():
    numBinary = ''
    
    while numUser > 0:
        numBinary += str(numUser % 2)
        numUser //= 2
    
    return numUser

numUser = int(input())




if __name__ == "__main__":
    reverse_binary()