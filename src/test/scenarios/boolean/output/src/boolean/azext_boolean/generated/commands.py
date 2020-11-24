# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_boolean.generated._client_factory import cf_bool
    bool_bool = CliCommandType(
        operations_tmpl='azext_boolean.vendored_sdks.boolean.operations._bool_operations#BoolOperations.{}',
        client_factory=cf_bool)
    with self.command_group('test-server bool', bool_bool, client_factory=cf_bool, is_experimental=True) as g:
        g.custom_command('put-false', 'test_server_bool_put_false')
        g.custom_command('put-true', 'test_server_bool_put_true')
        g.custom_command('show-false', 'test_server_bool_show_false')
        g.custom_command('show-invalid', 'test_server_bool_show_invalid')
        g.custom_command('show-null', 'test_server_bool_show_null')
        g.custom_command('show-true', 'test_server_bool_show_true')
