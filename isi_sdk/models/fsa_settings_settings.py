# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class FsaSettingsSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FsaSettingsSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'default_template': 'str',
            'disk_usage_depth': 'int',
            'max_age': 'int',
            'max_count': 'int',
            'squash_depth': 'int',
            'top_n_max': 'int',
            'use_snapshot': 'bool'
        }

        self.attribute_map = {
            'default_template': 'default_template',
            'disk_usage_depth': 'disk_usage_depth',
            'max_age': 'max_age',
            'max_count': 'max_count',
            'squash_depth': 'squash_depth',
            'top_n_max': 'top_n_max',
            'use_snapshot': 'use_snapshot'
        }

        self._default_template = None
        self._disk_usage_depth = None
        self._max_age = None
        self._max_count = None
        self._squash_depth = None
        self._top_n_max = None
        self._use_snapshot = None

    @property
    def default_template(self):
        """
        Gets the default_template of this FsaSettingsSettings.
        Name of question template to use for new FSA jobs.

        :return: The default_template of this FsaSettingsSettings.
        :rtype: str
        """
        return self._default_template

    @default_template.setter
    def default_template(self, default_template):
        """
        Sets the default_template of this FsaSettingsSettings.
        Name of question template to use for new FSA jobs.

        :param default_template: The default_template of this FsaSettingsSettings.
        :type: str
        """
        self._default_template = default_template

    @property
    def disk_usage_depth(self):
        """
        Gets the disk_usage_depth of this FsaSettingsSettings.
        Maximum directory depth used for disk_usage question if not specified in the question.

        :return: The disk_usage_depth of this FsaSettingsSettings.
        :rtype: int
        """
        return self._disk_usage_depth

    @disk_usage_depth.setter
    def disk_usage_depth(self, disk_usage_depth):
        """
        Sets the disk_usage_depth of this FsaSettingsSettings.
        Maximum directory depth used for disk_usage question if not specified in the question.

        :param disk_usage_depth: The disk_usage_depth of this FsaSettingsSettings.
        :type: int
        """
        self._disk_usage_depth = disk_usage_depth

    @property
    def max_age(self):
        """
        Gets the max_age of this FsaSettingsSettings.
        Maximum age of non-pinned results in seconds.

        :return: The max_age of this FsaSettingsSettings.
        :rtype: int
        """
        return self._max_age

    @max_age.setter
    def max_age(self, max_age):
        """
        Sets the max_age of this FsaSettingsSettings.
        Maximum age of non-pinned results in seconds.

        :param max_age: The max_age of this FsaSettingsSettings.
        :type: int
        """
        self._max_age = max_age

    @property
    def max_count(self):
        """
        Gets the max_count of this FsaSettingsSettings.
        Maximum number of non-pinned result sets to keep.

        :return: The max_count of this FsaSettingsSettings.
        :rtype: int
        """
        return self._max_count

    @max_count.setter
    def max_count(self, max_count):
        """
        Sets the max_count of this FsaSettingsSettings.
        Maximum number of non-pinned result sets to keep.

        :param max_count: The max_count of this FsaSettingsSettings.
        :type: int
        """
        self._max_count = max_count

    @property
    def squash_depth(self):
        """
        Gets the squash_depth of this FsaSettingsSettings.
        Squash depth to use for squash binning questions if not specified in the question.

        :return: The squash_depth of this FsaSettingsSettings.
        :rtype: int
        """
        return self._squash_depth

    @squash_depth.setter
    def squash_depth(self, squash_depth):
        """
        Sets the squash_depth of this FsaSettingsSettings.
        Squash depth to use for squash binning questions if not specified in the question.

        :param squash_depth: The squash_depth of this FsaSettingsSettings.
        :type: int
        """
        self._squash_depth = squash_depth

    @property
    def top_n_max(self):
        """
        Gets the top_n_max of this FsaSettingsSettings.
        Maximum number of items in a Top-N question result if not specified in the question.

        :return: The top_n_max of this FsaSettingsSettings.
        :rtype: int
        """
        return self._top_n_max

    @top_n_max.setter
    def top_n_max(self, top_n_max):
        """
        Sets the top_n_max of this FsaSettingsSettings.
        Maximum number of items in a Top-N question result if not specified in the question.

        :param top_n_max: The top_n_max of this FsaSettingsSettings.
        :type: int
        """
        self._top_n_max = top_n_max

    @property
    def use_snapshot(self):
        """
        Gets the use_snapshot of this FsaSettingsSettings.
        If true, use a snapshot for consistency, otherwise analyze head.

        :return: The use_snapshot of this FsaSettingsSettings.
        :rtype: bool
        """
        return self._use_snapshot

    @use_snapshot.setter
    def use_snapshot(self, use_snapshot):
        """
        Sets the use_snapshot of this FsaSettingsSettings.
        If true, use a snapshot for consistency, otherwise analyze head.

        :param use_snapshot: The use_snapshot of this FsaSettingsSettings.
        :type: bool
        """
        self._use_snapshot = use_snapshot

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other
