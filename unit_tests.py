#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import config
from modules import utilities, serializer, exporter


class UnitTests(unittest.TestCase):
    """
    Unit Test class for serializer
    """
    user_data = utilities.build_data(utilities.read_data_file(config.TEST_DATA))

    def test_json(self):
        json_serializer_object = serializer.JsonSerializer(data=self.user_data)
        json_blob = json_serializer_object.serialize()
        json_deserialized_data = serializer.JsonSerializer.deserialize(data=json_blob)
        self.assertEqual(self.user_data, json_deserialized_data)

    def test_pickle(self):
        pickle_serializer_object = serializer.PickleSerializer(data=self.user_data)
        pickle_blob = pickle_serializer_object.serialize()
        pickle_deserialized_data = serializer.PickleSerializer.deserialize(data=pickle_blob)
        self.assertEqual(self.user_data, pickle_deserialized_data)

    def test_html(self):
        html_data = exporter.HtmlExporter(data=self.user_data)
        html_data.export(file_path=config.HTML)

    def test_txt(self):
        text_data = exporter.TextExporter(data=self.user_data)
        text_data.export(file_path=config.TXT)


if __name__ == '__main__':
    unittest.main()
