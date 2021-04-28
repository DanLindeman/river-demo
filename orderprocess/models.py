from django.db import models
from river.models.fields.state import StateField


class MyModel(models.Model):
    my_state_field = StateField()
