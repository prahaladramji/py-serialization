# -*- coding: utf-8 -*-

import os
import sys
import json
import pickle

# Serialization format classes registry
registry = dict()


def get_supported_serializer_formats():
    """
    Get all the supported serialization formats.
    """
    return registry


def register_serializer(target_class):
    """
    Helper method to register a serializer class.
    """
    registry[target_class.__name__] = target_class
    return target_class


class RegisterMetaClass(type):
    """
    Meta-Class to register with registry of supported serializers.
    """
    def __new__(cls, class_name, bases, attributes):
        new_class = super(RegisterMetaClass, cls).__new__(cls, class_name, bases, attributes)
        register_serializer(new_class)
        return new_class


class Serializer(object):
    """
    The base class for other defined serializers.
    """

    def __init__(self, data):
        super(Serializer, self).__init__()
        self.data_to_serialize = data

    def encode(self):
        """
        Method to encode/serialize the data.
        """
        raise NotImplementedError

    def decode(self):
        """
        Method to decode/de-serialize the data.
        """
        raise NotImplementedError


class JsonSerializer(Serializer):
    """
    JSON Serializer class.
    """

    # Register the class
    __metaclass__ = RegisterMetaClass

    def __init__(self, data=None):
        super(JsonSerializer, self).__init__(data)

    def encode(self, file_path=None):
        """
        Method to encode/serialize the data in json format.
        """

        serialized_file = file_path.replace("\\", "/")

        with open(serialized_file, "w") as write_file:
            json.dump(self.data_to_serialize, write_file, indent=4)

        print("Json serialized data saved here :  %s" % serialized_file)
        return serialized_file

    @classmethod
    def decode(cls, file_path=None):
        """
        Method to decode/de-serialize the data from a json file.
        """

        serialized_file = file_path.replace("\\", "/")

        if not os.path.exists(serialized_file):
            sys.exit("{0} not found".format(serialized_file))

        with open(serialized_file, "r") as read_file:
            data = json.load(read_file)
        return data


class PickleSerializer(Serializer):
    """
    Pickle Serializer class.
    """

    # Register this class
    __metaclass__ = RegisterMetaClass

    def __init__(self, data):
        super(PickleSerializer, self).__init__(data)

    def encode(self, file_path=None):
        """
        Method for encode/serialize the data in pickle binary format.
        """

        serialized_file = file_path.replace("\\", "/")

        with open(serialized_file, "wb") as write_file:
            pickle.dump(self.data_to_serialize, write_file)

        print("Binary serialized data saved here :  %s" % serialized_file)
        return serialized_file

    @classmethod
    def decode(cls, file_path=None):
        """
        Method for decode/de-serialize the data from a pickle binary file.
        """

        serialized_file = file_path.replace("\\", "/")

        if not os.path.exists(serialized_file):
            sys.exit("{0} not found".format(serialized_file))

        with open(serialized_file, "rb") as read_file:
            data = pickle.load(read_file)
        return data

