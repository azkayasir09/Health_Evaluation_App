from django.contrib import admin
from webapp.models import Prediction
from webapp.models import Login
from webapp.models import Registration
from webapp.models import Feedback
from webapp.models import User

# Register your models here.
admin.site.register(Prediction)
admin.site.register(Feedback)
admin.site.register(Login)
admin.site.register(Registration)
admin.site.register(User)
