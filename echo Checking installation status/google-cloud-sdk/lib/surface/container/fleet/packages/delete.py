# -*- coding: utf-8 -*- #
# Copyright 2024 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command to delete a Fleet Package."""

from googlecloudsdk.api_lib.container.fleet.packages import fleet_packages as apis
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.container.fleet.packages import flags
from googlecloudsdk.command_lib.util.concepts import concept_parsers

_DETAILED_HELP = {
    'DESCRIPTION': '{description}',
    'EXAMPLES': """ \
        To delete Fleet Package `cert-manager-app` in `us-central1`, run:

          $ {command} cert-manager-app --location=us-central1
        """,
}


@base.DefaultUniverseOnly
@base.ReleaseTracks(base.ReleaseTrack.BETA)
class Delete(base.DeleteCommand):
  """Delete Package Rollouts Fleet Package."""

  detailed_help = _DETAILED_HELP
  _api_version = 'v1beta'

  @staticmethod
  def Args(parser):
    flags.AddForceDeleteFlag(parser, 'Fleet Package')
    concept_parsers.ConceptParser.ForResource(
        'fleet_package',
        flags.GetFleetPackageResourceSpec(),
        'The Fleet Package to create.',
        required=True,
        prefixes=False,
    ).AddToParser(parser)

  def Run(self, args):
    """Run the delete command."""
    client = apis.FleetPackagesClient(self._api_version)
    return client.Delete(
        project=flags.GetProject(args),
        location=flags.GetLocation(args),
        name=args.fleet_package,
        force=args.force,
    )


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class DeleteAlpha(Delete):
  """Delete Package Rollouts Fleet Package."""

  _api_version = 'v1alpha'
