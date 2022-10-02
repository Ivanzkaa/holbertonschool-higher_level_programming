#!/usr/bin/python3
"""
Before the function
"""


import sys
import os


arg = sys.argv[1:]


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


py_list = []

if os.path.exists("./add_item.json"):
    py_list = load_from_json_file("add_item.json")

save_to_json_file(py_list + arg, "add_item.json")
