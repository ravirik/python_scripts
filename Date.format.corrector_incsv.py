import csv
import datetime

# Function to convert mixed date formats into a singular format.
def convert_date(date_str):
    try:
        # Try parsing with '-' separator
        return datetime.datetime.strptime(date_str, '%d-%m-%Y').date().strftime('%Y-%m-%d')
    except ValueError:
        try:
            # If '-' parsing fails, try parsing with '/' separator
            return datetime.datetime.strptime(date_str, '%m/%d/%Y').date().strftime('%Y-%m-%d')
        except ValueError:
            return date_str  # Return original value for invalid date

# Read original CSV and update corrected values
with open('/supermarket_sales-Sheet1.csv', 'r', newline='') as input_file:
    csv_reader = csv.reader(input_file)
    rows = list(csv_reader)  # Read all rows into memory

# Update date values within the same CSV file
with open('/supermarket_sales-Sheet1.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)

    for row in rows:
        corrected_row = row[:]
        corrected_row[10] = convert_date(row[10])  # Update Date column

        csv_writer.writerow(corrected_row)

updated date formats within the same columns of the original CSV file
