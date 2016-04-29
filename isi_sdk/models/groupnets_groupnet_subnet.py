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


class GroupnetsGroupnetSubnet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        GroupnetsGroupnetSubnet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'dsr_addrs': 'list[str]',
            'gateway': 'str',
            'gateway_priority': 'int',
            'mtu': 'int',
            'name': 'str',
            'prefixlen': 'int',
            'sc_service_addr': 'str',
            'vlan_enabled': 'bool',
            'vlan_id': 'int'
        }

        self.attribute_map = {
            'description': 'description',
            'dsr_addrs': 'dsr_addrs',
            'gateway': 'gateway',
            'gateway_priority': 'gateway_priority',
            'mtu': 'mtu',
            'name': 'name',
            'prefixlen': 'prefixlen',
            'sc_service_addr': 'sc_service_addr',
            'vlan_enabled': 'vlan_enabled',
            'vlan_id': 'vlan_id'
        }

        self._description = None
        self._dsr_addrs = None
        self._gateway = None
        self._gateway_priority = None
        self._mtu = None
        self._name = None
        self._prefixlen = None
        self._sc_service_addr = None
        self._vlan_enabled = None
        self._vlan_id = None

    @property
    def description(self):
        """
        Gets the description of this GroupnetsGroupnetSubnet.
        A description of the subnet.

        :return: The description of this GroupnetsGroupnetSubnet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GroupnetsGroupnetSubnet.
        A description of the subnet.

        :param description: The description of this GroupnetsGroupnetSubnet.
        :type: str
        """
        self._description = description

    @property
    def dsr_addrs(self):
        """
        Gets the dsr_addrs of this GroupnetsGroupnetSubnet.
        List of Direct Server Return addresses.

        :return: The dsr_addrs of this GroupnetsGroupnetSubnet.
        :rtype: list[str]
        """
        return self._dsr_addrs

    @dsr_addrs.setter
    def dsr_addrs(self, dsr_addrs):
        """
        Sets the dsr_addrs of this GroupnetsGroupnetSubnet.
        List of Direct Server Return addresses.

        :param dsr_addrs: The dsr_addrs of this GroupnetsGroupnetSubnet.
        :type: list[str]
        """
        self._dsr_addrs = dsr_addrs

    @property
    def gateway(self):
        """
        Gets the gateway of this GroupnetsGroupnetSubnet.
        Gateway IP address.

        :return: The gateway of this GroupnetsGroupnetSubnet.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this GroupnetsGroupnetSubnet.
        Gateway IP address.

        :param gateway: The gateway of this GroupnetsGroupnetSubnet.
        :type: str
        """
        self._gateway = gateway

    @property
    def gateway_priority(self):
        """
        Gets the gateway_priority of this GroupnetsGroupnetSubnet.
        Gateway priority.

        :return: The gateway_priority of this GroupnetsGroupnetSubnet.
        :rtype: int
        """
        return self._gateway_priority

    @gateway_priority.setter
    def gateway_priority(self, gateway_priority):
        """
        Sets the gateway_priority of this GroupnetsGroupnetSubnet.
        Gateway priority.

        :param gateway_priority: The gateway_priority of this GroupnetsGroupnetSubnet.
        :type: int
        """
        self._gateway_priority = gateway_priority

    @property
    def mtu(self):
        """
        Gets the mtu of this GroupnetsGroupnetSubnet.
        MTU of the subnet.

        :return: The mtu of this GroupnetsGroupnetSubnet.
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """
        Sets the mtu of this GroupnetsGroupnetSubnet.
        MTU of the subnet.

        :param mtu: The mtu of this GroupnetsGroupnetSubnet.
        :type: int
        """
        self._mtu = mtu

    @property
    def name(self):
        """
        Gets the name of this GroupnetsGroupnetSubnet.
        The name of the subnet.

        :return: The name of this GroupnetsGroupnetSubnet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GroupnetsGroupnetSubnet.
        The name of the subnet.

        :param name: The name of this GroupnetsGroupnetSubnet.
        :type: str
        """
        self._name = name

    @property
    def prefixlen(self):
        """
        Gets the prefixlen of this GroupnetsGroupnetSubnet.
        Subnet Prefix Length.

        :return: The prefixlen of this GroupnetsGroupnetSubnet.
        :rtype: int
        """
        return self._prefixlen

    @prefixlen.setter
    def prefixlen(self, prefixlen):
        """
        Sets the prefixlen of this GroupnetsGroupnetSubnet.
        Subnet Prefix Length.

        :param prefixlen: The prefixlen of this GroupnetsGroupnetSubnet.
        :type: int
        """
        self._prefixlen = prefixlen

    @property
    def sc_service_addr(self):
        """
        Gets the sc_service_addr of this GroupnetsGroupnetSubnet.
        The address that SmartConnect listens for DNS requests.

        :return: The sc_service_addr of this GroupnetsGroupnetSubnet.
        :rtype: str
        """
        return self._sc_service_addr

    @sc_service_addr.setter
    def sc_service_addr(self, sc_service_addr):
        """
        Sets the sc_service_addr of this GroupnetsGroupnetSubnet.
        The address that SmartConnect listens for DNS requests.

        :param sc_service_addr: The sc_service_addr of this GroupnetsGroupnetSubnet.
        :type: str
        """
        self._sc_service_addr = sc_service_addr

    @property
    def vlan_enabled(self):
        """
        Gets the vlan_enabled of this GroupnetsGroupnetSubnet.
        VLAN tagging enabled or disabled.

        :return: The vlan_enabled of this GroupnetsGroupnetSubnet.
        :rtype: bool
        """
        return self._vlan_enabled

    @vlan_enabled.setter
    def vlan_enabled(self, vlan_enabled):
        """
        Sets the vlan_enabled of this GroupnetsGroupnetSubnet.
        VLAN tagging enabled or disabled.

        :param vlan_enabled: The vlan_enabled of this GroupnetsGroupnetSubnet.
        :type: bool
        """
        self._vlan_enabled = vlan_enabled

    @property
    def vlan_id(self):
        """
        Gets the vlan_id of this GroupnetsGroupnetSubnet.
        VLAN ID for all interfaces in the subnet.

        :return: The vlan_id of this GroupnetsGroupnetSubnet.
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """
        Sets the vlan_id of this GroupnetsGroupnetSubnet.
        VLAN ID for all interfaces in the subnet.

        :param vlan_id: The vlan_id of this GroupnetsGroupnetSubnet.
        :type: int
        """
        self._vlan_id = vlan_id

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
