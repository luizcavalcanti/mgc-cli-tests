from utils import run_cli

def test_vm_images_list():
    exit_code, _, _, jsonout = run_cli(["vm", "images", "list"])
    assert exit_code == 0
    assert len(jsonout["images"]) > 0

def test_vm_machine_types_list():
    exit_code, _, _, jsonout = run_cli(["vm", "machine-types", "list"])
    assert exit_code == 0
    assert len(jsonout["machine_types"]) > 0

def test_vm_instances_list():
    exit_code, _, _, jsonout = run_cli(["vm", "instances", "list"])
    assert exit_code == 0
    assert "instances" in jsonout

def test_vm_snapshots_list():
    exit_code, _, _, jsonout = run_cli(["vm", "snapshots", "list"])
    assert exit_code == 0
    assert "snapshots" in jsonout
