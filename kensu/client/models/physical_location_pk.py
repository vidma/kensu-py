# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat

from six import iteritems


class PhysicalLocationPK(object):
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
        'city': 'str',
        'country': 'str'
    }

    attribute_map = {
        'city': 'city',
        'country': 'country'
    }

    def __init__(self, city=None, country=None):
        """
        PhysicalLocationPK - a model defined in Swagger
        """

        self._city = None
        self._country = None

        self.city = city
        self.country = country

    @property
    def city(self):
        """
        Gets the city of this PhysicalLocationPK.

        :return: The city of this PhysicalLocationPK.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this PhysicalLocationPK.

        :param city: The city of this PhysicalLocationPK.
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")

        self._city = city

    @property
    def country(self):
        """
        Gets the country of this PhysicalLocationPK.

        :return: The country of this PhysicalLocationPK.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this PhysicalLocationPK.

        :param country: The country of this PhysicalLocationPK.
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")

        self._country = country

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
        if not isinstance(other, PhysicalLocationPK):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
