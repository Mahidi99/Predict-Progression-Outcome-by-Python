# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 2019766
# Date: 03/04/2020


def Pass_Credits():
    passes = int(input("Please Enter Pass Credits : "))
    while(passes>120 or passes<0 or passes%20!=0):
        print("\t Range Error")
        passes = int(input("Please Enter Pass Credits : "))
            
    return passes

def Defer_Credits():
    defer = int(input("Please Enter Defer Credits : "))
    while(defer>120 or defer<0 or defer%20!=0):
        print("\t Range Error")
        defer = int(input("Enter Defer Credits : "))
            
    return defer

def Fail_Credits():
    fail = int(input("Please Enter Fail Credits : "))
    while(fail>120 or fail<0 or fail%20!=0):
        print("\t Range Error")
        fail = int(input("Please Enter Fail Credits : "))
            
    return fail
    
def Progression():
    if passes + defer + fail == 120:
        if passes == 120:
            print("\t Progress")
        elif(passes==100):
            print("\t Progress - module trailer")
        elif(fail>=80):
            print("\t Excludes")
        else:
            print("\t Do not progress – module retriever")
    else:
        print("\tTotal Incorrect")
condition = 0
while (condition == 0):
    try:
        passes = Pass_Credits()
        defer = Defer_Credits()
        fail = Fail_Credits()
        Progression()
                    
        condition = 1
    except:
        print("\t Integer Required")




 
