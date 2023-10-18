from vaccination_request import VACCINATION_REQUEST


class Collection:
    def __init__(self):
        self.vaccination_requests = []

    def add_request(self, request):
        self.vaccination_requests.append(request)

    def remove_request(self, ID):
        self.vaccination_requests = [request for request in self.vaccination_requests if request.ID != ID]

    def edit_request(self, ID, updated_request):
        for request in self.vaccination_requests:
            if request.ID == ID:
                request.ID = updated_request.ID
                request.patient_name = updated_request.patient_name
                request.patient_phone = updated_request.patient_phone
                request.vaccine = updated_request.vaccine
                request.date = updated_request.date
                request.start_time = updated_request.start_time
                request.end_time = updated_request.end_time

    def display_requests(self):
        if len(self.vaccination_requests) == 0:
            print("The collection is empty")
        for request in self.vaccination_requests:
            print(request)

    def load_requests_from_file(self, filename):
        try:
            file = open(filename, 'r')
            for line in file:
                data = line.strip().split(',')
                if len(data) == 7:
                    request = VACCINATION_REQUEST(*data)
                    self.add_request(request)

                else:
                    print(f"Invalid data: {line}")
        except FileNotFoundError:
            print("File not found.")

    def save_requests_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for request in self.vaccination_requests:
                    file.write(f"{request.ID},{request.patient_name},{request.patient_phone},{request.vaccine},{request.date},{request.start_time},{request.end_time}\n")
        except FileNotFoundError:
            print("File not found.")

    def search_requests(self, query):
        query = query.lower()
        matching_requests = Collection()
        for request in self.vaccination_requests:
            request_str = str(request).lower()
            if query in request_str:
                matching_requests.vaccination_requests.append(request)
        return matching_requests

    def sort_requests(self, key):
        self.vaccination_requests.sort(key=key)

