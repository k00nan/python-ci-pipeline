# type: ignore

import nox


@nox.session(python=["3.10"])
def check_code_formatting(session):
    session.run("poetry", "install", "--only", "formatting", external=True)
    session.run("isort", ".", "--check", external=True)
    session.run("black", ".", "--check", external=True)


@nox.session(python=["3.10"])
def format_code(session):
    session.run("poetry", "install", "--only", "formatting", external=True)
    session.run("isort", ".", external=True)
    session.run("black", ".", external=True)


@nox.session(python=["3.10"])
def check_static_typing(session):
    session.run("poetry", "install", "--only", "static_type_checking", external=True)
    session.run("poetry", "install", "--only", "testing", external=True)
    session.run("mypy", ".", external=True)


@nox.session(python=["3.10"])
def lint(session):
    session.run("poetry", "install", "--only", "linting", external=True)
    session.run("ruff", ".", external=True)


@nox.session(python=["3.10"])
def run_unit_tests(session):
    session.run("poetry", "install", "--only", "testing", external=True)
    session.run("pytest", ".", external=True)
