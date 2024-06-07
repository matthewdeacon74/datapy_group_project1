class Media:

    def __init__(self, title: str, author: str, status: str, condition: int):
        self.title = title
        self.author = author
        self.status = status
        self.condition = condition
        self.due_date = 'N/A'

    def get_inventory(self) -> str:
        item_info = f"Title: {self.title}\nAuthor: {self.author}\nStatus: {self.status}\nCondition: {self.condition}%\nDue Date: {self.due_date}"
        return item_info


