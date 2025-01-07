from utils import run_cli

test_workspace_context = {}


def test_workspace_list():
    exit_code, _, _, jsonout = run_cli(["workspace", "list"])
    assert exit_code == 0
    assert isinstance(jsonout, list)
    assert len(jsonout) > 0
    
    if len(jsonout) == 1:
        assert jsonout[0]["name"] == "default"

    test_workspace_context["initial_count"] = len(jsonout)

def test_workspace_create():
    exit_code, _, _, jsonout = run_cli(["workspace", "create", "test-workspace"])
    assert exit_code == 0
    assert jsonout["name"] == "test-workspace"

def test_workspace_set():
    exit_code, _, _, jsonout = run_cli(["workspace", "set", "test-workspace"])
    assert exit_code == 0
    assert jsonout["name"] == "test-workspace"

def test_workspace_get():
    exit_code, _, _, jsonout = run_cli(["workspace", "get"])
    assert exit_code == 0
    assert jsonout["name"] == "test-workspace"

def test_workspace_delete_fails_on_current_profile():
    exit_code, _, _, jsonout = run_cli(["workspace", "delete", "test-workspace", "--no-confirm"])
    assert exit_code == 1

def test_workspace_delete():
    exit_code, _, _, _ = run_cli(["workspace", "set", "default"])
    assert exit_code == 0
    
    exit_code, _, _, jsonout = run_cli(["workspace", "delete", "test-workspace", "--no-confirm"])
    assert exit_code == 0
    assert jsonout["name"] == "test-workspace"

    exit_code, _, _, jsonout = run_cli(["workspace", "list"]) 
    assert exit_code == 0
    assert len(jsonout) == test_workspace_context["initial_count"]
