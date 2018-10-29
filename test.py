import bottle
from bottle import route, template, run

bottle.TEMPLATE_PATH.insert(0, 'views')

@route('/', method="POST")
@route('/', method="GET")
def index_page():
    output = template("index")
    return output


@route("/tank_description",methods='GET')
@route("/tank_description",methods='POST')
def tank_description():
    output = template("index")
    return output


@route("/war" ,methods=('GET', 'POST' ))
def war():
    return "This is the results page"


@route("/query", methods=('GET', 'POST' ))
def query():
    return "This will be used to find details of certain battles"


run(debug=True)
