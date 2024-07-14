import random
import time

def printInformation(location):
    print("Location " + location + " is Dirty.")
    print("Cost for CLEANING " + location + ": 1")
    print("Location " + location + " has been Cleaned.")

def vacuumCleaner(goalState, currentState, location, battery, cleaningBin):
    print("Goal State Required:", goalState)
    print("Vacuum is placed in Location " + location)

    totalCost = 0

    while currentState != goalState:
        if battery <= 10:
            print("Battery is low. Charging for 10 seconds...")
            time.sleep(10)
            battery = 100
            print("Battery charged to 100%")

        if cleaningBin >= 90:
            print("Cleaning bin is full. Self-cleaning for 10 seconds...")
            time.sleep(10)
            cleaningBin = 0
            print("Cleaning complete. Cleaning bin is empty.")

        print("Current State:", currentState)

        if location == "A":
            if currentState["A"] == 1:
                currentState["A"] = 0
                totalCost += 1
                cleaningBin += 1
                printInformation("A")
                battery -= 1
            if currentState["B"] == 1:
                print("Moving right to the location B.\nCost for moving RIGHT: 1")
                location = "B"
                totalCost += 1
                battery -= 1
        elif location == "B":
            if currentState["B"] == 1:
                currentState["B"] = 0
                totalCost += 1
                cleaningBin += 1
                printInformation("B")
                battery -= 1
            if currentState["A"] == 1:
                print("Moving left to the location A.\nCost for moving LEFT: 1")
                location = "A"
                totalCost += 1
                battery -= 1



    print("GOAL STATE:", currentState)
    return totalCost, battery, cleaningBin

battery = 100
cleaningBin = 0

while True:
    goalState = {"A": 0, "B": 0}
    currentState = {"A": random.choice([0, 1]), "B": random.choice([0, 1])}
    location = random.choice(["A", "B"])

    totalCost, battery, cleaningBin = vacuumCleaner(goalState, currentState, location, battery, cleaningBin)

    print("Performance Measurement:", totalCost)
    print("Battery: %", battery)
    print("Cleaning Bin Capacity: %", cleaningBin)
    print("*********************************************************")
    time.sleep(10)
