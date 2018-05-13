#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import config
from pprint import pprint
from modules import utilities, encoder, exporter

if not os.path.isdir(config.OUTPUT_DIR):
    print('Creating output directory {0}'.format(config.OUTPUT_DIR))
    try:
        os.makedirs(config.OUTPUT_DIR)
    except Exception, e:
        print("ERROR {0} :: Failed to create output directory {1}".format(e, config.OUTPUT_DIR))


if __name__ == '__main__':
    user_data = utilities.read_data_file(config.TEST_DATA)
    user_data = utilities.build_data(user_data)

    ''' Serializations '''
    # JSON serializations
    json_blob = encoder.JsonSerializer(data=user_data)
    json_file = json_blob.encode(file_path=config.SERIALIZED_JSON)

    # PICKLE serializations
    pickle_blob = encoder.PickleSerializer(data=user_data)
    pickle_file = pickle_blob.encode(file_path=config.SERIALIZED_PKL)

    ''' De-Serializations '''
    # pprint(json_blob.decode(file_path=config.SERIALIZED_JSON))
    # pprint(pickle_blob.decode(file_path=config.SERIALIZED_PKL))

    ''' User readable output files '''
    # HTML file
    html_data = exporter.HtmlExporter(data=user_data)
    html_file = html_data.export(file_path=config.HTML)
    utilities.open_file(file_path=html_file)

    # Txt File
    text_data = exporter.TextExporter(data=user_data)
    text_file = text_data.export(file_path=config.TXT)
    utilities.open_file(file_path=text_file)
