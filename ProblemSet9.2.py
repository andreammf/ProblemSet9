import sys
num = int(input("height: "))

if num > 8 or num < 0:
    print("Error")
    sys.exit(1)
    # raise(OverflowError("the input should be between 0 and 8!"))

for i in range(1,num+1):
    # for j in range(1,i+1):  
    print("#" * i )
    # print()
