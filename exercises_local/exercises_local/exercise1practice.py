# Create a list of five file names: "data_jan.csv" through "data_may.csv"
# make a tuple that contains a year and a month
# Create a dictionary that holds config info "db" = postgres, "port" = 5432, "timeout" = 30


from numpy import extract


files = ["data_jan.csv", "data_feb.csv", "data_mar.csv", "data_apr", "data_may.csv"]
date_y_m = (2024, "Jan")
config = {
    "db":"postgres",
    "port": 5432,
    "timeout": 30
}

#4
given_list = ["a.csv", "b.csv", "a.csv", "c.csv", "b.csv"]
unique_files = list(set(given_list))
print(unique_files)

#5
def bak_ext(filenames):
    empty_list= []
    for file in filenames:
        empty_list.append(file + ".bak")
    return empty_list


#6 Create a dictionary where: Keys are filenames (strings) & Values are file sizes in megabytes (integers or floats)
folder = {
    "a.csv": 10,
    "b.csv": 200,
    "c.csv": 102
}

#7 Write a function that takes a dictionary of file paths and sizes, and returns only the paths for files over 100MB
def get_large_files(file_dict):
    large_file = []
    for name, size in file_dict.items():
        if size > 100:
            large_file.append(name)
    return large_file

print(get_large_files(folder))

#8 Simulate loading multiple files and logging a message for each like: "Loaded data_jan.csv successfully." using a loop

def load_files(files):
    for file in files:
        {f"Loaded {file} successfully."}

#9 Create a list of tuples, each containing a filename and its size. Then extract all filenames >100MB into a new list.
folder = [("a.csv", 200),("b.csv", 300),("c.csv", 80)]

def extract_large_files(tuple_list):
    large_file_list = []
    for name, size in tuple_list:
        if size > 100:
            large_file_list.append(name)
    return large_file_list

print(extract_large_files(folder))       
