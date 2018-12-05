# Webapp-todo

## How to run the application app locally

* Clone the repository
* Run `cd webapp-todo`
* Run `pip install -r requirements`
* IMPORTANT: Make sure to EDIT _api.py_ and change the 'SQLALCHEMY_DATABASE_URI' -> You can use a SQLite3 database
* Start the current web application
  * You can try running the Flask application directly `python api.py`
  * Or you can run it using _gunicorn_ webserver `gunicorn api:app`


## Live web server deployed (for testing purposes)

* https://orca-todo.herokuapp.com/
