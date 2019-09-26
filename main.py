 # Task6
import os
import library.statistics
import library.humidity
import library.tvoc
import library.co2
import statistics
class Instrument:
    data = [] #since data is initialized as a list no need for constructor
    def add_datum(self,id,value,time):
        datum = TimeSeriesData(id,value,time)
        self.data.append(datum)

    def get_values_by_id(self,id):
        values = [] #append values by id
        for datum in self.data:
            if datum.id == id:
                values.append(datum.value)
        return values

    def get_mean_by_id(self,id):
        values = self.get_values_by_id(id)
        mean = statistics.mean(get_values)
        return mean

    def get_median_by_id(self,id):
        values = self.get_values_by_id(id)
        median = statistics.median(values)
        return median
    def get_value_by_id(self, id):
        self.id = id
        max_value = max()

        min_value = min()


def get_command_input():
    print(" ---------------------------------------------")
    print("|Indoor Air Quality Monitoring Command Console|\n ---------------------------------------------\n")
    print("Please select from the following options: \n")
    print("1. Add reading")
    print("2. List readings")
    print("3. Calculate")
    print("4. Exit\n")

    command = input("Please enter your choice : ")
    os.system("clear")
    return command

def get_readings():

    print("Please enter the data \n ")
    temperature = input("Temperature (degrees): ")
    humidity = input("Humidity (%): ")
    pressure = input("Pressure (kPa): ")
    altitude = input("Altitude (ft): ")
    tvoc = input("TVOC (ppb): ")
    co2 = input("CO2 (ppm): ")
    readings = {"temperature": temperature,"humidity": humidity}
    os.system("clear")

    print("* * * * * * * * * * * * * *")
    print("Successfully saved reading")
    print("* * * * * * * * * * * * * *")
    print("\nHit enter key to return to the menu")
    input()

    os.system("clear")
    return readings

tool = Instrument()


def main():
    # This variable controls the main runtime loop
    # of our application. If this variable is `False`
    # then our application should terminal.
    main_loop_is_running = True

    readings = []

    while main_loop_is_running:
        temperature = []
        humidity = []
        pressure = []
        altitude = []
        tvoc = []
        co2 = []
        time = []
        command = get_command_input()

        if command == "1":
            data_reading = get_readings()
            readings.append(data_reading)


        elif command == "2":
            os.system("clear")
            print("TODO: List readings GUI page")
            tool.print_list()
            print("\n\n\n\n\n\n\n\n\n")










            exist = input("Please enter X to exist the list : ")
            if exist == "x" or exist == "X":
                os.system("clear")












        elif command == "3":
            pass



        elif command == "4":
            main_loop_is_running = False
            print("Exit Successfully! ")



if __name__ == "__main__":
    main()
