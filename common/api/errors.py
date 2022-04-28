from bottle import error


@error(404)
def error404(err):
    return 'Nothing here, sorry'


@error(500)
def error500(err):
    return 'Oops!'
