The following are instructions for setting up and running the sample project.

1. First, download prerequisites via command line:

pip install django
pip install django-heroku
pip install gunicorn
pip install postgres
pip install psycopg2-binary
pip install dj_database_url

2. In order to clone the repository, run

git clone https://github.com/maximiliani2014/Mini-WhereDoYouLive

(It will go into a new directory titled Mini-WhereDoYouLive in the current directory.)

3. Make it a Django project:

django-admin startproject mysite

4. Create a Postgres database. The easiest way to accomplish this is by installing Postgres.app and following its instructions. Make sure to run the Postgres server on port 5432 and that the database's details are the following:

name: database
username: postgres
password: postgres

If you can't run the app for some reason, you can run the following commands:

pg_ctl -D /usr/local/var/postgres start
createdb [database]
psql [database]
 
# your prompt should now be [database]=#

CREATE USER [user] WITH PASSWORD '[password]';
Some configuration that Django expects:
ALTER ROLE [user] SET client_encoding TO 'utf8';
ALTER ROLE [user] SET default_transaction_isolation TO 'read committed';
ALTER ROLE [user] SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE [database] TO [user];
\q

5. Migrate:

python manage.py migrate

6. Now, you should be able to host the server locally! Run

python manage.py runserver

and type

localhost:8000

in the address bar in your web browser.

7. To push the project onto Heroku, you will first need to uncomment the following lines (since the configuration is different locally and on Heroku)

import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

8. Now, initialize the Heroku project:

heroku create

Your project will be given a random name, such as serene-caverns-8293.

9. Push the project to Heroku:

git push heroku master

10. Provision Postgres for your project. This involves going to your app's page on heroku.com, going to Resources > Add-ons, and searching for Postgres. Make sure Postgres isn't already provisioned!

11. Push the table to Heroku, since Heroku doesn't generate the tables automatically. This can be accomplished by the command

heroku pg:push [local database] [Heroku database] --app [app name]

You can check the name of the Heroku database on the Add-ons panel from above.

For further information, see the following tutorials:
https://docs.djangoproject.com/en/2.1/intro/tutorial01/
https://devcenter.heroku.com/articles/heroku-postgresql (Provisioning Heroku Postgres, Local setup, Using the CLI, Connecting in Python)
https://devcenter.heroku.com/articles/getting-started-with-python 