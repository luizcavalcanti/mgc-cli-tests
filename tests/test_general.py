from utils import run_cli

def test_general_version():
    exit_code, stdout, _, _ = run_cli(["--version"])
    assert exit_code == 0
    assert "mgc version v" in stdout
