# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_mixed_reality_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_mixed_reality.vendored_sdks.mixedreality import MixedRealityClient
    return get_mgmt_service_client(cli_ctx,
                                   MixedRealityClient)


def cf_spatial_anchor_account(cli_ctx, *_):
    return cf_mixed_reality_cl(cli_ctx).spatial_anchor_account


def cf_remote_rendering_account(cli_ctx, *_):
    return cf_mixed_reality_cl(cli_ctx).remote_rendering_account
