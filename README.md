# 📝 todo-cli — Simple To-Do Manager for the terminal  

![CI](https://github.com/kazuhito0811/todo-cli/actions/workflows/python.yml/badge.svg)
<!-- PyPI に公開したら下のバッジを有効化してください -->
<!-- ![PyPI](https://img.shields.io/pypi/v/todo-cli?color=blue) -->

> A zero-dependency command-line to-do list written with [Typer](https://typer.tiangolo.com/).  
> Add, list, and mark tasks as done — all from your terminal.

---

## ✨ Features
- **Instant setup** – `pip install todo-cli` で即利用  
- **Persistent storage** – タスクを `~/.todo_cli.json` に自動保存  
- **Colorful output** – 完了時にグリーン表示  
- Python 3.10+ / Windows・macOS・Linux で動作

## 🎬 Demo
```bash
$ todo add "Finish README"
✓ 追加: 1. Finish README

$ todo list
1. [ ] Finish README   (2025-05-13 10:32)

$ todo done 1
✓ 完了: 1. Finish README
