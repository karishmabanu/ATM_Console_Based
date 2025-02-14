accounts={1920:["user1",1916,1000,"user1@gmail.com"],
          1921:["user2",2917,5000,"user2@gmail.com"],
          1923:["user3",None,10000,"user3@gmail.com"]}
while True:
    print("select your option: ")
    print("1. check balance ")
    print("2. withdraw ")
    print("3. Deposit ")
    print("4. Pin Generation ")
    print("5. Exit ")
    x=int(input("select your option: "))
    print("**********************************")
    if x==1:
        acc=int(input("enter account number: "))
        if acc not in accounts:
            print("Invalid account number")
        else:
            pin=int(input("enter your pin "))
            if accounts[acc][1]==pin:
                print(accounts[acc][2])
            else:
                print("Invalid pin")
    
    elif x==2:
        acc=int(input("enter account number: "))
        if acc not in accounts:
            print("Invalid account number")
        else:
            pin=int(input("Enter your pin: "))
            if accounts[acc][1]==pin:
                amt=int(input("Enter amount: "))
                if accounts[acc][2]>=amt:
                    accounts[acc][2]=accounts[acc][2]-amt
                    print("amount withdraw successfully")
                else:
                    print("Insufficient balance")
            else:
                print("Invalid pin")
    
    elif x==3:
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            amt = int(input("Enter Amount: "))
            accounts[acc][2] += amt
            print("Deposit Sucessfull !")
    
    elif x==4:
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            if accounts[acc][1] is not None:
                print("Pin Already Generated !")
            else:
                pin = int(input("Enter New Pin: "))
                accounts[acc][1] = pin
                print("Pin Generated Sucessfully !")
    
    elif x == 5:
        print("Thank you ")
        print("Visit Again")
        break
                
                    
                
        
        
    
        
        
                    
          

          
          