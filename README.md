Sentry on OpenShift
================


Create a new OpenShift app:

```
rhc app create -a <app_name> -t diy-0.1
rhc app cartridge add -c mysql-5.1 -a <app_name>
```

Add this upstream repo

```
cd django
git remote add upstream -m master git://github.com/openshift/django-example.git
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

**Warning:**
On every deployment re-creating the python virtual environment

Comment string at `.openshift/action_hooks/deploy` after first push to OpenShift:
```
virtualenv --no-site-packages --clear $OPENSHIFT_DATA_DIR/$OPENSHIFT_APP_NAME
```