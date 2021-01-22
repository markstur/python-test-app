import os
from flask import Flask
application = Flask(__name__)

def test_chown():
    testfile = "/tmp/testfile.txt"
    print("TEST1")

    os.close(os.open(testfile, os.O_CREAT))
    print("TEST2")

    print("st_uid:", os.stat(testfile).st_uid)
    print("st_gid:", os.stat(testfile).st_gid)
    print("TEST3")

    uid = 501
    gid = 20
    os.chown(testfile, uid, gid)
    print("os.chown", testfile, uid, gid)
    print("TEST4")

    print("st_uid:", os.stat(testfile).st_uid)
    print("st_gid:", os.stat(testfile).st_gid)
    print("TEST5")

@application.route('/')
def hello():
    test_chown()
    return b'Hello World from mod_wsgi hosted WSGI application!'

if __name__ == '__main__':
    application.run()
