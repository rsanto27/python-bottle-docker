from bottle import Bottle, run, template, request, post, route, get, response
import src.user.user_rest as userRest
import src.profile.profile_rest as profRest

appFactory = Bottle()
appFactory.merge(userRest.appUser)
appFactory.merge(profRest.appProfile)