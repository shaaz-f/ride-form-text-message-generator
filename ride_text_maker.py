import csv
import os
import random

## Can probably remake as OOP

GREETING = ["Hi", "Hey", "Ya Ali Madad"]
WARMTH = ["hope you're doing well.", 
        "hope you're having a good day.",
        "hope you're having a good week.",
        "hope you're staying warm.",
        "hope you're doing okay."]
TRANSITION_RIDES = ["I just wanted to reach out to you about rides for the upcoming rotation",
                    "I just wanted to let you know who you're giving rides to this rotation"]
CLOSING = ["Thank you",
            "Thanks",
            "Thank you so much",
            "Thanks so much",
            "Thanks for your help"]
ASK_FOR_HELP = ["If you have any questions, please let me know.",
                "If you have any questions, please reach out.",
                "Let me know if there are any concerns."]



def find_rider(name, list):
    for rider in list:
        if list[rider]["First name"].lower() == name.lower():
            return list[rider]
    return None


def main():
    drivers = {}
    need_rides = {}

    file_name = input("File name: ")
    file_lines = []
    with open(os.path.expanduser("~/Downloads/" + file_name + ".csv"), "r") as csv_file:
        reader = csv.reader(csv_file)
        ## Put all the lines in a list
        for row in reader:
            file_lines.append(row)
    
    ## Organize the data into dictionaries
    driver_row = 1
    for row in file_lines:
        ## Skip the first row, break at end
        if row[0] == "Timestamp":
            continue
        elif row[2] == "":
            break
        
        current = {
            "First name": row[2].split()[0] if len(row[2].split()) > 1 else row[2],
            "Last name": " ".join(row[2].split()[1:]) if len(row[2].split()) > 1 else "",
            "Phone number": row[3],
            "Email": row[1],
            "Address": row[4]
        }
        need_rides[row[2]] = current
        driver_row += 1

    ## Find ride givers
    for i in range(driver_row+1, len(file_lines)):
        if file_lines[i][0] != "":
            driver_row = i
            break
    
    ## Find who they giving ride to
    for i in range(len(file_lines[driver_row])):
        with_driver = []
        j = driver_row + 1
        while j < len(file_lines):
            if file_lines[j][i] == "":
                break
            with_driver.append(file_lines[j][i])
            j += 1

        current_name = file_lines[driver_row][i]
        if not current_name.isalpha():
            current_name = current_name[:current_name.find("(")].strip()
        
        current_number = ""##input("Phone number for " + current_name + ": ")

        drivers[current_name] = {"Name": current_name,
                                "Phone number": current_number,
                                "Riders": with_driver}

    ## Making the driver text
    for driver in drivers:
        text = random.choice(GREETING) + " " + drivers[driver]["Name"] + ", "
        text += random.choice(WARMTH) + " " + random.choice(TRANSITION_RIDES) + ":\n\n"
        for rider in drivers[driver]["Riders"]:
            current_rider = find_rider(rider, need_rides)
            if current_rider:
                text += current_rider["First name"] + " " + current_rider["Last name"] + "\n"
                text += "Phone number: " + current_rider["Phone number"] + "\n"
                text += "Address: " + current_rider["Address"] + "\n\n"
            else:
                text += rider + "\n\n"
        
        print(text)


main()