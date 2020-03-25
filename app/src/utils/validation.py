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

# just for test if is callable based on two decorators :)
def unique(function, model):
    def innerss(*args, **kwargs):
        abort(400, "error")
        if request.json:
            print("that's ok")
            return function(*args, **kwargs)
        
        response.status = 400
        return {'error': 'ValidationError',
                'error_message': 'Body is required (and must be JSON).'}
    return innerss