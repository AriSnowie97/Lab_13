import json

def load_data(filename="rozetka_phones.json"):
    """Loads data from a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in file '{filename}'.")
        return []

def sort_phones(phones, criterion, reverse=False):
    return sorted(phones, key=lambda phone: phone.get(criterion), reverse=reverse)

def find_phones(phones, query):
    query = query.lower()
    results = []
    for phone in phones:
        if query in phone.get('name', '').lower():
            results.append(phone)
        else:
            for key, value in phone.items():
                if isinstance(value, (int, float, str)) and query in str(value).lower():
                    results.append(phone)
                    break
    return results

def display_phone_details(phone):
    print("\nDetailed Information:")
    for key, value in phone.items():
        print(f"{key.capitalize()}: {value}")
    print("-" * 20)

def main():
    phones = load_data()
    if not phones:
        return

    while True:
        print("\nMenu:")
        print("1. View all phones")
        print("2. Sort by price")
        print("3. Sort by rating")
        print("4. Sort by review count")
        print("5. Search for a phone")
        print("6. View phone details (by index)")
        print("7. Exit")

        choice = input("Choose an action: ")

        if choice == '1':
            for i, phone in enumerate(phones):
                print(f"{i+1}. {phone['name']}")
        elif choice == '2':
            sorted_phones = sort_phones(phones, 'price')
            for i, phone in enumerate(sorted_phones):
                print(f"{i+1}. {phone['name']} (Price: {phone['price']})")
        elif choice == '3':
            sorted_phones = sort_phones(phones, 'rating', reverse=True)
            for i, phone in enumerate(sorted_phones):
                print(f"{i+1}. {phone['name']} (Rating: {phone['rating']})")
        elif choice == '4':
            sorted_phones = sort_phones(phones, 'review_count', reverse=True)
            for i, phone in enumerate(sorted_phones):
                print(f"{i+1}. {phone['name']} (Reviews: {phone['review_count']})")
        elif choice == '5':
            query = input("Enter name or characteristic to search: ")
            found_phones = find_phones(phones, query)
            if found_phones:
                print("\nFound:")
                for i, phone in enumerate(found_phones):
                    print(f"{i+1}. {phone['name']}")
            else:
                print("Nothing found.")
        elif choice == '6':
            try:
                index = int(input("Enter the index of the phone to view details: ")) - 1
                if 0 <= index < len(phones):
                    display_phone_details(phones[index])
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a number.")
        elif choice == '7':
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()