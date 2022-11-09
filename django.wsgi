import os, sys
virtual_env = os.path.expanduser('~/projects/env')
activate_this = os.path.join(virtual_env, 'bin/activate_this.py')
exec(open(activate_this).read(), dict(__file__=activate_this))
sys.path.insert(0, os.path.expanduser('~/projects/mysite'))
from mysite.wsgi import application

