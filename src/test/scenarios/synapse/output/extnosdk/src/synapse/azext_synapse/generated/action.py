# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddAutoScale(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.auto_scale = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'min-node-count':
                d['min_node_count'] = v[0]
            elif kl == 'enabled':
                d['enabled'] = v[0]
            elif kl == 'max-node-count':
                d['max_node_count'] = v[0]
            else:
                raise CLIError('usage error: {} [WRONG KEY] You only have the following keys to use : min-node-count, enabled, max-node-count. And your key : '.format(option_string) + kl + ' is invalid')
        return d


class AddAutoPause(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.auto_pause = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'delay-in-minutes':
                d['delay_in_minutes'] = v[0]
            elif kl == 'enabled':
                d['enabled'] = v[0]
            else:
                raise CLIError('usage error: {} [WRONG KEY] You only have the following keys to use : delay-in-minutes, enabled. And your key : '.format(option_string) + kl + ' is invalid')
        return d


class AddLibraryRequirements(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.library_requirements = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'content':
                d['content'] = v[0]
            elif kl == 'filename':
                d['filename'] = v[0]
            else:
                raise CLIError('usage error: {} [WRONG KEY] You only have the following keys to use : content, filename. And your key : '.format(option_string) + kl + ' is invalid')
        return d


class AddSku(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.sku = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'tier':
                d['tier'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            else:
                raise CLIError('usage error: {} [WRONG KEY] You only have the following keys to use : tier, name. And your key : '.format(option_string) + kl + ' is invalid')
        return d


class AddRecurringScans(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.recurring_scans = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        d['email_subscription_admins'] = True
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'is-enabled':
                d['is_enabled'] = v[0]
            elif kl == 'email-subscription-admins':
                d['email_subscription_admins'] = v[0]
            elif kl == 'emails':
                d['emails'] = v
            else:
                raise CLIError('usage error: {} [WRONG KEY] You only have the following keys to use : is-enabled, email-subscription-admins, emails. And your key : '.format(option_string) + kl + ' is invalid')
        return d


class AddBaselineResults(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddBaselineResults, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'result':
                d['result'] = v
            else:
                raise CLIError('usage error: {} [WRONG KEY] You only have the following keys to use : result. And your key : '.format(option_string) + kl + ' is invalid')
        return d


class AddDefaultDataLakeStorage(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.default_data_lake_storage = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'account-url':
                d['account_url'] = v[0]
            elif kl == 'filesystem':
                d['filesystem'] = v[0]
            else:
                raise CLIError('usage error: {} [WRONG KEY] You only have the following keys to use : account-url, filesystem. And your key : '.format(option_string) + kl + ' is invalid')
        return d


class AddConnectivityEndpoints(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.connectivity_endpoints = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            v = properties[k]
            d[k] = v[0]
        return d


class AddPrivateEndpointConnections(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddPrivateEndpointConnections, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'status':
                d['status'] = v[0]
            elif kl == 'description':
                d['description'] = v[0]
            else:
                raise CLIError('usage error: {} [WRONG KEY] You only have the following keys to use : status, description. And your key : '.format(option_string) + kl + ' is invalid')
        return d
