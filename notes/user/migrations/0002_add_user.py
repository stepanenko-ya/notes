from django.db import migrations, models
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


def create_initial_users(apps, schema_editor):
    User = get_user_model()

    admin, created = User.objects.get_or_create(
        email='admin@test.com',
        defaults={
            'username': 'admin',
            'password': make_password('admin'),
            'is_active': True,
            'is_staff': False,
            'is_superuser': False
        })
    admin.save()


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0001_initial'),
    ]
    operations = [migrations.RunPython(create_initial_users)]

