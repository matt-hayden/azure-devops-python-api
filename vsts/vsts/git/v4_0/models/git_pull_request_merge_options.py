# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class GitPullRequestMergeOptions(Model):
    """GitPullRequestMergeOptions.

    :param disable_renames:
    :type disable_renames: bool
    """

    _attribute_map = {
        'disable_renames': {'key': 'disableRenames', 'type': 'bool'}
    }

    def __init__(self, disable_renames=None):
        super(GitPullRequestMergeOptions, self).__init__()
        self.disable_renames = disable_renames
