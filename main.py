#Function that converites intergear value called minutes
def time_converter(minutes):
    time = []
    num_hours = minutes // 60
    minutes  = minutes - ( num_hours * 60)
    num_mins = minutes
    time.append(num_hours) #number of hours from number of minutes
    time.append(num_mins) #number of remaining minutes
    #print(time[0],time[1])
    return(time)
    
#takes in str and returns it as a list of ints
def get_flight_times(flight):
    flight_nums = flight.split()
    for i in range(len(flight_nums)):
        flight_nums[i] = int(flight_nums[i]) #Converts the strs into ints in the list
    #Turns the hours into minutes
    flight_nums[0] *= 60
    flight_nums[2] *= 60
    #computes the departure and arrival time in minutes
    flight_time = []
    flight_time.append(flight_nums[0] + flight_nums[1])#departure
    flight_time.append(flight_nums[2] + flight_nums[3])#arrival
    return flight_time

#take in a start and end time(both ints), the minutes that overlapsed since the start of the day and computes the elspesed time of the leg(flight or layover)
#Either both times are in the same day or they are not, this determined start <= end == sameday or start > end = different day
def get_leg_time(end_time,start_time):
    if start_time <= end_time:
        return end_time - start_time
    #day boundray crossed
    else:
        return (1440 - start_time) + (end_time)
    
def get_layover_and_total_time(flight1,flight2):
    time_list = []
    #Subtracting departure time of flight 2 from arrival time of flight 1
    #if:
    time_list.append (get_leg_time(flight2[0],flight1[1]))# Layover time
    #computes total time, total time is computed as flight 1 time + flight 2 time plus layover time
    time_list.append((get_leg_time(flight1[1],flight1[0])) + (get_leg_time(flight2[1],flight2[0])) + time_list[0]) #total time
    #checks if total time goes overninght and if so adds on a day of time
    
    return(time_list)


#Gets the inputs for the flights 
flight_1 = (input("Flight 1: "))
flight_2 = (input("Flight 2: "))
flight_1_time = get_flight_times(flight_1)
flight_2_time = get_flight_times(flight_2)
times = get_layover_and_total_time(flight_1_time,flight_2_time)
#Function call for laytime
ltime = time_converter(times[0])
#Function call for total time
tTime = time_converter(times[1])
#prints the results of the program.
print("Layover:",ltime[0],"hr",ltime[1],"min\nTotal:",tTime[0],"hr",tTime[1],"min")
