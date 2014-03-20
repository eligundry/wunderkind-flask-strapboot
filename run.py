import sys

from flask.ext.script import Manager, prompt, prompt_bool, prompt_pass

from application import create_app, db, models

app = create_app(['application.settings.site'])
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
    "Run the server on localhost:5000"
    app.debug = True
    app.run()

@manager.command
def db(action):
    "Create or delete the application's database"
    if action is 'create':
        pass
    elif action is 'drop':
        pass
    else:
        print(u'Invalid action "{}"'.format(action))
        sys.exit(1)

if __name__ == "__main__":
    manager.run()
