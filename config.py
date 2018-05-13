# -*- coding: utf-8 -*-

import os

PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA = os.path.join(PROJECT_ROOT_DIR, "test_data.csv")
OUTPUT_DIR = os.path.join(PROJECT_ROOT_DIR, "output")

SERIALIZED_JSON = os.path.join(OUTPUT_DIR, "serialized.json")
SERIALIZED_PKL = os.path.join(OUTPUT_DIR, "serialized.pkl")

TXT = os.path.join(OUTPUT_DIR, "output.txt")
HTML = os.path.join(OUTPUT_DIR, "output.html")
