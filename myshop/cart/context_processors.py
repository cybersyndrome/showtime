from .cart import Cart

def cart(request):
    '''
    -instatiate the cart using the request object
    -make it available for the templates as a variable named cart
    '''
    return {'cart': Cart(request)}

    # a context procressor is a python function that takes a request object
    # and returns a dictionary that gets added to the request context