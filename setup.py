# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 4
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "isi-sdk-8-0-1"
VERSION = "0.2.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Isilon SDK",
    author_email="sdk@isilon.com",
    url="",
    keywords=["Swagger", "Isilon SDK"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
About
-----

This package is part of the Isilon SDK. It includes language bindings
for easier programmatic access to the OneFS API for cluster
configuration (on your cluster this is the REST API made up of all the
URIs underneath ``https://[cluster]:8080/platform/*``, also called the
"Platform API" or "PAPI").

Installation
------------

``pip install PKG_NAME``

Documentation
-------------

The SDK documentation is auto generated by Swagger Codegen and is
located in the
`isilon\_sdk\_python <https://github.com/Isilon/isilon_sdk_python>`__
repository. Please select the repository branch that is applicable to
the SDK package and OneFS version for accurate documentation references.
All SDK methods and models are linked from the top level README file.

Example program
---------------

Here's an example of using the Python PAPI bindings to retrieve a list
of NFS exports from your cluster:

.. code:: python

    from pprint import pprint
    import urllib3

    import PKG_NAME
    from PKG_NAME.rest import ApiException

    urllib3.disable_warnings()

    # configure username and password
    configuration = PKG_NAME.Configuration()
    configuration.username = "YOUR_USERNAME"
    configuration.password = "YOUR_PASSWORD"
    configuration.verify_ssl = False

    # configure host
    configuration.host = "https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080"
    api_client = PKG_NAME.ApiClient(configuration)
    protocols_api = PKG_NAME.ProtocolsApi(api_client)

    # get all exports
    sort = "description"
    limit = 50
    dir = "ASC"
    try:
        api_response = protocols_api.list_nfs_exports(sort=sort, limit=limit, dir=dir)
        pprint(api_response)
    except ApiException as e:
        print "Exception when calling ProtocolsApi->list_nfs_exports: %s" % e

There are more examples of coding to the Python PAPI bindings in the
`tests <https://github.com/Isilon/isilon_sdk/tree/master/tests>`__
subdirectory of the repo. The tests currently run against a generic
``isi_sdk`` import which is how the bindings library is named by default
if you build your own bindings. If you want to run the tests against one
of the libraries you've downloaded from the prebuilt releases page, you
should change the ``import isi_sdk`` lines to ``import isi_sdk_7_2`` or
``import isi_sdk_8_0`` depending on which one you downloaded.

More info
---------

See the Github repo for more information:
https://github.com/isilon/isilon_sdk

""".replace('PKG_NAME', NAME.replace('-', '_'))
)
