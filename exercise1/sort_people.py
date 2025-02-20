import json
import argparse
from datetime import datetime

# Function to calculate age based on date of birth
def calculate_age(dob):
    today = datetime.today()
    dob = datetime.strptime(dob, "%Y-%m-%d")
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# Function to read the JSON file and remove duplicates
def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Remove duplicates based on name and date of birth
    unique_people = []
    seen = set()
    
    for person in data:
        identifier = (person["name"], person["dob"])  # Creating a tuple (name, dob) to identify duplicates
        if identifier not in seen:
            seen.add(identifier)
            unique_people.append(person)

    return unique_people

# Function to sort the people by age
def sort_by_age(people):
    return sorted(people, key=lambda person: calculate_age(person["dob"]))

# Function to print the sorted list of people
def print_people(people):
    for person in people:
        print(f"{person['name']} - Age: {calculate_age(person['dob'])}, Country of Birth: {person['country_of_birth']}")

def main():
    # Set up argparse to accept the JSON file as an argument
    parser = argparse.ArgumentParser(description="Process and sort people by age from a JSON file.")
    parser.add_argument('file_path', help="Path to the input JSON file.")
    
    args = parser.parse_args()

    # Parse the JSON and remove duplicates
    people = parse_json(args.file_path)

    # Sort people by age
    sorted_people = sort_by_age(people)

    # Print the sorted list
    print("\nPeople sorted by age:")
    print_people(sorted_people)

if __name__ == "__main__":
    main()

