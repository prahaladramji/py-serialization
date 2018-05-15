#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import config
from pprint import pprint
from modules import utilities, serializer, exporter

if not os.path.isdir(config.OUTPUT_DIR):
    print('Creating output directory {0}'.format(config.OUTPUT_DIR))
    try:
        os.makedirs(config.OUTPUT_DIR)
    except Exception, e:
        print("ERROR {0} :: Failed to create output directory {1}".format(e, config.OUTPUT_DIR))


if __name__ == '__main__':
    user_data = utilities.build_data(utilities.read_data_file(config.TEST_DATA))

    ''' Serializations '''
    # JSON serializations
    json_serializer_object = serializer.JsonSerializer(data=user_data)
    json_blob = json_serializer_object.serialize()
    print("json file saved here :  %s " % config.SERIALIZED_JSON)
    utilities.write_file(file_path=config.SERIALIZED_JSON, data=json_blob)

    # PICKLE serializations
    pickle_serializer_object = serializer.PickleSerializer(data=user_data)
    pickle_blob = pickle_serializer_object.serialize()
    print("pkl file saved here :  %s " % config.SERIALIZED_PKL)
    utilities.write_file(file_path=config.SERIALIZED_PKL, data=pickle_blob)

    ''' De-Serializations '''
    pprint(serializer.JsonSerializer.deserialize(data=json_blob))
    pprint(serializer.PickleSerializer.deserialize(data=pickle_blob))

    ''' User readable output files '''
    # HTML file
    html_data = exporter.HtmlExporter(data=user_data)
    html_file = html_data.export(file_path=config.HTML)
    utilities.open_file(file_path=html_file)

    # Txt File
    text_data = exporter.TextExporter(data=user_data)
    text_file = text_data.export(file_path=config.TXT)
    utilities.open_file(file_path=text_file)
