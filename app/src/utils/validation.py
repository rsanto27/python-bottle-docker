from bottle import request, response, abort

def verifyKeys(model):
    error = {
        "fieldsNotFound": [],
        "fieldsWrongType": []
    }
    for key in model:
        try:
            if key not in request.json:
                error["fieldsNotFound"].append(key)
        except:
            # TODO deal better with this
            pass

    if error["fieldsNotFound"]:
        abort(400, error)


def valid(function, model):
    def inner(*args, **kwargs):
        if request.json:
            verifyKeys(model)
            return function(*args, **kwargs)
        
        response.status = 400
        return {'error': 'ValidationError',
                'error_message': 'Body is required (and must be JSON).'}
    return inner
