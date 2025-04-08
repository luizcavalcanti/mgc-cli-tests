from utils import run_cli

test_config_context = {}


def test_config_list():
    exit_code, _, _, jsonout = run_cli(["config", "list"])
    assert exit_code == 0
    assert "chunkSize" in jsonout
    assert "defaultOutput" in jsonout
    assert "region" in jsonout
    assert "workers" in jsonout
    assert "x-zone" in jsonout


def test_config_get_schema():
    exit_code, _, stderr, jsonout = run_cli(["config", "get-schema", "env"])
    assert exit_code == 0, stderr
    assert jsonout["default"] == "prod"

    exit_code, _, stderr, jsonout = run_cli(["config", "get-schema", "defaultOutput"])
    assert exit_code == 0, stderr
    assert "default" not in jsonout


def test_config_set():
    exit_code, _, stderr, _ = run_cli(["config", "set", "workers", "999"])
    assert exit_code == 0, stderr


def test_config_get():
    exit_code, _, stderr, jsonout = run_cli(["config", "get", "workers"])
    assert exit_code == 0, stderr
    assert jsonout == 999


def test_config_delete():
    exit_code, _, stderr, jsonout = run_cli(["config", "delete", "workers"])
    assert exit_code == 0, stderr

    exit_code, _, stderr, jsonout = run_cli(["config", "get", "workers"])
    assert exit_code == 0, stderr
    assert jsonout == {}
