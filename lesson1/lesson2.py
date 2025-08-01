import csv

#1 Reading a Text File (Line by Line)
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip()) # .strip() removes newline

# with open(...) ensures the file is safely closed after use — best practice!


#2 Writing to a text file
lines = ["Hello", "World", "This is a test"]

with open("output.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")


#3. Read a csv file with csv Module
# import csv
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row) # each row is a list of strings


#4. Writing to csv file
# import csv
data =[["name", "age"],["Alice", 30], ["Bob", 25]]

with open("people.csv", "w", newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(data)


#5. Reading JSON Files
import json

with open("config.json", "r") as f:
    config = json.load(f)

print(config["db"]) #Access value like a dictionary


#6. Writing JSON Files
# import json
data = {"name": "Alice", "role": "engineer"}

with open("output.json", "w") as f:
    json.dump(data, f, indent=2)


# Real world USE-CASE
with open("raw_data.csv", "r") as f:
    for line in f:
        if "ERROR" in line:
            print("found a bad row", line.strip)