import csv
import os

from classes import Person, Driver, Rider
from classes import messages


def main():
    drivers_csv = os.path.expanduser("~/Downloads/" + input("Drivers CSV: ") + ".csv")
    riders_csv = os.path.expanduser("~/Downloads/" + input("Riders CSV: ") + ".csv")

    all_driving = get_driving(drivers_csv, riders_csv)
    for driver in all_driving:
        print("-"  * 20)
        print(get_driver_message(driver))
        for rider in driver.get_riders():
            print("#" * 5)
            print(get_rider_message(rider))
        





def find_rider(name, list):
    for rider in range(len(list)):
        if list[rider].get_first_name().lower() == name.lower():
            return list[rider]
    return None

def get_all_riders(rider_path):
    riders = []
    lines = []
    with open(rider_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            lines.append(line)
    
    for i in range(1, len(lines)):
        if lines[i][2] == "":
            break
        firstname = lines[i][2].split()[0] if len(lines[i][2].split()) > 1 else lines[i][2]
        lastname = lines[i][2].split()[1] if len(lines[i][2].split()) > 1 else ""
        number = lines[i][3]
        email = lines[i][1]
        address = lines[i][4]
        new_rider = Rider(firstname, lastname, number, address)
        riders.append(new_rider)

    return riders

def get_all_drivers(driver_path):
    drivers = []
    lines = []
    with open(driver_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            lines.append(line)
    
    for i in range(1, len(lines)):
        firstname = lines[i][0].split()[0] if len(lines[i][0].split()) > 1 else lines[i][0]
        lastname = lines[i][0].split()[1] if len(lines[i][0].split()) > 1 else ""
        number = lines[i][1]
        new_driver = Driver(firstname, lastname, number)
        drivers.append(new_driver)
    return drivers

def get_driving(driver_path, rider_path):
    drivers = get_all_drivers(driver_path)
    riders = get_all_riders(rider_path)

    driving = []

    lines = []
    with open(rider_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            lines.append(line)

    driver_line = 1
    for i in range(1, len(lines)):
        if lines[i][2] == "":
            break
        driver_line += 1
    
    while (lines[driver_line][0] == ""):
        driver_line += 1
    
    for i in range(len(lines[driver_line])):
        name = lines[driver_line][i]
        notes = ""
        if not name.isalpha():
            notes = name[name.find("("):-1]
            name = name[:name.find("(")].strip()
            
        
        current_driver = None

        for driver in drivers:
            # print(driver.get_first_name())
            if driver.get_first_name().lower() == name.lower():
                current_driver = driver
                break

        if not current_driver:
            num = input("What is " + name + "'s phone number? ")
            current_driver = Driver(name, "", num, [])
        
        j = driver_line + 1
        while j < len(lines):
            if lines[j][i] == "":
                break
            rider_name = lines[j][i]
            rider_notes = ""
            if not rider_name.isalpha():
                rider_notes = rider_name[rider_name.find("("):-1]
                rider_name = rider_name[:rider_name.find("(")].strip()
            
            current_rider = find_rider(rider_name, riders)
            if not current_rider:
                current_rider = Rider(rider_name, "", "", ridernotes="")
            current_rider.set_driver(current_driver)
            current_rider.set_notes(rider_notes)
            j += 1
            current_driver.set_notes(notes)
            current_driver.add_rider(current_rider)
        driving.append(current_driver)
    return driving

def get_driver_message(driver):
    text = f'{messages.get_greeting()} {driver.get_first_name()}, {messages.get_warmth()}. '
    text += f'{messages.get_driver_transition()}:\n'
    for rider in driver.get_riders():
        text += f'\n--{rider.get_first_name()}\n'
        text += f'Phone number: {rider.get_phone_number()}\n'
        text += f'Address: {rider.get_address()}\n'
    text += f'\n{messages.get_closing().capitalize()}. {messages.get_appreciation().capitalize()} and {messages.get_farewell()}.\n'
    return text

def get_rider_message(rider):
    text = f'{messages.get_greeting()} {rider.get_first_name()}, {messages.get_warmth()}. '
    text += f'{messages.get_rider_transition()}. You will be going with {rider.get_driver().get_first_name()}.'
    text += f' Their number is {rider.get_driver().get_phone_number()}.'
    text += f' {messages.get_closing().capitalize()}. {messages.get_appreciation().capitalize()} and {messages.get_farewell()}.\n'
    return text

if __name__ == "__main__":
    main()