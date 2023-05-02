from datetime import datetime
from ParkingLot import ParkingLot


# פונקציה שמדפיסה תפריט
def show_selection_menu(menu):
    print("\nYour options:")
    for key in menu:
        print(f"{key}. {menu[key]}")


# פונקציה שלוקחת מספר מהמשתמש ובודקת אם הוא תקין
def take_number_from_user_to_menu(low, high, menu):
    show_selection_menu(menu)
    while True:
        try:
            number = int(input("\nEnter your choice:\n"))
        except ValueError:
            print("\nTry again. please just a number.")
            continue
        else:
            if number < low or number > high:
                print(f"\nThe number should be between {low} and {high}.")
                continue
            return number


# 1. הצגת מחירון חנייה
# 2. הצגת מספר המקומות הפנויים בחניון
# 3. כניסת רכב לחניון
# 4. משך החנייה של רכב מסויים
# 5. עלות החנייה של רכב מסויים
# 6. הוצאת רכב מהחניון
# 7. רשימת כל המכוניות שחונות כרגע בחניון
# 8. רשימת מכוניות שחונות מעל 24 שעות
# 9. תפריט מנהל החניון
# 10. סיום ויציאה מתפריט הבחירה
def user_menu():
    dic_user_menu = {"1": "Presentation of the parking price list",
                     "2": "Displaying the number of available spaces in the parking lot",
                     "3": "Vehicle entry into the parking lot",
                     "4": "The parking duration of a certain vehicle",
                     "5": "The cost of parking a certain vehicle",
                     "6": "Removing a car from the parking lot",
                     "7": "List of all cars currently parked in the parking lot",
                     "8": "List of cars parked for more than 24 hours",
                     "9": "The parking lot manager's menu",
                     "10": "Ending and exiting the selection menu"}
    return dic_user_menu


# 0. חזרה לתפריט הראשי
# 1. שינוי מחיר לשעת חניה
# 2. שינוי מספר המכוניות המקסימלי בחניון
# 3. איפוס החניון
def manager_menu():
    dic_manager_menu = {"0": "Back to the main menu",
                        "1": "Price change per parking hour",
                        "2": "Changing the maximum number of cars in the parking lot",
                        "3": "Resetting the parking lot"}
    return dic_manager_menu


def take_phone_number(user_car):
    phone_number = ""
    while not user_car.is_phone_number_ok(phone_number):
        phone_number = input("Enter your phone number.\nIsrael number like: 000-0000000\n")
    return phone_number


def take_car_number():
    while True:
        try:
            car_number = int(input("Enter car number: "))
        except ValueError:
            continue
        else:
            return car_number


def take_car_type():
    car_type = ""
    types = ["private", "public"]
    while car_type not in types:
        car_type = input("Enter your car typy. choose: private, public\n")
    return car_type


def take_arrival_time():
    return datetime.now()


def some_car(user_car):
    some_car = take_car_number()
    for c in user_car.cars:
        if some_car == c.car_number:
            return c
    return False


def some_number_from_user(is_float=True):
    while True:
        try:
            if is_float:
                number_from_user = float(input("Enter the new price: "))
            else:
                number_from_user = int(input("Enter the new capacity: "))
        except ValueError:
            print("Error. try again.")
            continue
        else:
            if number_from_user > 0:
                return number_from_user
            continue


def total_time(user_car):
    c = some_car(user_car)
    if not c:
        return "The car not exist"
    return f"This car parking {user_car.calculate_time_of_parking(c)} hours"


def total_price(user_car):
    c = some_car(user_car)
    if not c:
        return "The car not exist"
    return f"Parking cost {user_car.calculate_price(c)} $"


def remove_specific_car(user_car):
    c = some_car(user_car)
    if not c:
        return "The car not exist"
    if user_car.remove_car(c):
        return f"The car {c.car_number} left the parking lot.\n" \
               f"Parking cost {user_car.calculate_price(c)} $"


def get_username_and_password_from_user():
    username = input("Enter username > ")
    password = input("Enter password > ")
    return username, password


def main():
    user_car = ParkingLot(25, 100)
    user_choose = ""
    manager_choose = ""
    # user_car.add_car(5236, "private", datetime.now(), "054-965238")
    # user_car.add_car(5235, "public", datetime(2023, 3, 1, 15, 20), "053-968962")

    while user_choose != 10:
        user_choose = take_number_from_user_to_menu(1, 10, user_menu())
        if user_choose == 1:
            print(f"\nThe cost of an hour of parking in the parking lot is {user_car.get_price()} $")
        elif user_choose == 2:
            print(f"\nThere are {user_car.get_capacity() - user_car.amount_of_car_now()} available parking spaces")
        elif user_choose == 3:
            user_car.add_car(take_car_number(), take_car_type(), take_arrival_time(), take_phone_number(user_car))
        elif user_choose == 4:
            print(total_time(user_car))
        elif user_choose == 5:
            print(total_price(user_car))
        elif user_choose == 6:
            print(remove_specific_car(user_car))
        elif user_choose == 7:
            for c in user_car.cars:
                print(c)
        elif user_choose == 8:
            for c in user_car.cars:
                if user_car.calculate_time_of_parking(c) > 24:
                    print(c)
        elif user_choose == 9:
            username, password = get_username_and_password_from_user()
            if user_car.check_admin(username, password):
                while manager_choose != 0:
                    manager_choose = take_number_from_user_to_menu(0, 3, manager_menu())
                    if manager_choose == 0:
                        continue
                    elif manager_choose == 1:
                        print(user_car.set_price(some_number_from_user()))
                    elif manager_choose == 2:
                        print(user_car.set_capacity(some_number_from_user(False)))
                    elif manager_choose == 3:
                        user_car.cars = []
                        print("The parking lot has been reset.")
            else:
                print("There is a mistake in the username or password")
        else:
            print("Good Bye!!")
            break


main()
