"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Will Morris
Lab Time: Friday Afternoon
"""

def norm():
    # Write your code here
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())

    numList = [a, b, c, d, e, f]
    maxValue = max(numList)

    for val in numList:
        newValue = val / maxValue
        print(f"{newValue:.2f}")

    
    
if __name__ == "__main__":
    norm()