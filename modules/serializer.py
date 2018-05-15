# -*- coding: utf-8 -*-

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
    def __new__(mcs, class_name, bases, attributes):
        new_class = type.__new__(mcs, class_name, bases, attributes)
        register_serializer(new_class)
        return new_class


class Serializer(object):
    """
    The base class for other defined serializers.
    """
    __metaclass__ = RegisterMetaClass

    def __init__(self, data=None):
        super(Serializer, self).__init__()
        self.data_to_serialize = data

    def serialize(self):
        """
        Method to serialize the data.
        """
        raise NotImplementedError

    def deserialize(self, data):
        """
        Method to deserialize the data.
        """
        raise NotImplementedError


class JsonSerializer(Serializer):
    """
    JSON Serializer class.
    """
    def serialize(self):
        return json.dumps(self.data_to_serialize, indent=4)

    @classmethod
    def deserialize(cls, data):
        return json.loads(data)


class PickleSerializer(Serializer):
    """
    Pickle Serializer class.
    """
    def serialize(self):
        return pickle.dumps(self.data_to_serialize)

    @classmethod
    def deserialize(cls, data):
        return pickle.loads(data)
