class person:
    def __init__(self,name,email):
        self.name=name
        self.email=email
class teacher(person):
    def __init__(self,name,email,subject):
        super().__init__(name,email)
        self.subject=subject
class student(person):
    def __init__(self,name,email,branch):
        super().__init__(name,email)
        self.branch=branch
class college:
    def __init__(self,cid,name):
        self.cid=cid
        self.name=name
        self.teacher=[]
        self.student=[]
    def add_teacher(self,teacher):
        self.teacher.append(teacher)
    def add_student(self,student):
        self.student.append(student)
    def display_teacher(self):
        if len(self.teacher)==0:
            print("No teachers in the list")
        else:
            for x in self.teacher:
                print("Name:",x.name)
                print("Email:",x.email)
                print("subject:",x.subject)
                print()
    def display_student(self):
        if len(self.student)==0:
            print("No students in list")
        else:
            for x in self.student:
                print("Name:",x.name)
                print("Email:",x.email)
                print("Branch:",x.branch)
                print()
colleges=[]
while True:
    print("Choose your option")
    print("1. To create college:")
    print("2. To add Teachers:")
    print("3. To add students:")
    print("4.To Display Teachers:")
    print("5.To Display Students:")
    print("6.Exit:")
    option=int(input("Enter your option:"))
    if option == 1:
        clg_id=int(input("Enter college id :"))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                x = True
                break
        if x==True:
            print(f"college with {clg_id} is already exist,try again")
        else:
            clg_name=input("Enter college Name:")
            clg=college(clg_id,clg_name)
            colleges.append(clg)
            print("College created successfully")
            
    elif option==2:
        clg_id=int(input("Enter college id:"))
        for val in colleges:
            if val.cid==clg_id:
                clg1=val
                x=True
                break
        if x==True:
            name=input("Enter Name:")
            email=input("Enter email:")
            subject=input("Enter subject:")
            t = teacher(name,email,subject)
            clg1.add_teacher(t)
            print()
            print(f"Teacher Added Sucessfully to {clg1.name}")
            print()
        else:
            print("College does not exists")
    elif option==3:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x==True:
            name=input("Enter student name:")
            email=input("Enter student Email:")
            branch=input("Enter student branch:")
            s=student(name,email,branch)
            clg1.add_student(s)
            print(f"student added successfully to {clg1.name}")
        else:
            print("college does not exists")
    elif option==4:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x == True:
            clg1.display_teacher()
        else:
            print()
            print("College Does not Exists")
            print()
    elif option==5:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x == True:
            clg1.display_student()
        else:
            print()
            print("College Does not Exists")
            print()
    elif option==6:
        break
    else:
        print("worng option opted,try again")
    
            
    
    
            
        
            
        
    


            
            
    
        
        
    
    
    
