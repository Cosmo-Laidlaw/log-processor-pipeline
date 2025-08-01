files = ['data_2024.csv','data_2025.csv','logfile.txt']
print(files[0]) #first element
files.append('readme.md')
print(files)
# USE CASE: storing column names, file paths, rows of data

record = (2023, 50000)
print(record[0])
# USE CASE: returning multiple values from a function, database rows

config = {
    "input_path" : "/data_raw",
    "output_path" : "/data_cleaned",
    "batch_size" : 100
}

print(config['input_path'])

config["batch_size"] = 200 #update value
print(config['batch_size'])

seen_ids = {101, 102, 103}
seen_ids.add(104)
print(103 in seen_ids) # check for existince