from bottle import request, response, abort
import src.utils.validation as validUtils

userPostModel = {
    "name": "str",
    "email": "str",
    "filtTest": "str"
}

userUniqueModel = {
    "name": "unique"
}

def valid(function):
    return validUtils.valid(function, userPostModel)

# this function is just to know if can i call two decorators from apply()
def testUnique(function):
    return validUtils.unique(function, userUniqueModel)
