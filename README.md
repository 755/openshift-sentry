Sentry on OpenShift
===================

Basic Setup
-----------

Create a new OpenShift app:

```
rhc app create -a <app_name> -t diy-0.1
```

Choose a database engine to install.

_note: if you have an older version of rhc you may need to use the syntax `rhc app cartridge add -c <db_cartrige> -a <app_name>`_

For **postgresql** (the default setup for this repo):

```
rhc cartridge add postgresql-8.4 -a <app_name>
```

For **mysql** (may be your preference, or installing mysql is having issues):

```
rhc cartridge add mysql-5.1 -a <app_name>
```

Add this upstream repo

```
cd <app_name>
git remote add upstream -m master git://github.com/755/openshift-sentry.git
git pull -s recursive -X theirs upstream master
```

Configuration
-------------

Edit sentry.conf.py:
```
SENTRY_KEY = 'super_secret_key'
```

Two additional changes if you are choosing mysql:

Firstly, change the database engine as well in sentry.conf.py from:
```
'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
```
to:
```
'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
```

Secondly, switch which database python package is commented out in requirements.txt:
```
psycopg2==2.4.5
#MySQL-python
```
(There should not be a problem if you leave both uncommented, you will just waste time installing things you do not need)

Deployment and final setup
--------------------------

Now, push the repo upstream

```
git push
```

Create superuser
* login to rhcloud
```
ssh c8812345:123214@<app_name>-namespace.rhcloud.com
```

* activate virtual env
```
source ${OPENSHIFT_DATA_DIR}/${OPENSHIFT_APP_NAME}/bin/activate
```

* create superuser
```
sentry --config=$OPENSHIFT_REPO_DIR/sentry.conf.py createsuperuser
```



**Warning:**
You need to create superuser via ssh


License
-------

Copyright (C) 2011 Nick Nazarov <nazarov755@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

See also: [MIT_License](http://en.wikipedia.org/wiki/MIT_License "MIT_License")


