# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.testsdk import ScenarioTest


# Test class for Scenario
class PositiveTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(PositiveTest, self).__init__(*args, **kwargs)

    def test_create_provider(self):
        # From /Operation/put/AttestationProviders_Create
        self.cmd('az attestation create-provider '
                 '--provider-name "myattestationprovider" '
                 '--resource-group "MyResourceGroup"')

        # From /Operation/put/AttestationProviders_Create_MaximumSet_Gen
        self.cmd('az attestation create-provider '
                 '--provider-name "myattestationprovider" '
                 '--resource-group "MyResourceGroup"')

        # From /Operation/put/AttestationProviders_Create_MinimumSet_Gen
        self.cmd('az attestation create-provider '
                 '--resource-group "MyResourceGroup"')

    def test_list_operation(self):
        # From /Operation/get/Operations_List
        self.cmd('az attestation list-operation')

    def test_attestation_provider_provider_list(self):
        # From /AttestationProviders/get/AttestationProviders_ListByResourceGroup
        self.cmd('az attestation attestation-provider provider list '
                 '--resource-group "testrg1"')

    def test_attestation_provider_provider_list2(self):
        # From /AttestationProviders/get/AttestationProviders_List
        self.cmd('az attestation attestation-provider provider list')

    def test_attestation_provider_show(self):
        # From /AttestationProviders/get/AttestationProviders_Get
        self.cmd('az attestation attestation-provider show '
                 '--provider-name "myattestationprovider" '
                 '--resource-group "MyResourceGroup"')

    def test_attestation_provider_update(self):
        # From /AttestationProviders/patch/AttestationProviders_Update
        self.cmd('az attestation attestation-provider update '
                 '--provider-name "myattestationprovider" '
                 '--resource-group "MyResourceGroup" '
                 '--tags Property1="Value1" Property2="Value2" Property3="Value3"')

    def test_attestation_provider_delete(self):
        # From /AttestationProviders/delete/AttestationProviders_Delete
        self.cmd('az attestation attestation-provider delete -y '
                 '--provider-name "myattestationprovider" '
                 '--resource-group "sample-resource-group"')
