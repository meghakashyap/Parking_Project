import os,random,json
from datetime import date
from pprint import pprint

veh_list=["","Car","Bike","Truck","Bus"]
name_ = input("Please Enter your Name :-")
print(" ")
print("Welcome",name_,"to Divine Parking Slot")
print(" ")
parking_opt = int(input("Enter the option which you like to choose: \n1.Park your vehicle\n2.Collect your vehichle\n=>"))
print("       ")
motor_cycleSpot = 5
large_spot = 5
compact_spot = 5

large,compact,motor=0,0,0

if os.path.exists("parking_details.json"):
    vehicle_file = open("parking_details.json","r")
    details = json.load(vehicle_file)
    for i in details:
        for x in details[i]:
            if x["Slot"]=="Large_spot":
                large+=1
            if x["Slot"]=="Compact_spot":
                compact+=1
            if x["Slot"]=="Motor_bike":
                motor+=1
else:
    pass

s_m=motor_cycleSpot-motor
s_c=compact_spot-compact
s_l=large_spot-large

list=[]
dict1={"user":list}
dic={}

if parking_opt == 1:
    
    vehicle = int(input("Enter the number which vehicle you want to park like(1.car,2.bike,3.Truck,4.Bus  :="))
    no_of_vehicle = int(input("Enter how many vehicle you want to park="))
    
    if vehicle == 2 :
        space=motor_cycleSpot-motor
        if s_m >=  no_of_vehicle:
            print(space,"left for motor_Bike,")
            i=0
            while i< no_of_vehicle:
                bike_amt=50
                name = input("Enter which vehicle you want to park like(car,bike,scooty etc..) =")
                vehicle_num = input("Enter you vehicle number = ")
                hour = int(input("Enter the parking duration :-"))
                date = date.today()
                amount =bike_amt*hour
                for b in name_:
                    token_no=ord(b)
                print("         ")
                print(token_no,"Please Don't Forget your Token")
                print(amount,"You have to pay !!")
                dic["Name"]=name_
                dic["Vehicle"] = name
                dic["num_of_vehicle"] = no_of_vehicle        
                dic["Vehicle_Number"] = vehicle_num
                dic["Duration"] = hour
                dic["Date"] = str(date)
                dic["Amount"] = amount
                dic["Token"]=token_no
                dic["Slot"]="Motor_bike"
                if os.path.exists("parking_details.json"):
                    with open("parking_details.json") as file:
                        k=json.load(file)
                        l=k["user"]
                        l.append(dic)
                        dict1["user"]=l
                        with open("parking_details.json","w") as file1:
                            json.dump(dict1,file1,indent=4)
                else:
                    list.append(dic)
                    with open("parking_details.json","w") as file:
                        json.dump(dict1,file,indent=4)
                    
                i+=1
                
        elif s_c >= no_of_vehicle:
            print(s_c,"Space left in Compact Slot ")
            i=0
            while i< no_of_vehicle:
                bike_amt=70
                name = input("Enter which vehicle you want to park like(car,bike,scooty etc..) =")
                vehicle_num = input("Enter you vehicle number = ")
                hour = int(input("Enter the parking duration :-"))
                date = date.today()
                amount =bike_amt*hour
                for b in name_:
                    token_no=ord(b)
                print("          ")
                print(token_no,"Please Don't Forget your Token")
                print(amount,"You have to pay !!")
                dic["Name"]=name_
                dic["Vehicle"] = name
                dic["num_of_vehicle"] = no_of_vehicle        
                dic["Vehicle_Number"] = vehicle_num
                dic["Duration"] = hour
                dic["Date"] = str(date)
                dic["Amount"] = amount
                dic["Token"]=token_no
                dic["Slot"]="Compact_spot"
                if os.path.exists("parking_details.json"):
                    with open("parking_details.json") as file:
                        k=json.load(file)
                        l=k["user"]
                        l.append(dic)
                        dict1["user"]=l
                        with open("parking_details.json","w") as file1:
                            json.dump(dict1,file1,indent=4)
                else:
                    list.append(dic)
                    with open("parking_details.json","w") as file:
                        json.dump(dict1,file,indent=4)
                    
                i+=1
        elif s_l >= no_of_vehicle:
            print(s_l,"Space left in Large Slot ")
            i=0
            while i< no_of_vehicle:
                bike_amt=70
                name = input("Enter which vehicle you want to park like(car,bike,scooty etc..) =")
                vehicle_num = input("Enter you vehicle number = ")
                hour = int(input("Enter the parking duration :-"))
                date = date.today()
                amount =bike_amt*hour
                for b in name_:
                    token_no=ord(b)
                print("        ")
                print(token_no,"Please Don't Forget your Token")
                print(amount,"You have to pay !!")
                dic["Name"]=name_
                dic["Vehicle"] = name
                dic["num_of_vehicle"] = no_of_vehicle        
                dic["Vehicle_Number"] = vehicle_num
                dic["Duration"] = hour
                dic["Date"] = str(date)
                dic["Amount"] = amount
                dic["Token"]=token_no
                dic["Slot"]="Large_spot"
                if os.path.exists("parking_details.json"):
                    with open("parking_details.json") as file:
                        k=json.load(file)
                        l=k["user"]
                        l.append(dic)
                        dict1["user"]=l
                        with open("parking_details.json","w") as file1:
                            json.dump(dict1,file1,indent=4)
                else:
                    list.append(dic)
                    with open("parking_details.json","w") as file:
                        json.dump(dict1,file,indent=4)
                    
                i+=1
        else:
            print("THERE IS NO SPACE FOR BIKE SORRY :(")
            
                
    elif vehicle == 1:
        if s_c >=  no_of_vehicle:
            print(s_c,"place left in Compact space for car")
            i=0
            while i< no_of_vehicle:
                car_amt=70
                name = input("Enter which vehicle you want to park like(car,bike,scooty etc..) =")
                vehicle_num = input("Enter you vehicle number = ")
                hour = int(input("Enter the parking duration :-"))
                date = date.today()
                amount =car_amt*hour
                for b in name_:
                    token_no=ord(b)
                print("         ")
                print(token_no,"Please Don't Forget your Token")
                print(amount,"You have to pay !!")
                dic["Name"]=name_
                dic["Vehicle"] = name
                dic["num_of_vehicle"] = no_of_vehicle        
                dic["Vehicle_Number"] = vehicle_num
                dic["Duration"] = hour
                dic["Date"] = str(date)
                dic["Amount"] = amount
                dic["Token"]=token_no
                dic["Slot"]="Compact_spot"
                if os.path.exists("parking_details.json"):
                    with open("parking_details.json") as file:
                        k=json.load(file)
                        l=k["user"]
                        l.append(dic)
                        dict1["user"]=l
                        with open("parking_details.json","w") as file1:
                            json.dump(dict1,file1,indent=4)
                else:
                    list.append(dic)
                    with open("parking_details.json","w") as file:
                        json.dump(dict1,file,indent=4)
                    
                i+=1
                
        elif s_l>= no_of_vehicle:
            print(s_l,"Space left in Large Spot ")
            if vehicle==1:
                i=0
                while i< no_of_vehicle:
                    car_amt=70
                    name = input("Enter which vehicle you want to park like(car,bike,scooty etc..) =")
                    vehicle_num = input("Enter you vehicle number = ")
                    hour = int(input("Enter the parking duration :-"))
                    date = date.today()
                    amount =car_amt*hour
                    for b in name:
                        token_no=ord(b)
                    print("      ")
                    print(token_no,"Please Don't Forget your Token")
                    print(amount,"You have to pay !!")
                    dic["Name"]=name_
                    dic["Vehicle"] = name
                    dic["num_of_vehicle"] = no_of_vehicle        
                    dic["Vehicle_Number"] = vehicle_num
                    dic["Duration"] = hour
                    dic["Date"] = str(date)
                    dic["Amount"] = amount
                    dic["Token"]=token_no
                    dic["Slot"]="Large_spot"
                    if os.path.exists("parking_details.json"):
                        with open("parking_details.json") as file:
                            k=json.load(file)
                            l=k["user"]
                            l.append(dic)
                            dict1["user"]=l
                            with open("parking_details.json","w") as file1:
                                json.dump(dict1,file1,indent=4)
                    else:
                        list.append(dic)
                        with open("parking_details.json","w") as file:
                            json.dump(dict1,file,indent=4)
                        
                    i+=1
        else:
            print("THERE IS NO SPACE EMPTY FOR CAR")
            
                
    elif  vehicle ==3 or 4:
        if s_l >=  no_of_vehicle:
            print(s_l,"Space left in Large Spot ")
            if vehicle==4:
                i=0
                while i< no_of_vehicle:
                    bus_amt=70
                    name = input("Enter which vehicle you want to park like(car,bike,scooty etc..) =")
                    vehicle_num = input("Enter you vehicle number = ")
                    hour = int(input("Enter the parking duration :-"))
                    date = date.today()
                    amount =bus_amt*hour
                    for b in name_:
                        token_no=ord(b)
                    print("     ")
                    print(token_no,"Please Don't Forget your Token")
                    print(amount,"You have to pay !!")
                    dic["Name"]=name_
                    dic["Vehicle"] = name
                    dic["num_of_vehicle"] = no_of_vehicle        
                    dic["Vehicle_Number"] = vehicle_num
                    dic["Duration"] = hour
                    dic["Date"] = str(date)
                    dic["Amount"] = amount
                    dic["Token"]=token_no
                    dic["Slot"]="Large_spot"
                    if os.path.exists("parking_details.json"):
                        with open("parking_details.json") as file:
                            k=json.load(file)
                            l=k["user"]
                            l.append(dic)
                            dict1["user"]=l
                            with open("parking_details.json","w") as file1:
                                json.dump(dict1,file1,indent=4)
                    else:
                        list.append(dic)
                        with open("parking_details.json","w") as file:
                            json.dump(dict1,file,indent=4)
                        
                    i+=1

                    
            elif vehicle==3 :
                print(s_l,"Space left in Large Spot ")
                i=0
                while i< no_of_vehicle:
                    truck_amt=70
                    name = input("Enter which vehicle you want to park like(car,bike,scooty etc..) =")
                    vehicle_num = input("Enter you vehicle number = ")
                    hour = int(input("Enter the parking duration :-"))
                    date = date.today()
                    amount =truck_amt*hour
                    for b in name:
                        token_no=ord(b)
                    print("         ")
                    print(token_no,"Please Don't Forget your Token ")
                    print(amount,"You have to pay !!")
                    dic["Name"]=name_
                    dic["Vehicle"] = name
                    dic["num_of_vehicle"] = no_of_vehicle        
                    dic["Vehicle_Number"] = vehicle_num
                    dic["Duration"] = hour
                    dic["Date"] = str(date)
                    dic["Amount"] = amount
                    dic["Token"]=token_no
                    dic["Slot"]="Large_spot"
                    if os.path.exists("parking_details.json"):
                        with open("parking_details.json") as file:
                            k=json.load(file)
                            l=k["user"]
                            l.append(dic)
                            dict1["user"]=l
                            with open("parking_details.json","w") as file1:
                                json.dump(dict1,file1,indent=4)
                    else:
                        list.append(dic)
                        with open("parking_details.json","w") as file:
                            json.dump(dict1,file,indent=4)
                        
                    i+=1
            else:
                if vehichle==3:
                    print("THERE IS N0 SPACE LEFT FOR TRUCK SORRY:(")
                elif vehichle==3:
                    print("THERE IS N0 SPACE LEFT FOR BUS SORRY:(")
        
            
elif  parking_opt == 2:
    extra=20
    token=int(input("Enter your token number :-"))
    time=int(input("Enter your Parking duration time :-" ))
    
    if os.path.exists("parking_details.json"):
        vehicle_file = open("parking_details.json","r")
    details = json.load(vehicle_file)
    for i in details:
        for x in details[i]:
            if x["Token"]== token:
                if x["Duration"]==time:
                    print("\n You vehicle slip\n")
                    pprint(x)
                    print("")
                    print("ThankYou, Please visit again :)")
                    break
                elif x["Duration"]!=time :
                    charge=time-x["Duration"]
                    print("")
                    print("You Are Late you have to give extra charge RS.",charge*extra)
                    break           
        else :
            print("INVALID TOKEN NO")
    else:
        pass
    
else:
    print("Sorry Try Again :(")     
            

    
        
        
    