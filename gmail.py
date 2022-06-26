# Hi this is me Amar Dagaura , s_ID:210129
#------------------------------------------------Email Varifications Tool-------------------
#Only Email,Gmail, outlook and softwarica email varification tool 
email = input("Enter your email address: ")
a,b,c=0,0,0
if len(email)>=6 and len(email)<=30:
    if email[0].isalpha() or email[1].isdigit():
        if ("@" in email) and (email.count("@")==1):
            if (email[-10]=="@" or email[-12]=="@" or email[-18]=="@" or email[-23]=="@"):
                if ("." in email) and (email.count(".")==1) or (email.count(".")==2):
                    if (email[-4] or email[-3] or email[-7]=="."):
                        for i in email:

                            if i.isspace():
                                a=1
                                print("\n-Whitespace Invalid email")
                            elif i.isalpha():
                                if i==i.upper():
                                    b=1
                                    print("\n-UPPER case Invalid email")
                            elif i.isdigit():
                                continue
                            elif i=="." or i=="@":
                                continue
                            else:
                                c=1

                        if a==1 or b==1 or c==1:
                            print("Something Went Wrong!,>>Special characters == error!<< ")
                        else:
                            print("\nWelcome!\n You Have Entered Valid Email\n")
                    
                    else:
                        print("Please check! '.' is in wrong position")
                else:
                    print("Please check! your email and try again")
            else:
                print("Please check! '@' is in wrong position")
        else:
            print("Please check! Multiple'@' is not valid")
    else:
        print("Email most be in text format")
else:
    print("Sorry! you have to check your email length size.")
