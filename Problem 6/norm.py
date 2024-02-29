"""
Complete the following python code to take in a list of values from the user and then normalize them

Name:
Lab Time:
"""

def norm():
    # Write your code here
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()
    f = input()

    numList = {a, b, c, d, e, f}

    if a >= {a, b, c, d, e, f}:
        numList == numList / a
    if b >= {a, b, c, d, e, f}:
        numList == numList / b
    if c >= {a, b, c, d, e, f}:
        numList == numList / c
    if d >= {a, b, c, d, e, f}:
        numList == numList / d
    if e >= {a, b, c, d, e, f}:
        numList == numList / e
    if f >= {a, b, c, d, e, f}:
        numList == numList / f
   
    print("%.2f" % numList )
    
    
if __name__ == "__main__":
    norm()