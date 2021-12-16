from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    '''
    Register Profiles to access them from
    django admin panel
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
