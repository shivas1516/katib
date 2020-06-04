# coding: utf-8

"""
    katib

    swagger description for katib  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha3GraphConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'input_sizes': 'list[int]',
        'num_layers': 'int',
        'output_sizes': 'list[int]'
    }

    attribute_map = {
        'input_sizes': 'inputSizes',
        'num_layers': 'numLayers',
        'output_sizes': 'outputSizes'
    }

    def __init__(self, input_sizes=None, num_layers=None, output_sizes=None):  # noqa: E501
        """V1alpha3GraphConfig - a model defined in Swagger"""  # noqa: E501

        self._input_sizes = None
        self._num_layers = None
        self._output_sizes = None
        self.discriminator = None

        if input_sizes is not None:
            self.input_sizes = input_sizes
        if num_layers is not None:
            self.num_layers = num_layers
        if output_sizes is not None:
            self.output_sizes = output_sizes

    @property
    def input_sizes(self):
        """Gets the input_sizes of this V1alpha3GraphConfig.  # noqa: E501


        :return: The input_sizes of this V1alpha3GraphConfig.  # noqa: E501
        :rtype: list[int]
        """
        return self._input_sizes

    @input_sizes.setter
    def input_sizes(self, input_sizes):
        """Sets the input_sizes of this V1alpha3GraphConfig.


        :param input_sizes: The input_sizes of this V1alpha3GraphConfig.  # noqa: E501
        :type: list[int]
        """

        self._input_sizes = input_sizes

    @property
    def num_layers(self):
        """Gets the num_layers of this V1alpha3GraphConfig.  # noqa: E501


        :return: The num_layers of this V1alpha3GraphConfig.  # noqa: E501
        :rtype: int
        """
        return self._num_layers

    @num_layers.setter
    def num_layers(self, num_layers):
        """Sets the num_layers of this V1alpha3GraphConfig.


        :param num_layers: The num_layers of this V1alpha3GraphConfig.  # noqa: E501
        :type: int
        """

        self._num_layers = num_layers

    @property
    def output_sizes(self):
        """Gets the output_sizes of this V1alpha3GraphConfig.  # noqa: E501


        :return: The output_sizes of this V1alpha3GraphConfig.  # noqa: E501
        :rtype: list[int]
        """
        return self._output_sizes

    @output_sizes.setter
    def output_sizes(self, output_sizes):
        """Sets the output_sizes of this V1alpha3GraphConfig.


        :param output_sizes: The output_sizes of this V1alpha3GraphConfig.  # noqa: E501
        :type: list[int]
        """

        self._output_sizes = output_sizes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1alpha3GraphConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha3GraphConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
