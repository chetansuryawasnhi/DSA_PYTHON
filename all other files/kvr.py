print("Enter Number of Values and Press ! to stop")
lst=[]
while(True):
    value=input()
    if(not value.isalnum()) and (not value.isspace()):
        if(value.__contains__(".")):
            print("hii")
            lst.append(float(value))
        elif(value.startswith("-") and value.__contains__(".")):
            print("hii 2")
            lst.append(float(value))
        elif (value.startswith("-") ):
            print("hii 3")
            lst.append(float(value))
        elif(not value.__contains__(".")):
            print("hii 4")
            break
    else:
        print("else")
        lst.append(float(value))
print("List of Values={}".format(lst))