from flask.ext.script import Manager

from application import create_app, db, models

app = create_app('[application.settings.site]')
manager = Manager(app)

@manager.shell
def make_shell_context():
    context = {
        'app': app,
        'db': db,
        'models': models,
    }

    return context

@manager.command
def server():
    app.debug = True
    app.run()

if __name__ == "__main__":
    manager.run()
