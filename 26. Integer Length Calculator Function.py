print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("This is a program to print the length of the integer, like len() function does for strings.")

# def int_len(a):
    # if a<10 and a>0:
    #     print(1)
    # if a<100 and a>9:
    #     print(2)
    # if a<1000 and a>99:
    #     print(3)
    # if a<10000 and a>999:
    #     print(4)
    # if a<100000 and a>9999:
    #     print(5)

def int_len(a):
    i=0
    j=10
    k=0
    # for k in range(1,99999999999999999):
    while True:
        k=k+1
        if a<j and a>i:
            return(k)
            # print(k)
            break
        j=j*10
        i=(i*10)+9

i=int(input("Enter the number for which you want to find the length: "))
print(int_len(i))