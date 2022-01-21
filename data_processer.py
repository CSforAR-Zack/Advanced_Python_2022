import csv
import sqlite3

def main():
    file_content = get_data_csv("weather_lr.csv")

    db = database()


class database:
    def __init__(self):
        self.connection = sqlite3.connect("workshops.db")
        self.c = self.connection.cursor()


def get_data_csv(file):
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
    
        return list(reader)
        

if __name__ == "__main__":
    main()