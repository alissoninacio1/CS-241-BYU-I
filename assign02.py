"""
Write a Python 3 program to read from a .csv file containing rates from power companies.
Your program should determine the average commercial rate,
and also display the information for the highest and lowest rates found.
"""

#import csv in order towork with this type of file
import csv

#Prompt the user for a filename.
def get_file():
    file_name = input("Please enter the data file:")
    return file_name

"""
Open the requested file and read through it line by line.
Ignore the first line, as it contains header information.
"""

def reading_file(file_name):
     with open(file_name, new_line='') as f:
        comm_rate = []
        zip_data = []
        state = []
        name = []
        reader = csv.DictReader(f)
        for line in reader:
            comm_rate.append(float(line['comm_rate']))
            zip_data.append(int(line['zip']))
            state.append(line['state'])
            name.append(line['utility_name'])

        return (comm_rate, zip_data, state, name)

"""
display the average (mean) commercial rate across all zip codes.
"""

def rate_average(comm_rate):
        Sum = float(sum(comm_rate))
        average = str(Sum / float(len(comm_rate)))
        print(f"The average comercial rate is: ${average}\n")
        
"""
Display the utility company, zip code, state, and rate for the zip code with the highest commercial rate in the file.
"""

def highest_rate(comm_rate, zip_data, state, name):
    length = len(comm_rate)
    taxa = comm_rate
    max_value = max(taxa[-length:])
    index = taxa.index(max_value)
    print("The highest rate is:")
    print(f"{name[index]} ({zipData[index]}, {state[inex]}) - ${max_value}\n")


"""
Display the utility company, zip code, state, and rate for the zip code with the lowest commercial rate in the file.
"""
def lowest_rate(comm_rate, zip_data, state, name):
    length = len(comm_rate)
    taxa = comm_rate
    outra = taxa[-length:]
    min_value = min(outra[-length:])
    index = taxa.index(min_value)
    print("The lowest rate is:")
    print(f"{name[index]} ({zip_data[index]}, {state[index]}) - ${min_value}")



def main():
    file_name = get_file()
    (comm_rate, zip_data, state, name) = reading_file(file_name)
    rate_average(comm_rate)
    highest_rate(comm_rate, zip_data, state, name)
    lowest_rate(comm_rate, zip_data, state, name)


if _name_ == "_main_":
    main()


#This code was based in another code, but modified for my own used. 
