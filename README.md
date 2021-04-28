# River demo

Install and run the demo

Language setup

```
echo "layout poetry" >> .envrc
asdf local python 3.9.2
```

```
poetry install
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username demo --email demo@demo.com
python manage.py runserver
```

Navigate to http://localhost:8000/admin (login with `demo`)

- Make State(s)

  - start, start, start node
  - second, second, second node

- Make Workflow
  - orderprocess.models.MyModel - my_state_field, start
