#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import config
from modules import utilities, encoder, exporter


class UnitTests(unittest.TestCase):
    """
    Unit Test class for serializer
    """
    user_data = utilities.read_data_file(config.TEST_DATA)
    user_data = utilities.build_data(user_data)

    def test_json(self):
        json_blob = encoder.JsonSerializer(data=self.user_data)
        json_file = json_blob.encode(file_path=config.SERIALIZED_JSON)
        json_deserialized_data = json_blob.decode(file_path=json_file)
        self.assertEqual(self.user_data, json_deserialized_data)

    def test_pickle(self):
        pickle_blob = encoder.PickleSerializer(data=self.user_data)
        pickle_file = pickle_blob.encode(file_path=config.SERIALIZED_PKL)
        pickle_deserialized_data = pickle_blob.decode(file_path=pickle_file)
        self.assertEqual(self.user_data, pickle_deserialized_data)

    def test_html(self):
        html_data = exporter.HtmlExporter(data=self.user_data)
        html_data.export(file_path=config.HTML)

    def test_txt(self):
        text_data = exporter.TextExporter(data=self.user_data)
        text_data.export(file_path=config.TXT)


if __name__ == '__main__':
    unittest.main()
