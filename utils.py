from typing import List
from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    name: str
    email: str

class Librarian(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)

class Member(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)

@dataclass
class Book:
    book_id: int
    title: str
    author: str
    availability: bool