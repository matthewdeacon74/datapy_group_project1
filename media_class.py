class Media:

    def __init__(self, title: str, status: str, condition: int):
        self.title = title
        self.status = status
        self.condition = condition
        self.due_date = 'N/A'

    def get_inventory(self) -> str:
        item_info = f"Title: {self.title}\nStatus: {self.status}\nCondition: {self.condition}%\nDue Date: {self.due_date}"
        return item_info


class Book(Media):
    def __init__(self, title: str, author: str, status: str, condition: int):
        super().__init__(title, status, condition)
        self.author = author

    def get_inventory(self) -> str:
        item_info = f"Title: {self.title}\nAuthor: {self.author}\nStatus: {self.status}\nCondition: {self.condition}%\nDue Date: {self.due_date}"
        return item_info


class Movie(Media):
    def __init__(self, title: str, director: str, status: str, condition: int, runtime: int):
        super().__init__(title, status, condition)
        self.director = director
        self.runtime = runtime

    def get_inventory(self) -> str:
        item_info = f"Title: {self.title}\nDirector: {self.director}\nStatus: {self.status}\nRuntime: {self.runtime} minutes\nCondition: {self.condition}%\nDue Date: {self.due_date}"
        return item_info


