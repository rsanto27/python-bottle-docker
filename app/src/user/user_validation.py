from bottle import request, response, abort

userPost = {
    "name": "str",
    "email": "str",
    "filtTest": "str"
}

error = {
    "status": 400,
    "fieldsNotFound": [],
    "fieldsWrongType": []
}

def verifyKeys():
    for key in userPost:
        print(key)
        try:
            if key not in request.json:
                error["fieldsNotFound"].append(key)
        except:
            # TODO deal better with this
            pass

    if error["fieldsNotFound"]:
        abort(400, {'error': 'fieldsNotFound', 'error_message': 'This fields are required: {}'.format(error["fieldsNotFound"]), 'fields': error["fieldsNotFound"]})

def valid(function):
    def inner(*args, **kwargs):
        if request.json:
            verifyKeys()
            return function(*args, **kwargs)
        
        response.status = 400
        return {'error': 'ValidationError',
                'error_message': 'Body is required (and must be JSON).'}
    return inner