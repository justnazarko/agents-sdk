from vaccination_request import VACCINATION_REQUEST
from collection import Collection

def main():
    collection = Collection()
    filename = "data.txt"
    while True:
        print("\nMenu:")
        print("1. Load vaccination requests from file")
        print("2. Add a new vaccination request")
        print("3. Remove a vaccination request by ID")
        print("4. Edit a vaccination request by ID")
        print("5. Display all vaccination requests")
        print("6. Save data to the file")
        print("7. Search for requests")
        print("8. Sort requests")
        print(".. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            collection.load_requests_from_file(filename)
        elif choice == '2':
            request = VACCINATION_REQUEST()
            while True:
                try:
                    request.ID = input("Enter ID: ")
                    request.patient_name = input("Enter patient name: ")
                    request.patient_phone = input("Enter patient phone: ")
                    request.vaccine = input("Enter vaccine: ")
                    request.date = input("Enter date: ")
                    request.start_time = input("Enter start time: ")
                    request.end_time = input("Enter end time: ")
                    collection.add_request(request)
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")
                    continue
        elif choice == '3':
            ID = input("Enter ID to remove: ")
            collection.remove_request(ID)
        elif choice == '4':
            ID = input("Enter ID to edit: ")
            name = input("Enter new patient name: ")
            phone = input("Enter new patient phone: ")
            vaccine = input("Enter new vaccine: ")
            date = input("Enter new date: ")
            start_time = input("Enter new start time: ")
            end_time = input("Enter new end time: ")
            updated_request = VACCINATION_REQUEST(ID, name, phone, vaccine, date, start_time, end_time)
            collection.edit_request(ID, updated_request)
        elif choice == '5':
            collection.display_requests()
        elif choice == '6':
            collection.save_requests_to_file(filename)
            print("Requests saved to file.")
        elif choice == '7':
            query = input("Enter search query: ")
            collection.search_requests(query).display_requests()
        elif choice == '8':
            field = input("Enter field to sort by (ID, name, phone, vaccine, date, start_time, end_time): ")
            key = lambda x: getattr(x, field)
            collection.sort_requests(key)
        elif choice == '.':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
