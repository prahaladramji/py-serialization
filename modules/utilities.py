# -*- coding: utf-8 -*-

import os
import csv
import webbrowser
from collections import OrderedDict


def read_data_file(file_path):
    """
    Read the sample data file
    """
    if not os.path.exists(file_path):
        sys.exit("Test data not found")

    with open(file_path, "r") as data_file:
        reader = csv.reader(data_file, delimiter=',')
        for row in reader:
            yield row


def build_data(data):
    """
    Build the data for use with the serializer class
    """
    container = list()
    content = list(data)
    if not content:
        return container

    headers = content.pop(0)
    for info in content:
        local_dict = OrderedDict(zip(headers, info))
        container.append(local_dict)

    return container


def open_file(file_path=None):
    """
    Open the file in a web browser.
    """
    if not os.path.exists(file_path):
        sys.exit("File not found in {0}".format(file_path))

    try:
        webbrowser.open("file://" + file_path)
    except Exception, e:
        print("Unable to open file in {0} :: ERROR: {1}".format(file_path, e))
