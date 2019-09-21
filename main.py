 # Task6
import os
from library.temperature import c_to_f

def get_command_input():
    print("Indoor Air Quality Monitoring Command Console\n")
    print("Please select from the following options:")
    print("1. Add reading")
    print("2. List readings")
    print("3. Calculate")
    print("4. Exit\n")
    command = input("Input: ")
    os.system("clear")
    return command

def get_readings():
    print("Please input")
    temperature = input("Temperature (degrees): ")
    humidity = input("Humidity (%): ")
    readings = {"temperature": temperature,"humidity": humidity}
    os.system("clear")

    print("* * * * * * * * * * * * * *")
    print("Successfully saved reading")
    print("* * * * * * * * * * * * * *")
    print("\nHit enter key to return to the menu")
    input()

    os.system("clear")
    return readings

def main():
    # This variable controls the main runtime loop
    # of our application. If this variable is `False`
    # then our application should terminal.
    main_loop_is_running = True

    readings = []

    while main_loop_is_running:

        command = get_command_input()

        if command == "1":
            data_reading = get_readings()
            readings.append(data_reading)
        elif command == "2":
            print("TODO: List readings GUI page")
        elif command == "3":
            print("TODO: Calculate")
        elif command == "4":
            main_loop_is_running = False

if __name__ == "__main__":
    main()
