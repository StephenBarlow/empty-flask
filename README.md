# Empty Flask

A simple Flask application managed with [uv](https://docs.astral.sh/uv/).

## Setup

Install dependencies:

```bash
uv sync
```

## Run

Run the Flask application:

```bash
uv run flask --app hello run
```

Or activate the virtual environment:

```bash
source .venv/bin/activate
flask --app hello run
```

## Add Dependencies

Add new dependencies:

```bash
uv add package-name
```

Or edit `pyproject.toml` and run `uv sync`.
