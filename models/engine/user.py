#!/usr/bin/python3
"""
A class named User
"""
from models.engine.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""