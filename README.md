Sentry on OpenShift
================


Create a new OpenShift app:

```
rhc app create -a <app_name> -t diy-0.1
rhc app cartridge add -c mysql-5.1 -a <app_name>
```

Add this upstream repo

```
cd <app_name>
git remote add upstream -m master git://github.com/755/openshift-sentry.git
git pull -s recursive -X theirs upstream master
```

Edit sentry.conf.py:
```
SENTRY_KEY = 'super_secret_key'
```

Then push the repo upstream

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

