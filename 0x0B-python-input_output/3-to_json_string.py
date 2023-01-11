#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json


def to_json_string(my_obj):
    """
    Returns a json string containing object's representation

    Arguments:
        my_obj (str): The inputed object to convert in json format

    Return:
        A json format text
    """
    return json.dumps(my_obj)
