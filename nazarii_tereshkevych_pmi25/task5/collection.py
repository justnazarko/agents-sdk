from vaccination_request import VACCINATION_REQUEST
from copy import deepcopy


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Collection:
    def __init__(self):
        self.vaccination_requests = []
        self._history = []
        self._max_history_size = 5

    def _create_memento(self):

        return Memento(deepcopy(self.vaccination_requests))

    def _add_to_history(self, memento):

        self._history.append(memento)
        if len(self._history) > self._max_history_size:
            self._history.pop(0)

    def save_state(self):

        memento = self._create_memento()
        self._add_to_history(memento)

    def undo(self):
        if len(self._history) > 1:
            self._history.pop()
            last_state = self._history[-1].get_state()
            self.vaccination_requests = deepcopy(last_state)

    def redo(self):
        if len(self._history) > 1:
            last_state = self._history.pop()
            self._history.append(last_state)
            last_state = self._history[-1].get_state()
            self.vaccination_requests = deepcopy(last_state)

    def add_request(self, request):
        self.vaccination_requests.append(request)
        self.save_state()

    def remove_request(self, ID):
        for request in self.vaccination_requests:
            if ID == request.ID:
                self.vaccination_requests.remove(request)
                self.save_state()
                return
        raise ValueError("There is no such object")

    def edit_request(self, ID, updated_request):
        for request in self.vaccination_requests:
            if request.ID == ID:
                self.save_state()

                request.ID = updated_request.ID
                request.patient_name = updated_request.patient_name
                request.patient_phone = updated_request.patient_phone
                request.vaccine = updated_request.vaccine
                request.date = updated_request.date
                request.start_time = updated_request.start_time
                request.end_time = updated_request.end_time
                return
        print(f"Request with ID {ID} not found.")

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
                    try:
                        request = VACCINATION_REQUEST(*data)
                    except ValueError as e:
                        print(line, e, sep="\n")
                        continue

                    self.add_request(request)

                else:
                    print(f"Invalid data: {line}")
        except FileNotFoundError:
            print("File not found.")

    def save_requests_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for request in self.vaccination_requests:
                    file.write(f"{request.ID},{request.patient_name},{request.patient_phone},{request.vaccine},"
                               f"{request.date},{request.start_time},{request.end_time}\n")
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
