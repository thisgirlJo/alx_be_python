from datetime import datetime
def display_current_datetime(current_date):
    current_date = datetime.now()
    print(f"%Y-%m-%d %H:%M:%S")
    return

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(future_date):
    future_date = display_current_datetime() + timedelta(number_of_days)
    print(future_date.striftime)
    return
