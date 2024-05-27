from flask.cli import FlaskGroup

from project import app, db, People

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("config")
def config():
    print(app.config.keys())
    print(app.config.values())
    
@cli.command("seed_db")
def seed_db():
    db.session.add(People(first_name='Batman', last_name='Robin'))
    db.session.commit()
    
if __name__ == '__main__':
    cli()