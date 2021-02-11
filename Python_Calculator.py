
#  define some arithmetic operation
def sum(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def multip(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2
#define some log method
def log_num(n):
    print(str(n))
def strTOnum(str):
    return float(str)
x = True
while x:
    input1 = input("Do you want to do a calculation ? [y/n]")
    if (input1 == "y" ):
        #define input variable
        n1,op,n2 = input("inter a problem: ").split()
        n1 = strTOnum(n1)
        n2 = strTOnum(n2)
                #Logic under the calculator
        if (op == "+" or op =="plus" or op == "Add"):
            log_num(sum(n1,n2))
            x = True
        elif (op == "*" or op =="time" or op == "multi"):
            log_num(multip(n1,n2))
            x = True
        elif (op == "/" or op =="by" or op == "devid"):
            log_num(div(n1,n2))
            x = True
        elif (op == "-" or op =="minus" or op == "devid"):
            log_num(sub(n1,n2))
            x = True
        else :
            print("Enter a valid operator")
            x = False

    elif(input1 == "n"):
        break
    else:
        print("enter a valid argument ")
        x = True

