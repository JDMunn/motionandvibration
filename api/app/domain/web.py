import abc


class WebObject(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __tojson__(self):
        raise NotImplementedError('must define __tojson__ to use this base class,'
                                  + ' method should return an object that can be'
                                  + ' json serialized, such as a dictionary or list')


class Health(WebObject):

    def __init__(self, calls, routes, status):
        self.calls = calls
        self.routes = routes
        self.status = status


    def __tojson__(self):
        return {
            "requestsServed": {
                route: self.calls[route] for route in self.routes
            },
            "status": self.status
        }


class Error(WebObject):

    def __init__(self, error):
        self.error = error


    def __tojson__(self):
        return {
            "error": str(self.error)
        }
