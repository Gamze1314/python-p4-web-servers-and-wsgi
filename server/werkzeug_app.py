#!/usr/bin/env python3


from werkzeug.wrappers import Request, Response


@Request.application  # decorator. 
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    #run_simple method runs a server for a one-page application. not suited for a production server that supports millions of users.
    #requires 3 args.
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )

    

#CNTRL  + C to stop the server running.
#werkzeug and python together created a WSGI application that is running on port 5555. it handles the request and generates message line 10.( response). Werkzeug takes the request and returns the response. 