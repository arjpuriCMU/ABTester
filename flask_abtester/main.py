from flask import current_app, request

@abt.record
def init_app(ctx):
    app = ctx.app
    app.jinja_env.globals.update({
        'test': test,
        'converted': converted
    })

    @app.template_filter()
    def percentage(number):
        number *= 100
        if abs(number) < 10:
            return "%.1f%%" % round(number, 1)
        else:
            return "%d%%" % round(number)
def test():
    pass

def converted():
    pass
