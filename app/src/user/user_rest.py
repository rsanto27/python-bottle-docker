from bottle import Bottle, run, template, request, post, route, get, response, HTTPResponse
import auth.auth as au
import src.profile.profile_business as profBusiness
import src.user.user_validation as userValid

appUser = Bottle()

@appUser.route('/user/hello')
def sayHelloUser():
    return 'hello user'

@appUser.get('/user/token')
def get_token():
    user = {"name": "Rodrigo", "email": "rodrigo@email.com"}
    user["profile"] = profBusiness.get_profile()
    token = au.get_token(user)
    return {"token": token}
    

@appUser.get('/user/retoken')
def get_retoken():
    authReq = request.headers.get("Authorization")
    decoded = au.decode_token(authReq)
    # TODO 
    # if token ok, serch user on database, if ok renew
    return au.get_token(decoded)

@appUser.post('/user', apply=(userValid.valid))
# if used the decorator this way, its not nedded use apply
# @userValid.valid
def post_user():
    name = request.json.get("username")
    email = request.json.get("email")
    return "ok"
#     password = request.json.get("password")
#     response.body = name + "====" +password
#     return response
#     #return name + "====" +password
#     #return template('{{name}}  {{password}}', name=name, password=password)

