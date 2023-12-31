from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


class UserAdmin(admin.ModelAdmin):

    class Meta:
        model = User
        fields = '__all__'
