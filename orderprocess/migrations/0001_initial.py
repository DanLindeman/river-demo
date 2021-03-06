# Generated by Django 3.2 on 2021-04-28 05:03

from django.db import migrations, models
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('river', '0002_auto_20210428_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_state_field', river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='river.state')),
            ],
        ),
    ]
