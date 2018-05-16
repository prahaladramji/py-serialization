#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import config
from modules import utilities
from modules.serializer import serializer
from modules.exporter import exporter

if not os.path.isdir(config.OUTPUT_DIR):
    print('Creating output directory {0}'.format(config.OUTPUT_DIR))
    try:
        os.makedirs(config.OUTPUT_DIR)
    except Exception, e:
        print("ERROR {0} :: Failed to create output directory {1}".format(e, config.OUTPUT_DIR))


if __name__ == '__main__':
    user_data = utilities.build_data(utilities.read_data_file(config.TEST_DATA))

    ''' Serializations '''
    json_blob = serializer['JsonSerializer'](data=user_data).serialize()
    print("json file saved here :  %s " % config.SERIALIZED_JSON)
    utilities.write_file(file_path=config.SERIALIZED_JSON, data=json_blob)

    pickle_blob = serializer['PickleSerializer'](data=user_data).serialize()
    print("pkl file saved here :  %s " % config.SERIALIZED_PKL)
    utilities.write_file(file_path=config.SERIALIZED_PKL, data=pickle_blob)

    ''' De-Serializations '''
    print(serializer['JsonSerializer'].deserialize(json_blob))
    print(serializer['PickleSerializer'].deserialize(pickle_blob))

    ''' User readable output files '''
    html_file = exporter['HtmlExporter'](data=user_data).export(file_path=config.HTML)
    utilities.open_file(file_path=html_file)

    text_file = exporter['TextExporter'](data=user_data).export(file_path=config.TXT)
    utilities.open_file(file_path=text_file)
