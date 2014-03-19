from flask.ext.script import Manager

from application import create_app

app = create_app('[application.settings.site]')
manager = Manager(app)

@manager.command
def server():
    app.debug = True
    app.run()
