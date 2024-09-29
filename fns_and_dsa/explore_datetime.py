from datetime import datetime
def display_current_datetime(current_date):
    current_date = datetime.now()
    print(f"%Y-%m-%d %H:%M:%S")
    return

number_of_days = int(input("Enter a number of days: "))

def calculate_future_date(future_date):
    future_date = display_current_datetime() + timedelta(number_of_days)
    print(f"%Y-%m-%d %H:%M:%S")
    return
