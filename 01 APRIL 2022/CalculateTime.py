
def calculate_time_in_second(time):
    if(time.__contains__(":")):
        minute, seconds = time.split(":")
    else:
        minute = time
        seconds = "0"
    return (int(minute) *60)+ int(seconds)

def calculate_time_from_second_minute(time):
    ans_min = int(sum/60)
    ans_sec =  sum % 60
    print(f"{ans_min}:{ans_sec}")

if __name__ == "__main__":
    print('Abu')
    list_time = ["4:30","7:30","10:29","4:46","6:59","4"]
    print(4.3+7.3)
    sum = 0
    for time in list_time:
        sum += calculate_time_in_second(time)
    print(sum)
    calculate_time_from_second_minute(sum)




