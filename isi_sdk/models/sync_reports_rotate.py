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


class SyncReportsRotate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SyncReportsRotate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str',
            'running': 'bool'
        }

        self.attribute_map = {
            'message': 'message',
            'running': 'running'
        }

        self._message = None
        self._running = None

    @property
    def message(self):
        """
        Gets the message of this SyncReportsRotate.
        A message about the status of the task.

        :return: The message of this SyncReportsRotate.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this SyncReportsRotate.
        A message about the status of the task.

        :param message: The message of this SyncReportsRotate.
        :type: str
        """
        self._message = message

    @property
    def running(self):
        """
        Gets the running of this SyncReportsRotate.
        Whether this task is running or not.

        :return: The running of this SyncReportsRotate.
        :rtype: bool
        """
        return self._running

    @running.setter
    def running(self, running):
        """
        Sets the running of this SyncReportsRotate.
        Whether this task is running or not.

        :param running: The running of this SyncReportsRotate.
        :type: bool
        """
        self._running = running

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
