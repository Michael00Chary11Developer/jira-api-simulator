# python -m pip freeze
# python3 -m venv (name)
# pip install django
# django-admin startproject (name)
# python manage.py runserver
# python manage.py createsuperuser
# python manage.py makemigrations
# python manage.py migrate
# pip install djangorestframework
# pip install markdown
# pip install django-filter
# go to install app add => 'rest_framework'
# go to urls path('api-auth/', include('rest_framework.urls'))
# for creating new port => python manage.py runserver 8001
# pip install djangorestframework-simplejwt
# pip install djangorestframework-simplejwt[crypto]
# pip install drf-spectacular


# REST_FRAMEWORK = {
#     ...
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         ...
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     )
#     ...
# }


#DRF spactular

# INSTALLED_APPS = [
#     # ALL YOUR APPS
#     'drf_spectacular',
# ]