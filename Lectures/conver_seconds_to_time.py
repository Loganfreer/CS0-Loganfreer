'''
NAme: Logan Freerksen 
Date: 02/23/22

Step 1: input numbers of seconds
Step 2: Convert secondsss to minutes and hours
Step 2a: Covert seconds to hours
Stepp 2b: Convert remaining seconds to minutes
Step 3: Print out HH:MM:SS from inputed seconds

'''

   
def convert_seconds_time(seconds):
    hours = seconds // 3600    
    minutes = (seconds - (hours * 3600)) // 60
    rem_seconds = seconds % 60
    return hours, minutes, rem_seconds


def main():
    seconds = int(input("Please enter the number of seconds \n"))
    hours, minutes, rem_seconds = convert_seconds_time(seconds)
    print(f'The time format of seconds is: {hours}:{minutes}:{rem_seconds}')
    pass
main()

