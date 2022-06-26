email=input(" Enter your Email:") # a  m  a   r d  a  g  a  u  r  a  1  2  3  @  g m a i l . c o m
                                  # 24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1
a=0
b=0
c=0
if len(email)>=6 and len(email)<=30: # first is Alphabetical letter
    if email[0].isalpha(): # isalpha is funciton #0 is email first letter 
        if ("@" in email) and (email.count("@")==1): # membership operator
            if (email[-10]=="@") and (email[-4]=="."):

                #for loop upto c = 
                for i in email:
                    # is space or not 
                    if i==i.isspace():
                        a=1
                        print("\n space is invalid in email:")
                    elif i.isalpha():
                        #is upper case or not and will chenge into UPPER
                        if i==i.upper(): 
                            b=1
                            print("hello")
                    # is check digits in email
                    elif i.isdigit():
                        continue
                    # is check _@. in email for vailed 
                    elif i=="." or i=="@":
                        continue
                    
                    else:
                        c=1   

                if c==1:
                    print("\n5 Something went wrong:")#5th space condition email
                else:
                    print("\n6. Thank You!\nYou have entered varified Email\nYour valic Email is :",email)    
            
            else:
                print("\n4. .position is wrong in Email")# 4th condition wrong email
        else:
            print("\n3.Sorry,only one @ is valid for Email")# 3rd condtion wrong emaill
    else:
        print("\n2.Sorry, Invalid Email Address")# 2nd condition wrong email
else:
    print("\n1.Sorry! Please enter valid Email") # 1st condition wrong email


