import time
import uuid

from utils import run_cli

# ports           Operations related to Ports
# public-ips      Operations related to Public IPs
# rules           Operations related to Rules
# security-groups Operations related to Security Groups
# subnetpools     Operations related to Subnet Pools
# subnets         Operations related to Subnets
# vpcs            Operations related to VPCs

network_test_context = {}


def test_network_vpcs_list():
    exit_code, _, _, jsonout = run_cli(["network", "vpcs", "list"])
    assert exit_code == 0


def test_network_vpcs_create():
    exit_code, stdout, stderr, jsonout = run_cli(
        ["network", "vpcs", "create", f"--name=test-{uuid.uuid1()}"]
    )
    assert exit_code == 0
    assert jsonout["id"] is not None
    assert jsonout["status"] == "pending"

    network_test_context["vpc_id"] = jsonout["id"]


def test_network_vpcs_get():
    exit_code, _, _, jsonout = run_cli(
        ["network", "vpcs", "get", network_test_context["vpc_id"]]
    )
    assert exit_code == 0
    assert jsonout["id"] == network_test_context["vpc_id"]

    # Wait until VPC is not "processing" anymore
    while jsonout["status"] != "created":
        time.sleep(5)
        _, _, _, jsonout = run_cli(
            ["network", "vpcs", "get", network_test_context["vpc_id"]]
        )

def test_network_ports_list():
    exit_code, _, _, jsonout = run_cli(["network", "ports", "list"])
    assert exit_code == 0
    assert isinstance(jsonout, list)


def test_network_vpcs_delete():
    exit_code, _, _, _ = run_cli(
        ["network", "vpcs", "delete", network_test_context["vpc_id"], "--no-confirm"]
    )
    assert exit_code == 0
