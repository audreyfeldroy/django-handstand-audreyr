# deploy.wsgi is configured to live in <repo_root>/fc_project/deploy.

import os
import sys
import site

from os.path import abspath, dirname, join, pardir
from site import addsitedir

# Virtualenv fcc is in ~/.virtualenvs
site.addsitedir('/home/fc/.virtualenvs/fc/lib/python2.6/site-packages')

deploy_dir = dirname(__file__)
fc_project_dir = join(deploy_dir, pardir)
fluffiestcloud_dir = join(fc_project_dir, pardir)
home_dir = join(fluffiestcloud_dir, pardir)

sys.path.insert(0, abspath(fc_project_dir))
sys.path.insert(0, abspath(fluffiestcloud_dir))

#for path in sys.path:
#    print path

from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "fc_project.settings"

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
