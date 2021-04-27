# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat

from six import iteritems


class BatchSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'timestamp': 'int',
        'entity': 'Schema'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'entity': 'entity'
    }

    def __init__(self, timestamp=None, entity=None):
        """
        BatchSchema - a model defined in Swagger
        """

        self._timestamp = None
        self._entity = None

        self.timestamp = timestamp
        self.entity = entity

    @property
    def timestamp(self):
        """
        Gets the timestamp of this BatchSchema.
        Timestamp of creation

        :return: The timestamp of this BatchSchema.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this BatchSchema.
        Timestamp of creation

        :param timestamp: The timestamp of this BatchSchema.
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def entity(self):
        """
        Gets the entity of this BatchSchema.
        Entity to store

        :return: The entity of this BatchSchema.
        :rtype: Schema
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this BatchSchema.
        Entity to store

        :param entity: The entity of this BatchSchema.
        :type: Schema
        """
        if entity is None:
            raise ValueError("Invalid value for `entity`, must not be `None`")

        self._entity = entity

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, BatchSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
