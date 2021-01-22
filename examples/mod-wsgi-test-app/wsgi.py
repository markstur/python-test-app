import os
import pwd
from flask import Flask
application = Flask(__name__)

def test_chown():
    print("TEST1")
    testfile = "/tmp/testfile.txt"

    print("TEST2")
    os.close(os.open(testfile, os.O_CREAT))

    print("TEST3")
    print("st_uid:", os.stat(testfile).st_uid)
    print("st_gid:", os.stat(testfile).st_gid)

    print("TEST4")
    # uid = os.getuid()
    # gid = os.getgid()
    nobody = pwd.getpwnam("nobody")
    uid = nobody.pw_uid  # os.getuid()
    gid = nobody.pw_gid  # os.getgid()
    os.chown(testfile, uid, gid)
    print("os.chown", testfile, uid, gid)

    print("TEST5")
    print("st_uid:", os.stat(testfile).st_uid)
    print("st_gid:", os.stat(testfile).st_gid)

    print("TEST6")
    uid = os.getuid()
    gid = os.getgid()
    os.chown(testfile, uid, gid)
    print("os.chown", testfile, uid, gid)
    print("st_uid:", os.stat(testfile).st_uid)
    print("st_gid:", os.stat(testfile).st_gid)

@application.route('/')
def hello():
    test_chown()
    return b'Hello World from mod_wsgi hosted WSGI application!'

if __name__ == '__main__':
    application.run()
