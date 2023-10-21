flight_1 = (input("Flight 1: "))
flight_2 = (input("Flight 2: "))
flight_1nums = flight_1.split()
flight_2nums = flight_2.split()
#print(flight_1nums)
#print(flight_2nums)

for i in range(len(flight_1nums)):
    flight_1nums[i] = int(flight_1nums[i])
for i in range(len(flight_2nums)):
    flight_2nums[i] = int(flight_2nums[i])
#print(flight_1nums)
#print(flight_2nums)

flight_1nums[0] *= 60
flight_1nums[2] *= 60
flight_2nums[0] *= 60
flight_2nums[2] *= 60
#print(flight_1nums)
#print(flight_2nums) 

depart1mt = flight_1nums[0] + flight_1nums[1]
#print(depart1mt)
arrive1mt = flight_1nums[2] + flight_1nums[3]
#print(arrive1mt)
depart2mt = flight_2nums[0] + flight_2nums[1]
#print(depart2mt)
arrive2mt = flight_2nums[2] + flight_2nums[3]
#print(arrive2mt)

Laytime = abs(depart2mt - arrive1mt)
#print(depart2mt)
#print(arrive1mt)
#print(depart2mt - arrive1mt)
#print(Laytime)
Total_time = abs(depart1mt - arrive1mt) + abs(depart2mt - arrive2mt) + Laytime
#print(Total_time)
#print(abs(depart1mt - arrive1mt))
def Layover(Laytime):
    time = []
    num_hours = Laytime // 60
    Laytime = Laytime - (num_hours * 60)
    num_minutes = Laytime
    time.append(num_hours)
    time.append(num_minutes)
    #print(time[0],time[1])
    return(time)

def Total(Total_time):
    tTime = []
    num_hours = Total_time // 60
    Total_time = Total_time - ( num_hours * 60)
    num_mins = Total_time
    tTime.append(num_hours)
    tTime.append(num_mins)
    #print(tTime[0],tTime[1])
    return(tTime)

time = Layover(Laytime)
tTime = Total(Total_time)
print("Layover:",time[0],"hr",time[1],"min\nTotal:",tTime[0],"hr",tTime[1],"min")


