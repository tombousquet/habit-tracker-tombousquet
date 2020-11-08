# Generated by Django 3.1.3 on 2020-11-08 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('target', models.IntegerField()),
                ('measure', models.CharField(max_length=255)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual', models.IntegerField()),
                ('date', models.DateField()),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='core.habit')),
            ],
            options={
                'unique_together': {('habit', 'date')},
            },
        ),
    ]
