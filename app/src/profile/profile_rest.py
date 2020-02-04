from bottle import Bottle, run, template, request, post, route, get, response
import src.profile.profile_business as profBusiness

appProfile = Bottle()

@appProfile.get('/profile')
def get_profile():
    return profBusiness.get_profile()