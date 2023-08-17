#!/usr/bin/python3
"""
Import BaseModel
"""
from models.engine.base_model import BaseModel



class City(BaseModel):
    """
    City class
    """
    state_id = ""
    name = ""