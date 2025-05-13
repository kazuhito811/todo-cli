import json, pathlib, datetime; import typer
app = typer.Typer()
DATA = pathlib.Path.home() / ".todo_cli.json"

def _load(): return json.loads(DATA.read_text()) if DATA.exists() else []

def _save(tasks): DATA.write_text(json.dumps(tasks, ensure_ascii=False, indent=2))

@app.command()
def add(task: str):
    tasks = _load(); tasks.append({"task": task, "done": False,
                                   "created": datetime.datetime.now().isoformat()})
    _save(tasks); typer.echo(f"✓ 追加: {len(tasks)}. {task}")

@app.command()
def list():
    for i, t in enumerate(_load(), 1):
        created = t["created"][:16].replace("T", " ")
        typer.echo(f"{i}. [{'x' if t['done'] else ' '}] {t['task']} ({created})")

@app.command()
def done(number: int):
    tasks = _load()
    try:
        tasks[number-1]["done"] = True; _save(tasks)
        typer.secho(f"✓ 完了: {number}. {tasks[number-1]['task']}", fg=typer.colors.GREEN)
    except IndexError:
        typer.secho("番号がありません", fg=typer.colors.RED, err=True)

if __name__ == "__main__":
    app()
