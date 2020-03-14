import pickle

import click
from flask.cli import with_appcontext

from . import db


@click.command('init-db')
@with_appcontext
def init_db_command():
    db.init_db()


@click.command('set-model')
@click.argument('path')
@click.option('--reset_metrics', is_flag=True)
@with_appcontext
def set_model_command(path, reset_metrics):

    with open(path, 'rb') as f:
        model = pickle.load(f)
        db.set_model(model=model, reset_metrics=reset_metrics)

    click.echo('Model has been set.')
