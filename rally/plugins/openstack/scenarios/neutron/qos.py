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


class NeutronQosPolicy(utils.NeutronScenario):
    """Benchmark scenarios for Neutron Qos Policies."""

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def create_and_list_qos_policies(self, qos_policy_create_args=None):
        """Create and list Neutron qos-policies.

        Measure the "neutron qos-policy-create" and "neutron
        qos-policy-list" command performance.

        :param qos_policy_create_args: dict, POST /v2.0/qos/policies
                                           request options
        """
        qos_policy_create_args = qos_policy_create_args or {}
        self._create_qos_policy(**qos_policy_create_args)
        self._list_qos_policies()

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def create_and_delete_qos_policies(self, qos_policy_create_args=None):
        """Create and delete Neutron qos-policies.

        Measure the "neutron qos-policy-create" and "neutron
        qos-policy-delete" command performance.

        :param qos_policy_create_args: dict, POST /v2.0/qos-policies
                                           request options
        """
        qos_policy_create_args = qos_policy_create_args or {}
        qos_policy = self._create_qos_policy(
            **qos_policy_create_args)
        self._delete_qos_policy(qos_policy)

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def create_and_update_qos_policies(self,
                                       qos_policy_create_args=None,
                                       qos_policy_update_args=None):
        """Create and update Neutron qos-policies.

        Measure the "neutron qos-policy-create" and "neutron
        qos_policy-update" command performance.

        :param qos_policy_create_args: dict, POST /v2.0/qos-policies
                                           request options
        :param qos_policy_update_args: dict, PUT /v2.0/qos-policies
                                           update options
        """
        qos_policy_create_args = qos_policy_create_args or {}
        qos_policy_update_args = qos_policy_update_args or {}
        qos_policy = self._create_qos_policy(
            **qos_policy_create_args)
        self._update_qos_policy(qos_policy,
                                **qos_policy_update_args)
