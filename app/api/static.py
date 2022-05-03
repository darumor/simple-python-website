from bottle import static_file, get
from app.app_main import App


@get('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=App.service.config.static_files_directory)


@get('/scripts/components/<filename>')
def server_script(filename):
    return static_file(filename, root=App.service.config.static_files_directory+'/scripts/components')


@get('/scripts/<filename>')
def server_script(filename):
    return static_file(filename, root=App.service.config.static_files_directory+'/scripts')


@get('/')
def index():
    return server_static('frontpage.htm')


@get('/login')
def login():
    return server_static('login.htm')


@get('/restricted')
def restricted_area():
    return server_static("restricted.htm")


@get('/admin')
def admin_area():
    return server_static("adminpage.htm")
