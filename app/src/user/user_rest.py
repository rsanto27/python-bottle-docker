from bottle import Bottle, run, template, request, post, route, get, response
import auth.auth as au
import src.profile.profile_business as profBusiness

appUser = Bottle()

@appUser.route('/user/hello')
def sayHelloUser():
    return 'hello user'

@appUser.get('/user/token')
def get_token():
    user = {"name": "Rodrigo", "email": "rodrigo@email.com"}
    user["profile"] = profBusiness.get_profile()
    return au.get_token(user)

@appUser.get('/user/retoken')
def get_retoken():
    authReq = request.headers.get("Authorization")
    decoded = au.decode_token(authReq)
    # TODO 
    # if token ok, serch user on database, if ok renew
    return au.get_token(decoded)

