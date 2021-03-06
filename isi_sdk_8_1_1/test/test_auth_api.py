# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_1_1
from isi_sdk_8_1_1.api.auth_api import AuthApi  # noqa: E501
from isi_sdk_8_1_1.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_1_1.api.auth_api.AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_auth_cache_item(self):
        """Test case for create_auth_cache_item

        """
        pass

    def test_create_auth_group(self):
        """Test case for create_auth_group

        """
        pass

    def test_create_auth_refresh_item(self):
        """Test case for create_auth_refresh_item

        """
        pass

    def test_create_auth_role(self):
        """Test case for create_auth_role

        """
        pass

    def test_create_auth_user(self):
        """Test case for create_auth_user

        """
        pass

    def test_create_mapping_identities(self):
        """Test case for create_mapping_identities

        """
        pass

    def test_create_mapping_identity(self):
        """Test case for create_mapping_identity

        """
        pass

    def test_create_providers_ads_item(self):
        """Test case for create_providers_ads_item

        """
        pass

    def test_create_providers_file_item(self):
        """Test case for create_providers_file_item

        """
        pass

    def test_create_providers_krb5_item(self):
        """Test case for create_providers_krb5_item

        """
        pass

    def test_create_providers_ldap_item(self):
        """Test case for create_providers_ldap_item

        """
        pass

    def test_create_providers_nis_item(self):
        """Test case for create_providers_nis_item

        """
        pass

    def test_create_settings_krb5_domain(self):
        """Test case for create_settings_krb5_domain

        """
        pass

    def test_create_settings_krb5_realm(self):
        """Test case for create_settings_krb5_realm

        """
        pass

    def test_delete_auth_group(self):
        """Test case for delete_auth_group

        """
        pass

    def test_delete_auth_groups(self):
        """Test case for delete_auth_groups

        """
        pass

    def test_delete_auth_role(self):
        """Test case for delete_auth_role

        """
        pass

    def test_delete_auth_user(self):
        """Test case for delete_auth_user

        """
        pass

    def test_delete_auth_users(self):
        """Test case for delete_auth_users

        """
        pass

    def test_delete_mapping_identities(self):
        """Test case for delete_mapping_identities

        """
        pass

    def test_delete_mapping_identity(self):
        """Test case for delete_mapping_identity

        """
        pass

    def test_delete_providers_ads_by_id(self):
        """Test case for delete_providers_ads_by_id

        """
        pass

    def test_delete_providers_file_by_id(self):
        """Test case for delete_providers_file_by_id

        """
        pass

    def test_delete_providers_krb5_by_id(self):
        """Test case for delete_providers_krb5_by_id

        """
        pass

    def test_delete_providers_ldap_by_id(self):
        """Test case for delete_providers_ldap_by_id

        """
        pass

    def test_delete_providers_local_by_id(self):
        """Test case for delete_providers_local_by_id

        """
        pass

    def test_delete_providers_nis_by_id(self):
        """Test case for delete_providers_nis_by_id

        """
        pass

    def test_delete_settings_krb5_domain(self):
        """Test case for delete_settings_krb5_domain

        """
        pass

    def test_delete_settings_krb5_realm(self):
        """Test case for delete_settings_krb5_realm

        """
        pass

    def test_get_auth_access_user(self):
        """Test case for get_auth_access_user

        """
        pass

    def test_get_auth_group(self):
        """Test case for get_auth_group

        """
        pass

    def test_get_auth_id(self):
        """Test case for get_auth_id

        """
        pass

    def test_get_auth_ldap_template(self):
        """Test case for get_auth_ldap_template

        """
        pass

    def test_get_auth_ldap_templates(self):
        """Test case for get_auth_ldap_templates

        """
        pass

    def test_get_auth_log_level(self):
        """Test case for get_auth_log_level

        """
        pass

    def test_get_auth_netgroup(self):
        """Test case for get_auth_netgroup

        """
        pass

    def test_get_auth_privileges(self):
        """Test case for get_auth_privileges

        """
        pass

    def test_get_auth_role(self):
        """Test case for get_auth_role

        """
        pass

    def test_get_auth_shells(self):
        """Test case for get_auth_shells

        """
        pass

    def test_get_auth_user(self):
        """Test case for get_auth_user

        """
        pass

    def test_get_auth_wellknown(self):
        """Test case for get_auth_wellknown

        """
        pass

    def test_get_auth_wellknowns(self):
        """Test case for get_auth_wellknowns

        """
        pass

    def test_get_mapping_dump(self):
        """Test case for get_mapping_dump

        """
        pass

    def test_get_mapping_identity(self):
        """Test case for get_mapping_identity

        """
        pass

    def test_get_mapping_users_lookup(self):
        """Test case for get_mapping_users_lookup

        """
        pass

    def test_get_mapping_users_rules(self):
        """Test case for get_mapping_users_rules

        """
        pass

    def test_get_providers_ads_by_id(self):
        """Test case for get_providers_ads_by_id

        """
        pass

    def test_get_providers_file_by_id(self):
        """Test case for get_providers_file_by_id

        """
        pass

    def test_get_providers_krb5_by_id(self):
        """Test case for get_providers_krb5_by_id

        """
        pass

    def test_get_providers_ldap_by_id(self):
        """Test case for get_providers_ldap_by_id

        """
        pass

    def test_get_providers_local(self):
        """Test case for get_providers_local

        """
        pass

    def test_get_providers_local_by_id(self):
        """Test case for get_providers_local_by_id

        """
        pass

    def test_get_providers_nis_by_id(self):
        """Test case for get_providers_nis_by_id

        """
        pass

    def test_get_providers_summary(self):
        """Test case for get_providers_summary

        """
        pass

    def test_get_settings_acls(self):
        """Test case for get_settings_acls

        """
        pass

    def test_get_settings_global(self):
        """Test case for get_settings_global

        """
        pass

    def test_get_settings_krb5_defaults(self):
        """Test case for get_settings_krb5_defaults

        """
        pass

    def test_get_settings_krb5_domain(self):
        """Test case for get_settings_krb5_domain

        """
        pass

    def test_get_settings_krb5_realm(self):
        """Test case for get_settings_krb5_realm

        """
        pass

    def test_get_settings_mapping(self):
        """Test case for get_settings_mapping

        """
        pass

    def test_list_auth_groups(self):
        """Test case for list_auth_groups

        """
        pass

    def test_list_auth_roles(self):
        """Test case for list_auth_roles

        """
        pass

    def test_list_auth_users(self):
        """Test case for list_auth_users

        """
        pass

    def test_list_providers_ads(self):
        """Test case for list_providers_ads

        """
        pass

    def test_list_providers_file(self):
        """Test case for list_providers_file

        """
        pass

    def test_list_providers_krb5(self):
        """Test case for list_providers_krb5

        """
        pass

    def test_list_providers_ldap(self):
        """Test case for list_providers_ldap

        """
        pass

    def test_list_providers_nis(self):
        """Test case for list_providers_nis

        """
        pass

    def test_list_settings_krb5_domains(self):
        """Test case for list_settings_krb5_domains

        """
        pass

    def test_list_settings_krb5_realms(self):
        """Test case for list_settings_krb5_realms

        """
        pass

    def test_update_auth_group(self):
        """Test case for update_auth_group

        """
        pass

    def test_update_auth_log_level(self):
        """Test case for update_auth_log_level

        """
        pass

    def test_update_auth_role(self):
        """Test case for update_auth_role

        """
        pass

    def test_update_auth_user(self):
        """Test case for update_auth_user

        """
        pass

    def test_update_mapping_import(self):
        """Test case for update_mapping_import

        """
        pass

    def test_update_mapping_users_rules(self):
        """Test case for update_mapping_users_rules

        """
        pass

    def test_update_providers_ads_by_id(self):
        """Test case for update_providers_ads_by_id

        """
        pass

    def test_update_providers_file_by_id(self):
        """Test case for update_providers_file_by_id

        """
        pass

    def test_update_providers_krb5_by_id(self):
        """Test case for update_providers_krb5_by_id

        """
        pass

    def test_update_providers_ldap_by_id(self):
        """Test case for update_providers_ldap_by_id

        """
        pass

    def test_update_providers_local_by_id(self):
        """Test case for update_providers_local_by_id

        """
        pass

    def test_update_providers_nis_by_id(self):
        """Test case for update_providers_nis_by_id

        """
        pass

    def test_update_settings_acls(self):
        """Test case for update_settings_acls

        """
        pass

    def test_update_settings_global(self):
        """Test case for update_settings_global

        """
        pass

    def test_update_settings_krb5_defaults(self):
        """Test case for update_settings_krb5_defaults

        """
        pass

    def test_update_settings_krb5_domain(self):
        """Test case for update_settings_krb5_domain

        """
        pass

    def test_update_settings_krb5_realm(self):
        """Test case for update_settings_krb5_realm

        """
        pass

    def test_update_settings_mapping(self):
        """Test case for update_settings_mapping

        """
        pass


if __name__ == '__main__':
    unittest.main()
