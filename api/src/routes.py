from bottle import Bottle, run, template, request, post, route, get, response

app = Bottle()

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='default'):
    return template('hello {{name}}', name=name)

@app.get('/get')
def get_verb():
    return "<h1>get method request</h1>"

@app.get('/get/<param>')
def get_verb(param='default'):
    return param

@app.post('/postsomething')
def post_verb():
    name = request.json.get("username")
    password = request.json.get("password")
    response.body = name + "====" +password
    return response
    #return name + "====" +password
    #return template('{{name}}  {{password}}', name=name, password=password)

@app.hook('before_request')
def verify_token():
    print("valid_token")

@app.hook('after_request')
def response_view():
    response.body = "update_body"
    print(response)
    print("valid_token")

#run(app, host="localhost", port=8081)
app.run(debug=False, host='localhost', port=8081, reloader=False)