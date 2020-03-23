def error403(error):
    print(error) # inside error, we have all that we need, just format
    return "{'test':'test'}"

def error404(error):
    print(error) # inside error, we have all that we need, just format
    return "{'test':'testssss'}"

def error400(error):
    return error.body
