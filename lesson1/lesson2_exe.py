import csv

# Write a list of 3 strings to a file called log.txt.
# Read that file and print each line.
with open("lesson1\\log.txt", "r") as files:
    for line in files:
        print(line.strip())


# Write a list of lists (table data) to table.csv using the csv module.
# Read that same table.csv back and print each row.
list_of_lists = [["the following"], ["is a list"], ["of lists"],["that I'm using for an exercise"]]

with open("table.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(list_of_lists)
    print(line.strip()) 


table_data = [["Alice", 20, "Data Engineer" ],
              ["Bob", 25, "Software Developer"],
              ["Claire", 35, "Data Analyst"],
              ["Dillon", 50, "CTO"]
]

with open("people.csv", "w", newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(table_data)
    
print("people.csv has been written")

with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)















log_entry = ["Pipeline started", "Reading files", "Pipeline complete"]
with open("log_review.txt", "w") as file:
        for entry in log_entry:
             file.write(entry + "\n" )

with open("log_review.txt", "r") as f:
     for log in f:
          print(log.strip())


#import csv
# department_list = [["Finance", "Alice", 12], ["HR", "Bob", 8], ["IT", "Charlie", 25]]
# with open("departments.csv", "w") as f:
#      writer = csv.writer(f)
#      writer.writerows(department_list)

# #import csv
# with open("departments.csv", "r") as f:
#      reader = csv.reader(f)
#      for department, name, staff_count in reader:
#           if int(staff_count) > 10:
#                print(f"{department} has {staff_count} staff members")


def load_large_file(path):
     error_count = 0
     with open(path) as f:
          for line in f:
               if "Error" in line.lower():
                    error_count += 1
          return f" Found {error_count} error lines."
        

dictionary_exe = {"pipeline_name":"daily_sales_etl",
                  "enabled": True,
                  "batch_size": 500,
                  "output_format": "parquet"
                  }

import json
with open("config.json", "w") as f:
     json.dump(dictionary_exe, f, indent = 2)

with open("config.json", "r") as f:
     json_load = json.load(f)
     print(json_load["pipeline_name"])

#Bonus Exercise
with open("sale_log.txt", "r") as file:
     success_count = 0
     error_count = 0
     for line in file:
          if "SUCCESS" in line:
               success_count += 1
          if "ERROR" in line:
               error_count += 1

summary = {"success_count":success_count,
           "error_count":error_count
           }

with open("summary.json", "w") as f:
     json.dump(summary, f, indent = 2)
