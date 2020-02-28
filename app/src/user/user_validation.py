from bottle import request, response

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

def verify():

    for key in userPost:
        print(key)
        # print(request.json[key])
        if request.json[key] is None:
            error["fieldsNotFound"].append(key)

def valid(function):
    def inner(*args, **kwargs):
        if request.json:
            verify()
            return function(*args, **kwargs)

        response.status = 400
        return {'error': 'ValidationError',
                'error_message': 'Body is required (and must be JSON).'}
    return inner