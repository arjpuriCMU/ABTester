from flask import current_app, request

class ABTester:
    def __init__(self, app = None):
        self.app = app
        self.init_app(app)

    def init_app(app):
        app = ctx.app
        app.jinja_env.globals.update({
            'test': test,
            'converted': converted
        })

    def test():
        pass

    def converted():
        pass
