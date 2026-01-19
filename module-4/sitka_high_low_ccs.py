import csv
from datetime import datetime

from matplotlib import pyplot as plt
# Changed into function that returns lists
def load_weather_data(filename = 'sitka_weather_2018_simple.csv'):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and high temperatures from this file.
        # Added list for lows
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6]) # Adding low temp value to lows
            lows.append(low)
        return dates, highs, lows
    

# Plot the high temperatures.
# Changed into function that can plot high or low
def plot_temperatures(dates, temps, title, color):
    plt.style.use("seaborn-v0_8") # Incorporated seaborn style with appropriate version
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
# Created main function  
def main():
    print("=======================================")
    print("       Sitka 2018 Weather Viewer       ")
    print("=======================================\n")

    print("Loading weather data...")
    dates, highs, lows = load_weather_data() # Unpack lists from load_weather_data()
    print("Finished loading data.\n")
    print("Welcome to the Sitka 2018 Weather Viewer.")
    print("Please choose which data you would like to view:")
    # Allow user to infinitely loop until they wish to exit
    while True:
        print("\n==MENU==")
        print("1. View High Temperatures (red)")
        print("2. View Low Temperatures (blue)")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip() # Collect and sanitize user input

        if choice == "1":
            plot_temperatures(dates, highs, "Daily High Temperatures - Sitka, 2018", "red") # Display high temps in red
        elif choice == "2":
            plot_temperatures(dates, lows, "Daily Low Temperatures - Sitka, 2018", "blue") # Display low temps in blue
        elif choice == "3":
            print("\nThank you for using the Sitka Weather Viewer!") # Exit loop
            print("Goodbye!")
            break
        else:
            print("Error. Choice must be a number: 1, 2, or 3.") # Catch bad user input







if __name__ == "__main__":
    main()
