from typer.testing import CliRunner
from todo_cli.main import app, DATA
import json, os, tempfile

runner = CliRunner()

def test_add_and_done(tmp_path, monkeypatch):
    monkeypatch.setattr("todo_cli.main.DATA", tmp_path/"data.json")
    assert runner.invoke(app, ["add", "test"]).exit_code == 0
    assert runner.invoke(app, ["done", "1"]).exit_code == 0
    tasks = json.loads((tmp_path/"data.json").read_text())
    assert tasks[0]["done"] is True
