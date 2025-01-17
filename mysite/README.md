# Remember: Test the Views
## Run the development server:
"""
bash
Copy code
python manage.py runserver
Open your browser and test:
Homepage: http://127.0.0.1:8000/blog/
Detail page: http://127.0.0.1:8000/blog/1/
"""

# Model

> 
- used to **define** the structure of a database table to be used. specifies the field's (or column) data types and sizes
- in other words, model **describes** the desired database table needed to be created

# Migrations
> Migration files create a reference of any changes to the database models,
which means we can track changes-and debug errors 
So, create a migration file this way:

```python manage.py makemigrations myitemapp```

# migrate
> In other to have the database 'table' **described** by Model "physically constructed", we **migrate**. In another way, this means that migrate is used to **create** a database or a model by "building" the described database.

```python manage.py migrate```

The migrate command applies or constructs all the necessaries like admin, authentifications, contenttypes, apps or posts, sessions, etc in our migration file for further use.




