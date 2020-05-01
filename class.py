class Student:
    def __init__(self , name , roll , fees):
        self.name = name
        self.roll = roll
        self.fees = fees
        
    def display(self):
        print(f'Name : {self.name}')
        print(f'Roll no. : {self.roll}')
        print(f'Fees : {self.fees}')


student1st = Student("Ashu",26,32000 )
student1st.display()