# Django complete registration cli (development stage)
----------------------------------

## Todo
-------
* It should download all templates and place them in the app at the path templates/registration
* It should detect if django-registration-redux exists and if not then download it.
* It should find the settings.py and add 'registration' to apps.
* It should accept an argument of the app name to setup within
* It should accept an argument for the block name
* It should add (r'^accounts/', include('registration.backends.simple.urls')), to the projects urls.py
* It should add these lines to settings.py:
  * REGISTRATION_OPEN = True
  * ACCOUNT_ACTIVATION_DAYS = 7
  * REGISTRATION_AUTO_LOGIN = True
  * LOGIN_REDIRECT_URL = '/rango/'
  * LOGIN_URL = '/accounts/login/'
* It should add 'registration', to settings.py APPS

Note: Might just include the settings.py and urls.py as simple directions instead of file overrides for safety.


## URL Mappings
---------------
* ^admin/
* ^YOUR_APP/
* ^accounts/ ^register/$ [name='registration_register']
* ^accounts/ ^register/closed/$ [name='registration_disallowed']
* ^accounts/ ^register/complete/$ [name='registration_complete']
* ^accounts/ ^login/$ [name='auth_login']
* ^accounts/ ^logout/$ [name='auth_logout']
* ^accounts/ ^password/change/$ [name='auth_password_change']
* ^accounts/ ^password/change/done/$ [name='auth_password_change_done']
* ^accounts/ ^password/reset/$ [name='auth_password_reset']
* ^accounts/ ^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$ [* name='auth_password_reset_confirm']
* ^accounts/ ^password/reset/complete/$ [name='auth_password_reset_complete']
* ^accounts/ ^password/reset/done/$ [name='auth_password_reset_done']

## Resources
* Borrow from, clean up, and give credit to https://github.com/macdhuibh/django-registration-templates for the templates
* CL for django https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
