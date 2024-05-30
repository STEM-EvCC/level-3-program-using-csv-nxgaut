import csv

#specify the input and output file names
input_file = 'security_incidents.csv'
output_file ='securtiy_incidents_modified.csv'

#read the csv file and store data in list
with open(input_file, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    data = list(reader)

#add a new column named status with a default value of "pending"
new_column_name = 'status'
defaulth_value = 'pending'

#add the new column to header
header = data[0] + [new_column_name]

#add the new column to each row
rows = [row + [defaulth_value] for row in data[1:]]

#write modified data to new csv file
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f"modified data saved to '{output_file}'")