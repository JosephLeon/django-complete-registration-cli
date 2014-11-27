'''
1. Create django admin command
2. It should download all templates
3. It should detect if django-registration-redux exists and if not then download
it.
4. It should find the settings.py and add 'registration' to apps.
'''

'''
^admin/
^rango/
^accounts/ ^register/$ [name='registration_register']
^accounts/ ^register/closed/$ [name='registration_disallowed']
^accounts/ ^register/complete/$ [name='registration_complete']
^accounts/ ^login/$ [name='auth_login']
^accounts/ ^logout/$ [name='auth_logout']
^accounts/ ^password/change/$ [name='auth_password_change']
^accounts/ ^password/change/done/$ [name='auth_password_change_done']
^accounts/ ^password/reset/$ [name='auth_password_reset']
^accounts/ ^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$ [name='auth_password_reset_confirm']
^accounts/ ^password/reset/complete/$ [name='auth_password_reset_complete']
^accounts/ ^password/reset/done/$ [name='auth_password_reset_done']
'''
