from bottle import route, run, post, request
from mongoengine import connect

connect('datagram_db')

@route('/status/')
def server_status():
    return "Server is online"

@post('/login/')
def user_login():
    jsonData = request.json()
    user_email = jsonData['email']
    password = jsonData['password']


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)