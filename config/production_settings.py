from .settings import *
import django_heroku

SECRET_KEY = 'yftgrj&zt8=06mv7(hhum(fjceo2f$3$*xlo7m2gsq&fh92zrf'
#DEBUG = False

# About Page URL
ABOUT_URL_MAP = {
    'ja' : 'https://nomrand.github.io/pleethai/ja/',
    'en' : 'https://nomrand.github.io/pleethai/en/',
    'th' : 'https://nomrand.github.io/pleethai/th/',
}

### Heroku Setting
# Activate Django-Heroku.
django_heroku.settings(locals())
