#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from rally import consts
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.neutron import utils
from rally.task import validation


class NeutronFirewall(utils.NeutronScenario):
    """Benchmark scenarios for Neutron Firewall."""

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def create_and_list_firewall_policies(self, firewall_policy_create_args=None):
        """Create and list Neutron firewall-policies.

        Measure the "neutron firewall-policy-create" and "neutron
        firewall-policy-list" command performance.

        :param firewall_policy_create_args: dict, POST /v2.0/fw/firewall_policies
                                           request options
        """
        firewall_policy_create_args = firewall_policy_create_args or {}
        self._create_firewall_policy(**firewall_policy_create_args)
        self._list_firewall_policies()

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def create_and_delete_firewall_policies(self, firewall_policy_create_args=None):
        """Create and delete Neutron firewall-policies.

        Measure the "neutron firewall-policy-create" and "neutron
        firewall-policy-delete" command performance.

        :param firewall_policy_create_args: dict, POST /v2.0/fw/firewall_policies
                                           request options
        """
        firewall_policy_create_args = firewall_policy_create_args or {}
        firewall_policy = self._create_firewall_policy(
            **firewall_policy_create_args)
        self._delete_firewall_policy(firewall_policy)

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def create_and_update_firewall_policies(self,
                                            firewall_policy_create_args=None,
                                            firewall_policy_update_args=None):
        """Create and update Neutron firewall-policies.

        Measure the "neutron firewall-policy-create" and "neutron
        firewall-policy-update" command performance.

        :param firewall_policy_create_args: dict, POST /v2.0/firewall-policies
                                           request options
        :param firewall_policy_update_args: dict, PUT /v2.0/firewall-policies
                                           update options
        """
        firewall_policy_create_args = firewall_policy_create_args or {}
        firewall_policy_update_args = firewall_policy_update_args or {}
        firewall_policy = self._create_firewall_policy(
            **firewall_policy_create_args)
        self._update_firewall_policy(firewall_policy,
                                     **firewall_policy_update_args)

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def create_and_list_firewalls(self, firewall_policy_create_args=None,
                                  firewall_create_args=None):
        """Create a firewall and then list firewall.

        Measure the "neutron firewall-create" and "neutron firewall-list" command
        performance. The scenario creates a firewall for every firewall-policy created and
        then lists firewalls.

        :param firewall_create_args: dict, POST /fw/firewalls request options
        :param firewall_policy_create_args: dict, POST /fw/firewall-policies request options
        """
        firewall_create_args = firewall_create_args or {}
        firewall_policy_create_args = firewall_policy_create_args or {}
        firewall_policy = self._create_firewall_policy(**firewall_policy_create_args)
        self._create_firewall(firewall_policy, **firewall_create_args)
        self._list_firewalls()

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def create_and_delete_firewalls(self, firewall_policy_create_args=None,
                                    firewall_create_args=None):
        """Create a firewall and then delete firewalls.

        Measure the "neutron firewall-create" and "neutron firewall-delete"
        command performance. The scenario creates a firewall for firewall-policy and
        then deletes those firewalls.

        :param firewall_policy_create_args: dict, POST /fw/firewall-policies request options
        :param firewall_create_args: dict, POST /fw/firewalls request options
        """
        firewall_policy_create_args = firewall_policy_create_args or {}
        firewall_create_args = firewall_create_args or {}
        firewall_policy = self._create_firewall_policy(**firewall_policy_create_args)
        firewall = self._create_firewall(firewall_policy, **firewall_create_args)
        self._delete_firewall(firewall)

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def create_and_update_firewalls(self, firewall_policy_create_args=None,
                                    firewall_update_args=None,
                                    firewall_create_args=None):
        """Create firewalls and update firewalls.

        Measure the "neutron firewall-create" and "neutron firewall-update"
        command performance. The scenario creates a firewall-policy for every firewall
        and then update those firewalls.

        :param firewall_policy_create_args: dict, POST /fw/firewall-policies request options
        :param firewall_create_args: dict, POST /fw/firewalls request options
        :param firewall_update_args: dict, POST /fw/firewalls update options
        """
        firewall_policy_create_args = firewall_policy_create_args or {}
        firewall_create_args = firewall_create_args or {}
        firewall_update_args = firewall_update_args or {}
        firewall_policy = self._create_firewall_policy(**firewall_policy_create_args)
        firewall = self._create_firewall(firewall_policy, **firewall_create_args)
        self._update_firewall(firewall, **firewall_update_args)

