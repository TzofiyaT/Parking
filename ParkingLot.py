from datetime import datetime


class Car:
    def __init__(self, car_number, car_type, arrival_time, phone_number):
        self.car_number = car_number
        self.car_type = car_type
        self.arrival_time = arrival_time
        self.phone_number = phone_number

    def __str__(self):
        return f"Car number {self.car_number} belongs to {self.phone_number}. arrived at {self.arrival_time}"


class ParkingLot:
    def __init__(self, price, capacity):
        self.cars = []
        self.__price = price
        self.__capacity = capacity
        self.admin_username = 'Admin'
        self.admin_password = 'Admin'

    #מחזירה את המחיר לשעת חניה
    def get_price(self):
        return self.__price

    #משנה את המחיר לשעת חניה
    def set_price(self, new_price):
        # price must be greater than 0. must be a float!
        try:
            new_price = float(new_price)
        except ValueError:
            return self.__price
        else:
            if new_price > 0:
                self.__price = new_price
                return self.__price
        return new_price

    #מחזירה את כמות החניות
    def get_capacity(self):
        return self.__capacity

    # משנה את כמות החניות
    def set_capacity(self, new_capacity):
        # must be an integer! must be greater or equal to amount of currently parked cars
        if "." in str(new_capacity):
            return self.__capacity
        try:
            new_capacity = int(new_capacity)
        except ValueError:
            return self.__capacity
        else:
            amount_of_car = self.amount_of_car_now()
            if new_capacity >= amount_of_car:
                self.__capacity = new_capacity
                return new_capacity
        return self.__capacity

    #מוסיפה רכב לרשימת החניון
    def add_car(self, number_of_car, car_type, arrival_time, phone_number):
        if not self.is_car_in_parking_lot(number_of_car):
            if self.is_parking_available():
                new_car = Car(number_of_car, car_type, arrival_time, phone_number)
                self.cars.append(new_car)
            return True
        return False

    #מסירה רכב מרשימת החניון
    def remove_car(self, car_to_remove):
        index = 0
        for car in self.cars:
            if car_to_remove.car_number == car.car_number:
                self.cars.pop(index)
            index += 1
        return True

    #מחשבת את עלות החניה הכוללת
    def calculate_price(self, some_car):
        hours = self.calculate_time_of_parking(some_car)
        return hours * self.__price

    #מחשבת את זמן החניה הכולל
    def calculate_time_of_parking(self, some_car):
        then = some_car.arrival_time
        today = datetime.now()
        diff = today - then
        day = diff.days
        second = diff.seconds
        hours = (second/60)/60 + day*24
        return hours

    #מאשרת כניסת מנהל לפי שם משתמש וסיסמא
    def check_admin(self, username, password):
        return username == self.admin_username and password == self.admin_password

    #בודקת לפי מספר רכב אם רכב מסויים נמצא בחניון
    def is_car_in_parking_lot(self, number_of_car):
        for car in self.cars:
            if car.car_number == number_of_car:
                return True
        return False

    #האם יש מקומות פנויים בחניון
    def is_parking_available(self):
        if self.__capacity > self.amount_of_car_now():
            return True
        return False

    # בודקת אם מספר הטלפון תקין
    def is_phone_number_ok(self, number_of_phone):
        if len(number_of_phone) != 11:
            return False
        first = number_of_phone[0:3]
        middle = number_of_phone[3:4]
        last = number_of_phone[4:]
        first_number = ["050", "052", "053", "054", "055", "056", "057", "058", "059"]
        if first in first_number:
            if middle == "-":
                try:
                    last = int(last)
                except ValueError:
                    return False
                else:
                    return True
        return False

    #מספר המכוניות הנוכחי בחניון
    def amount_of_car_now(self):
        return len(self.cars)

    #איפוס החניון
    def restart_to_parking(self):
        self.cars.clear()


# list_of_cars = ParkingLot(15, 30)
# print(list_of_cars.set_capacity(-8))
# list_of_cars.add_car("5236", "pr", datetime.now(), "054-965238")
# list_of_cars.add_car("5236", "pu", datetime(2023, 3, 1, 15, 20), "053-968962")
# for c in list_of_cars.cars:
#     print(c)
#     print(list_of_cars.calculate_price(c))
#
# print(list_of_cars.is_car_in_parking_lot(5286))
# print(list_of_cars.is_car_in_parking_lot(5236))
#
# print(list_of_cars.restart_to_parking())
# print(list_of_cars.is_phone_number_ok("053-968962"))
# for c in list_of_cars.cars:
#     print(c)
