import auth.auth as au
from bottle import Bottle, run, template, request, post, route, get, response
import settings as sett
import src.app_factory as appFac

app = Bottle()
app.merge(appFac.appFactory)
settings = sett.Settings()

@app.hook('before_request')
def verify_token():
    token = au.get_token({"name": "Rodrigo", "email": "rodrigo@email.com"})
    print(settings.key)

@app.hook('after_request')
def after_request():
    enable_cors()

def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*' # set here the origins that you want to allow permission
    response.headers['Access-Control-Allow-Headers'] = 'Accept, Accept-Type, Authorization, Content-Type, Origin, X-CSRF-Token, X-Requested-With'
    response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, OPTIONS, POST, PUT'

app.run(debug=False, host='0.0.0.0', port=8081, reloader=False)


# @app.route('/hello')
# @app.route('/hello/<name>')
# def hello(name='default'):
#     return template('hello {{name}}', name=name)

# @app.get('/get')
# def get_verb():
#     return "<h1>get method request</h1>"

# @app.get('/get/<param>')
# def get_verb(param='default'):
#     return param

# @app.post('/postsomething')
# def post_verb():
#     name = request.json.get("username")
#     password = request.json.get("password")
#     response.body = name + "====" +password
#     return response
#     #return name + "====" +password
#     #return template('{{name}}  {{password}}', name=name, password=password)