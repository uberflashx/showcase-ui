from enum import Enum

class AllureStory(str, Enum):
    SEARCH = "Search"
    CART = "Cart"
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"