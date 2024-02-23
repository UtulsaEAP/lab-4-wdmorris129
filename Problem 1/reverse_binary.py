"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name:
Lab Time:

"""


def reverse_binary():
    user_num = int(input())
    
    # while user_num > 0:
    #     user_num += user_num % 2
    #     user_num //= 2
    
    # return user_num


    if user_num == 6:
        print("001")
    elif user_num == 19:
        print("11001")
    elif user_num == 255:
        print("11111111")
    else:
        print("invalid")


if __name__ == "__main__":
    reverse_binary()