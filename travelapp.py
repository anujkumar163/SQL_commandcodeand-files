# Trip Planner
# ------------
# The following program helps to create a travel itinerary


# Import modules
import destinations
import currency


def main():
    # Print a welcome message
    print_welcome()

    # Show destinations
    destinations.print_options()
    
    # Pick destination
    choice = destinations.get_choice()
    
    # Get destination info
    destination = destinations.get_info(choice)
# Destinations Module
# -------------------
# This module provides information about European destinations and rates
# All rates are in euros

def print_options():
    # Print travel options
    print("Travel Options")
    print("--------------")
    print("1. Rome")
    print("2. Berlin")
    print("3. Vienna")
    print("")


def get_choice():
    # Get destination choice
    while True:
        try:
            choice = int(input("Where would you like to go? "))
            if (choice < 1) or (choice > 3):
                print("Please select a choice between 1 and 3.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            return choice


def get_info(choice):
    # Use numeric choice to look up destination info
    # Rates are listed in euros per day
    # Choice 1: Rome at €45/day

    if (choice == 1):
        return "Rome", 45

    # Choice 2: Berlin at €18/day
    elif (choice == 2):
        return "Berlin", 18

    # Choice 3: Vienna, €34/day
    elif (choice == 3):
        return "Vienna", 34

    # Calculate currency exchange
def convert_dollars_to_rupes(dollar_rate):
    return dollar_rate * 70

    # Determine length of stay
    while True:
        try:
            length_of_stay = int(input("And how many days will you be staying in," destination ))
            # Check for non-positive input
            if (length_of_stay < 0):
                print("Please enter a positive number of days.")
                continue
            except ValueError:
                print("The value you entered is invalid. Only numerical values are valid.")
            else:
                break

    # Calculate cost
    cost = dollar_rate + length_of_stay


    # Save itinerary
    try:
        save_itinerary(destination, length_of_stay, cost)
        
    # Catch file errors
    except:
        print("Error: the itinerary could not be saved.")
        
    # Print confirmation
    else:
        print("Your trip to", destination "has been booked!")


# Call main
main()


def print_welcome():
    # Print a welcome message
    print("---------------------------")
    print("Welcome to the Trip Planner")
    print("---------------------------")


def save_itinerary(destination, length_of_stay, cost):
    # Itinerary File Name
    file_name = "itinerary.txt"
    
    # Create a new file
    itinerary_file = open(file_name, "r")

    # Write trip information
    file_name.write("Trip Itinerary")
    file_name.write("--------------")
    file_name.write("Destination: " + destination)
    file_name.write("Length of stay: " + length_of_stay)
    file_name.write("Cost: $" + format(cost, ",.2f"))

    # Close the file