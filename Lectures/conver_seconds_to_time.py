'''
NAme: Logan Freerksen 
Date: 02/23/22

Step 1: input numbers of seconds
Step 2: Convert secondsss to minutes and hours
Step 2a: Covert seconds to hours
Stepp 2b: Convert remaining seconds to minutes
Step 3: Print out HH:MM:SS from inputed seconds

'''
def convert_seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours
    

def convert_seconds_to_minutes(seconds):
    minutes = seconds // 60
    return minutes
   

def main():
    seconds = int(input("Please enter the number of seconds \n"))
    hours = convert_seconds_to_hours(seconds)
    minutes = convert_seconds_to_minutes(seconds - (hours*3600))
    print(f'The time format of seconds is: {hours}:{minutes}:{seconds%60}')
    pass
main()

