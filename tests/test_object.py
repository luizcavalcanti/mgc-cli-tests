import time
from utils import run_cli

object_test_context = {}

bucket_name = "mgc-cli-tests-temp"


def test_objs_api_key_list():
    exit_code, _, stderr, jsonout = run_cli(["os", "api-key", "list"])
    assert exit_code == 0, stderr
    assert len(jsonout) > 0

    object_test_context["keys"] = jsonout


def test_objs_api_key_set():
    exit_code, _, stderr, _ = run_cli(
        ["os", "api-key", "set", object_test_context["keys"][0]["uuid"]]
    )
    assert exit_code == 0, stderr


def test_objs_buckets_create():
    exit_code, _, stderr, jsonout = run_cli(["os", "buckets", "create", bucket_name])
    assert exit_code == 0, stderr
    assert "bucket" in jsonout
    assert "bucket_is_prefix" in jsonout
    assert "enable_versioning" in jsonout


def test_objs_buckets_list():
    exit_code, _, stderr, jsonout = run_cli(["os", "buckets", "list"])
    assert exit_code == 0, stderr
    assert len(jsonout["Buckets"]) > 0


def test_objs_buckets_delete():
    exit_code, _, stderr, jsonout = run_cli(
        ["os", "buckets", "delete", f"--bucket={bucket_name}", "--no-confirm"]
    )
    assert exit_code == 0, stderr
