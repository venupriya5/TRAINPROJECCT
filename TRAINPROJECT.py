import datetime #importing time module
import random #random to take random pnr numbers
list_of_trains={"chennai_express":'12345',"tirupathi_express":'45678',"eastgost":'9876',"venkatadri_express":"45321","janmabumi":'45678'}
print(list_of_trains)
name=input("Enter Your Name:")
age=int(input("Enter Your Age:"))
gender=input("Enter Your Gender:")
train=input("Enter Required Train:")
for k,v in list_of_trains.items():
            print ("trainname",k,"trainnum:",v)
ticketrate={"chennai_express":'240',"tirupasthi_express":'500',"eastgost":'630',"venkatadri_express":"450","janmabumi":'480'}


for t,r in ticketrate.items():
    print("select_train:",t,"ticketrates:",r)
pas=int(input("enter number of passengers:"))
if train in ticketrate:
    print1=(("ticket_rate:",int(ticketrate[train])))
    price=(int(ticketrate[train])*pas) 
    print(price)

    user_date=int(input("enter your reservation date:"))
    date=datetime.datetime(2023,6,user_date)
    print("your reservation date:",date)
    print("your ticket was  reserved:",datetime.datetime.now())
    seat=input("select_seattype:")
    class Train():
        def __init__(self, train_num,select_seat, source, destination, seats,):
            self.train_num = train_num
            self.select_seat=select_seat
            self.source = source
            self.destination = destination
            self.seats = seats
        def display_info(self):
            print("Train number:",self.train_num)
            print("selectseat:",self.select_seat)
            print("Source:",self.source)
            print("Destination:",self.destination)
            print("Available seats:",self.seats)
            print()  # line break for each train information is displayed
    tr=Train("12345","Ac","vjy","hyd",2)
    print(25*"__","WELCOME TO IRCTC",25*"__")
    print("Name:",name)
    print("Age:",age)
    print("Gender:",gender)
    print("Trainname:",train)
    print(50*"  ","PNRNO:",random.randint(11111,1000000))
    print(40*"  ","Reservationdate:",date)
    tr.display_info()
    print(40*"  ","Number Of Passengers:",pas,"TOTALFARE",price)
    print(45*"  ","TOTALFARE:",price)
    print (25*"--" ,"HAPPY_JOURNEY",25*"--")
