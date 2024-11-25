import sys
import csv

def main():
    try:
        if len(sys.argv) != 3:
            print("Usage: python scourgify.py <input_csv_file> <output_csv_file>")
            sys.exit(1)
        
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        with open(input_file, newline='') as file:
            reader = csv.reader(file)
            next(reader)
            students = []
            for row in reader:
                name_parts = row[0].strip('"').split(", ") 
                first_name = name_parts[1]
                last_name = name_parts[0]
                house = row[1]
                students.append([first_name, last_name, house])

        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["first", "last", "house"])
            writer.writerows(students)

        print("Data has been successfully processed.")

    except FileNotFoundError:
        print("Input file not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()