# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1761262
# IIT ID: 2019766
# Date: 07/04/2020

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
        print("\t Range Err*or")
        fail = int(input("Please Enter Fail Credits : "))
                    
    return fail

progress=0
module_trailer=0
excludes=0
module_retriever=0        
passes = 0
defer = 0
fail = 0

try:
    option=str(input("Do you want to quit the programme?(n/q) : ")) #n = no , q = quit    
    while(option=='n'):
        passes = Pass_Credits()
        defer = Defer_Credits()
        fail = Fail_Credits()
        if(passes+defer+fail!=120):
                print("\t Total Incorrect")
        else:
            if passes == 120:
                print("\t Progress")
                progress+=1
            elif(passes==100):
                print("\t Progress - module trailer")
                module_trailer+=1
            elif(fail>=80):
                print("\t Excludes")
                excludes+=1
            else:
                print("\t Do not progress – module retriever")
                module_retriever+=1          
        option=str(input("Do you want to quit the programme?(n/q) : ")) #n = no , q = quit
        continue
    
    else:
        if(option=='q'):
            print("Progress",progress," : ","*" * progress) 
            print("Trailing",module_trailer," : ","*" * module_trailer)
            print("Retriever",module_retriever,": ","*" * module_retriever)
            print("Exclude",excludes,"  : ","*" * excludes+"\n")
            print(progress + module_trailer + excludes + module_retriever,"outcomes in total.")
            
except:
    print("\t Integer Required")


