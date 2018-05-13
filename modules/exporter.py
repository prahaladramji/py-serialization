# -*- coding: utf-8 -*-

from collections import OrderedDict

registry = dict()


def get_supported_output_formats():
    """
    Get all the supported output formats
    """
    return registry


def register_exporter(target_class):
    """
    Helper method to register an exporter class.
    """
    registry[target_class.__name__] = target_class
    return target_class


class RegisterMetaClass(type):
    """
    Meta-Class to register with registry of supported exporters.
    """
    def __new__(cls, class_name, bases, attributes):
        new_class = super(RegisterMetaClass, cls).__new__(cls, class_name, bases, attributes)
        register_exporter(new_class)
        return new_class


class Exporter(object):
    """
    The base class for other defined exporters.
    """

    def __init__(self, data):
        self.data = data

    def get_context(self):
        return self.data

    def convert_data_to_string(self):
        raise NotImplemented

    def export(self):
        """
        Method for the main export process.
        """
        raise NotImplemented


class HtmlExporter(Exporter):
    """
    Export the data to a html file.
    """

    # Register the class
    __metaclass__ = RegisterMetaClass

    def convert_data_to_string(self):
        """
        Generate and render the html content
        """

        data = self.get_context()

        html_string = """
        <html><body><table border=1, align="center">
        <tr>{HEAD}</tr><indent>{DATA}</indent>
        </table></body></html>
        """
        _head_string = ""
        _data_string = ""
        _header_updated = False
        for each_field in data:
            _data_string += "\t\t<tr>\n\t\t\t"
            for heading, info in OrderedDict(each_field).iteritems():
                _data_string += "<td align='center'> %s </td>\n\t\t\t" % info
                if _header_updated:
                    continue
                _head_string += "<th> %s </th>\n\t\t" % heading
            _header_updated = True
            _data_string += "\n\t\t</tr>\n"

        return html_string.format(HEAD=_head_string, DATA=_data_string)

    def export(self, file_path=None):
        """
        Export the rendered content to html file.
        """

        html_string = self.convert_data_to_string()

        with open(file_path, "w") as html_writer:
            html_writer.write(html_string)

        print("HTML output saved here :  %s " % file_path)
        return file_path


class TextExporter(Exporter):
    """
    Export data to a text file.
    """

    # Register this class
    __metaclass__ = RegisterMetaClass

    def convert_data_to_string(self):
        """
        Format the data to pretty print in a text file.
        """

        data = self.get_context()

        text_string = "------------------------------------------------\n"
        text_string += "----------  Output in TEXT Format  -------------\n"
        text_string += "------------------------------------------------\n"

        for each_info in data:
            for heading, info in OrderedDict(each_info).iteritems():
                text_string += "\t{0}\t\t:\t{1} \n".format(heading, info)
            text_string += "\n"
            text_string += "------------------------------------------------\n"
        return text_string

    def export(self, file_path=None):
        """
        Export to text file.
        """

        text_string = self.convert_data_to_string()

        with open(file_path, "w") as text_writer:
            text_writer.write(text_string)

        print("Text output Saved here :  %s " % file_path)
        return file_path
