import csv

# Define the input and output file paths
input_csv_file = 'token_balances_usd.csv'  # Replace with the actual path to your CSV file
output_csv_file = 'cleaned_token_balances_usd.csv'

def clean_csv(input_file, output_file):
    try:
        # Attempt to read the CSV file with utf-8 encoding
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            rows = list(reader)  # Read all rows into a list

        # Prepare to write to the output file
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # Write the first row (header) to the output file
            writer.writerow(rows[0])

            # Flag to track if we've written the header already
            header_written = False
            
            for row in rows[1:]:  # Skip the header row
                # Check if the row is a header or empty
                if row[0].strip() == "Address":
                    if not header_written:
                        writer.writerow(row)  # Write the first header occurrence
                        header_written = True  # Set flag to true after writing
                    continue  # Skip further occurrences of the header

                # Remove '$' from the USD Value column (4th column, index 3)
                if len(row) > 3:
                    row[3] = row[3].replace('$', '')  # Remove dollar sign

                writer.writerow(row)  # Write all other rows

    except UnicodeDecodeError:
        print("UnicodeDecodeError: Trying a different encoding...")
        # Try reading with a different encoding (e.g., latin1)
        with open(input_file, mode='r', newline='', encoding='latin1') as infile:
            reader = csv.reader(infile)
            rows = list(reader)  # Read all rows into a list

        # Prepare to write to the output file
        with open(output_file, mode='w', newline='', encoding='latin1') as outfile:
            writer = csv.writer(outfile)

            # Write the first row (header) to the output file
            writer.writerow(rows[0])

            # Flag to track if we've written the header already
            header_written = False
            
            for row in rows[1:]:  # Skip the header row
                if row[0].strip() == "Address":
                    if not header_written:
                        writer.writerow(row)
                        header_written = True
                    continue

                # Remove '$' from the USD Value column (4th column, index 3)
                if len(row) > 3:
                    row[3] = row[3].replace('$', '')  # Remove dollar sign

                writer.writerow(row)

def main():
    clean_csv(input_csv_file, output_csv_file)
    print(f"Cleaned CSV file '{output_csv_file}' has been created successfully.")

if __name__ == "__main__":
    main()