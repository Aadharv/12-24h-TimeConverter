time="07:21:59 PM"

def Clock(time):
    if (time[0:2]=="12" and time[-2:]=="AM"):
        return "00"+time[2:]
    elif (time[0:2]=="12" and time[-2:]=="PM"):
        return time[0:8]
    elif (time[-2:]=="PM"):
        return str(int(time[0:2])+12)+time[2:8]
    elif (time[-2:]=="AM"):
        return time[0:8]
print(Clock(time))
