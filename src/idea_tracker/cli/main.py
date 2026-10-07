import typer

from idea_tracker.storage.database import init_db

app = typer.Typer(help="Idea Tracker CLI")

@app.command()
def init():
    init_db()
    typer.echo("DB initialized.")

@app.command()
def add(title: str = typer.Option(...)):
    typer.echo(f"Added idea: {title}")

if __name__ == "__main__":
    app()
