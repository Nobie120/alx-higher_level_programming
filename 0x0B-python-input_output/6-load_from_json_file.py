#!/usr/bin/python3
''' Module for creating  an Object from a “JSON file” '''


import json


def load_from_json_file(filename):
    """  creates an Object from a “JSON file” """
    with open(filename, 'r', encoding="UTF-8") as f:
        return json.load(f)
