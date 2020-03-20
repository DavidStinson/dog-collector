# Generated by Django 3.0.4 on 2020-03-20 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Walks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('E', 'Evening')], default='M', max_length=1)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Dog')),
            ],
        ),
    ]
