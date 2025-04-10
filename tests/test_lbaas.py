import time

from utils import run_cli

lbaas_test_context = {}


def _get_nlb(nlb_id):
    return run_cli(["lb", "network-loadbalancers", "get", nlb_id])


def _get_default_vpc():
    _, _, _, jsonout = run_cli(["network", "vpcs", "list"])
    for vpc in jsonout["vpcs"]:
        if vpc["is_default"]:
            return vpc["id"]
    return "no-default-vpc-found"


def test_lb_network_loadbalancers_create():
    exit_code, _, stderr, jsonout = run_cli(
        [
            "lb",
            "network-loadbalancers",
            "create",
            "--name=nlb-test",
            "--visibility=internal",
            f"--vpc-id={_get_default_vpc()}",
            '--backends=[{"balance_algorithm":"round_robin","description":"Some optional backend description 1","health_check_name":"nlb-health-check-1","name":"nlb-backend-1","targets_type":"instance"}]',
            '--listeners=[{"backend_name":"nlb-backend-1","name":"nlb-listener-1","port":80,"protocol":"tcp"}]',
        ]
    )
    assert exit_code == 0, stderr
    assert "id" in jsonout

    lbaas_test_context["nlb_id"] = jsonout["id"]

    # Wait until vm creation is over (hoping it will be)
    _, _, _, jsonout = _get_nlb(lbaas_test_context["nlb_id"])
    while jsonout["status"] not in ["running"]:
        time.sleep(5)
        _, _, _, jsonout = _get_nlb(lbaas_test_context["nlb_id"])

    assert jsonout["status"] == "running"


def test_lb_network_loadbalancers_get():
    exit_code, _, stderr, jsonout = _get_nlb(lbaas_test_context["nlb_id"])

    assert exit_code == 0, stderr

    assert "id" in jsonout
    assert "backends" in jsonout
    assert "description" in jsonout
    assert "health_checks" in jsonout
    assert "ip_address" in jsonout
    assert "listeners" in jsonout
    assert "port" in jsonout
    assert "public_ips" in jsonout
    assert "status" in jsonout
    assert "type" in jsonout
    assert "visibility" in jsonout


def test_lb_network_loadbalancers_list():
    exit_code, _, stderr, jsonout = run_cli(["lb", "network-loadbalancers", "list"])
    assert exit_code == 0, stderr
    assert "meta" in jsonout
    assert "results" in jsonout
    assert len(jsonout["results"]) > 0


def test_lb_network_loadbalancers_delete():
    exit_code, _, stderr, _ = run_cli(
        [
            "lb",
            "network-loadbalancers",
            "delete",
            lbaas_test_context["nlb_id"],
            "--no-confirm",
        ]
    )
    assert exit_code == 0, stderr
