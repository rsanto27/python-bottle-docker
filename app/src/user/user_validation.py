from bottle import request, response

userPost = ["name", "email"]

def valid(function):
    def inner(*args, **kwargs):
        if request.json:
            return function(*args, **kwargs)

        response.status = 400
        return {'error': 'ValidationError',
                'error_message': 'Body is required (and must be JSON).'}
    return inner