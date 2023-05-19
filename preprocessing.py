import csv

# List of input file names
input_files = ["output-york07-ga-01.txt", "output-york07-ga-02.txt", "output-york07-ga-03.txt", "output-york07-ga-04.txt", "output-york07-ga-05.txt"]

# List of output file names
output_files = ["output-york07-ga-01.csv", "output-york07-ga-02.csv", "output-york07-ga-03.csv", "output-york07-ga-04.csv", "output-york07-ga-05.csv"]

# List of field names for the CSV file
fieldnames = ["Topic", "DocID", "Rank", "Okapi", "Offset", "Bytes", "TagID"]

# Loop over the input files
for i in range(len(input_files)):
    # Open the input file for reading and the output file for writing
    with open(input_files[i], 'rt', encoding='cp949') as f_in, open(output_files[i], 'w', newline='') as f_out:
        # Create a CSV writer object
        writer = csv.writer(f_out)
        # Write the column names as the first row of the CSV file
        writer.writerow(fieldnames)
        # Loop over each line in the input file
        for line in f_in:
            # Split the line into a list of values
            row = line.split()
            # Write the row to the CSV file
            writer.writerow(row)
