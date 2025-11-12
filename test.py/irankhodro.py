import mysql.connector
import random


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="AHMADrEza1604@",  
    database="irankhodro")
cursor = db.cursor()

class Car:  
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        return f"{self.name} , price : {self.price}"


def show_all_cars():
    cursor.execute("SELECT name, price FROM cars")
    result = cursor.fetchall()
    if not result:
        print("There are no cars.")
    else:
        print("\n*** Menu of cars ***")
        a = 1
        for name, price in result:
            print(f"{a}. {name} , price : {price}")
            a += 1


def add_car():
    name = input("Please insert the name: ")
    cursor.execute("SELECT name FROM cars WHERE name = %s", (name,))
    if cursor.fetchone():
        print("The car already exists.")
        return

    price = int(input("Please insert the price: "))
    cursor.execute("INSERT INTO cars (name, price) VALUES (%s, %s)", (name, price))
    db.commit()
    print("New car added.")


def delete_car():
    name = input("Please insert the name for deletion: ")
    cursor.execute("SELECT name FROM cars WHERE name = %s", (name,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM cars WHERE name = %s", (name,))
        db.commit()
        print("The car is deleted.")
    else:
        print("There are no cars with this name.")


def manager_car():
    while True :
        print("\n^^^ Manager Panel ^^^")
        print("1. Show all cars")
        print("2. Add car")
        print("3. Delete car")
        print("4. Exit")

        try:
            m = int(input("Please choose your number: "))
        except:
            print("Invalid choice")     
            continue

        if m == 1:
            show_all_cars()
        elif m == 2:
            add_car()
        elif m == 3:
            delete_car()
        elif m == 4:
            print("Thank you for seeing manager panel")
            break
        else:
            print("Invalid choice") 


def customer_car():
    while True :
        print("\n*** Customer Panel ***")  
        print("1. Show all cars")
        print("2. Exit") 

        try:
            c = int(input("Please choose your number: "))
        except:
            print("Invalid choice")
            continue

        if c == 1:
            show_all_cars()
        elif c == 2:
            print("Thank you for seeing customer panel")
            break
        else:
            print("Invalid choice")  

def Lottery_with_car():
    while True:
        print("\n*** Lottery Panel ***")
        print("1. Add participant")
        print("2. Show participent")
        print("3. Draw winner")
        print("4. Exit")
        try:
            choice = int(input("Choose: "))
        except:
            print("Invalid choice")
            continue

        if choice == 1:
            first_name = input("pl insert the first_name: ")
            last_name = input("pl insert the last_name: ")
            code_meli = input("pl insert the code_meli: ")
            cursor.execute("INSERT INTO lottery (first_name, last_name, national_code) VALUES (%s, %s, %s)", (first_name, last_name, code_meli))
            db.commit()
            print("Participant added!")

        elif choice == 2:
            cursor.execute("SELECT first_name, last_name, national_code FROM lottery")
            participants = cursor.fetchall()
            if not participants:
                print("No participants yet.")
            else:
                i = 1
                for first, last, code in participants:
                    print(f"{i}. {first} {last} - {code}")
                    i += 1
        elif choice == 3:
            cursor.execute("SELECT first_name, last_name, national_code FROM lottery")
            participants = cursor.fetchall()
            if participants:
                winner = random.choice(participants)
                print(f"\n*** Winner ***\n{winner[0]} {winner[1]} - {winner[2]}")
            else:
                print("No participants to draw from.")

        elif choice == 4:
            print("Exiting Lottery Panel.")
            break
        else:
            print("Invalid choice")
            

def menu():
    print("\n^^^ IranKhodro Management ^^^")
    print("1. Show all cars")
    print("2. Add car")
    print("3. Delete car")
    print("4. Manager Panel")
    print("5. Customer Panel")
    print("6. Lottery winners")
    print("7. Exit")


while True:
    menu()
    try:
        b = int(input("Please choose your number: "))
    except:
        print("Invalid choice")
        continue

    if b == 1:
        show_all_cars()
    elif b == 2:
        add_car()
    elif b == 3:
        delete_car()
    elif b == 4:
        manager_car()
    elif b == 5:
        customer_car()  
    elif b == 6:
        Lottery_with_car()
    elif b == 7:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
