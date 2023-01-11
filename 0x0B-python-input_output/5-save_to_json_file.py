#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
"""A function that creates an Object from a “JSON file”."""


def save_to_json_file(my_obj, filename):
    """Saves Object to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


