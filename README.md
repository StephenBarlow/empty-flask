# Empty Flask

A simple Flask application managed with [uv](https://docs.astral.sh/uv/).

## Setup

Install dependencies:

```bash
uv sync
```

## Run

Run the Flask development server:

```bash
uv run flask --app hello run
```

Run with Gunicorn (production):

```bash
uv run gunicorn hello:app
```

Or activate the virtual environment first:

```bash
source .venv/bin/activate
flask --app hello run        # development
gunicorn hello:app           # production
```

## Add Dependencies

Add new dependencies:

```bash
uv add package-name
```

Or edit `pyproject.toml` and run `uv sync`.
