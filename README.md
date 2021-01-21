# python-test-app

## Commands to run

```bash
oc login...
oc new-app https://github.com/markstur/python-test-app.git 
oc start-build python-test-app  
oc expose svc/python-test-app

```

## Example with output

```bash
% oc new-app https://github.com/markstur/python-test-app.git
--> Found image ae420ac (44 hours old) in image stream "markstur-project1/python" under tag "latest" for "python"

    Python 3.6 
    ---------- 
    Python 3.6 available as container is a base platform for building and running various Python 3.6 applications and frameworks. Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

    Tags: builder, python, python36, python-36, rh-python36

    * The source repository appears to match: python
    * A source build using source code from https://github.com/markstur/python-test-app.git will be created
      * The resulting image will be pushed to image stream tag "python-test-app:latest"
      * Use 'start-build' to trigger a new build
    * This image will be deployed in deployment config "python-test-app"
    * Port 8080/tcp will be load balanced by service "python-test-app"
      * Other containers can access this service through the hostname "python-test-app"

--> Creating resources ...
    imagestream.image.openshift.io "python-test-app" created
    buildconfig.build.openshift.io "python-test-app" created
    deploymentconfig.apps.openshift.io "python-test-app" created
    service "python-test-app" created
--> Success
    Build scheduled, use 'oc logs -f bc/python-test-app' to track its progress.
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose svc/python-test-app' 
    Run 'oc status' to view your app.

```

```bash
$ oc start-build python-test-app  
build.build.openshift.io/python-test-app-2 started
```




