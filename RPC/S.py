from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('192.168.100.85', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()


    class Operaciones:
        def add(self, x, y):
            return x + y

        def sus(self, x, y):
            return x - y

        def mul(self, x, y):
            return x * y

        def div(self, x, y):
            if y == 0:
                r = 0
            else:
                r = x / y
            return r


    server.register_instance(Operaciones())
    server.serve_forever()
