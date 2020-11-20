import django_heroku

### Heroku Setting
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yftgrj&zt8=06mv7(hhum(fjceo2f$3$*xlo7m2gsq&fh92zrf'

def production_init(outer_locals):
    # Activate Django-Heroku.
    django_heroku.settings(outer_locals)
