# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 3
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_0.models.acl_object import AclObject  # noqa: F401,E501
from isi_sdk_8_0.models.member_object import MemberObject  # noqa: F401,E501


class NamespaceAcl(object):
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
        'acl': 'list[AclObject]',
        'action': 'str',
        'authoritative': 'str',
        'group': 'MemberObject',
        'mode': 'str',
        'owner': 'MemberObject'
    }

    attribute_map = {
        'acl': 'acl',
        'action': 'action',
        'authoritative': 'authoritative',
        'group': 'group',
        'mode': 'mode',
        'owner': 'owner'
    }

    def __init__(self, acl=None, action='replace', authoritative=None, group=None, mode=None, owner=None):  # noqa: E501
        """NamespaceAcl - a model defined in Swagger"""  # noqa: E501

        self._acl = None
        self._action = None
        self._authoritative = None
        self._group = None
        self._mode = None
        self._owner = None
        self.discriminator = None

        if acl is not None:
            self.acl = acl
        if action is not None:
            self.action = action
        if authoritative is not None:
            self.authoritative = authoritative
        if group is not None:
            self.group = group
        if mode is not None:
            self.mode = mode
        if owner is not None:
            self.owner = owner

    @property
    def acl(self):
        """Gets the acl of this NamespaceAcl.  # noqa: E501

        Provides the JSON array of access rights.  # noqa: E501

        :return: The acl of this NamespaceAcl.  # noqa: E501
        :rtype: list[AclObject]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this NamespaceAcl.

        Provides the JSON array of access rights.  # noqa: E501

        :param acl: The acl of this NamespaceAcl.  # noqa: E501
        :type: list[AclObject]
        """

        self._acl = acl

    @property
    def action(self):
        """Gets the action of this NamespaceAcl.  # noqa: E501

        Action tells if we want to update the existing acl or delete and replace it with new acl defined. Default action is replace.  # noqa: E501

        :return: The action of this NamespaceAcl.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NamespaceAcl.

        Action tells if we want to update the existing acl or delete and replace it with new acl defined. Default action is replace.  # noqa: E501

        :param action: The action of this NamespaceAcl.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def authoritative(self):
        """Gets the authoritative of this NamespaceAcl.  # noqa: E501

        If the directory has access rights set, then this field is returned as acl. If the directory has POSIX permissions set, then this field is returned as mode.  # noqa: E501

        :return: The authoritative of this NamespaceAcl.  # noqa: E501
        :rtype: str
        """
        return self._authoritative

    @authoritative.setter
    def authoritative(self, authoritative):
        """Sets the authoritative of this NamespaceAcl.

        If the directory has access rights set, then this field is returned as acl. If the directory has POSIX permissions set, then this field is returned as mode.  # noqa: E501

        :param authoritative: The authoritative of this NamespaceAcl.  # noqa: E501
        :type: str
        """

        self._authoritative = authoritative

    @property
    def group(self):
        """Gets the group of this NamespaceAcl.  # noqa: E501

        Provides the JSON object for the group persona of the owner.  # noqa: E501

        :return: The group of this NamespaceAcl.  # noqa: E501
        :rtype: MemberObject
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this NamespaceAcl.

        Provides the JSON object for the group persona of the owner.  # noqa: E501

        :param group: The group of this NamespaceAcl.  # noqa: E501
        :type: MemberObject
        """

        self._group = group

    @property
    def mode(self):
        """Gets the mode of this NamespaceAcl.  # noqa: E501

        Provides the POSIX mode.  # noqa: E501

        :return: The mode of this NamespaceAcl.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this NamespaceAcl.

        Provides the POSIX mode.  # noqa: E501

        :param mode: The mode of this NamespaceAcl.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def owner(self):
        """Gets the owner of this NamespaceAcl.  # noqa: E501

        Provides the JSON object for the owner persona.  # noqa: E501

        :return: The owner of this NamespaceAcl.  # noqa: E501
        :rtype: MemberObject
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this NamespaceAcl.

        Provides the JSON object for the owner persona.  # noqa: E501

        :param owner: The owner of this NamespaceAcl.  # noqa: E501
        :type: MemberObject
        """

        self._owner = owner

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NamespaceAcl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other