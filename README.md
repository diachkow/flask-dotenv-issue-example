# Poetry + Flask + python-dotenv issue

Project to show the existing issue of using Flask with Poetry & python-dotenv package.

## Deployment

To run this application do the following:

1. Clone this repo.
2. Go to project root directory.
3. Install project dependencies: `poetry install`.
4. Make a copy of [dotenv](dotenv) and fill in the reuqired values:
```shell script
cp dotenv .env
vim .env
# Fill in the values
```
5. Activate virtualenvironment: `poetry shell`.
6. Run flask application: `python3 src/main.py`.

You are supposed so see something like that:
```
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 321-365-698
```

## Issue

As I use `vim` as a text editor I want to be in `src` directory when I'm working on my projects. However, if yoy will try to do this (after all dependencies install & `.env` configured):
```shell script
cd src
python3 main.py
```

You are supposed to get this error:
```
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
/home/vitaliy/.cache/pypoetry/virtualenvs/flask-poetry-issue-example-5Ps4O6ft-py3.8/bin/python3: can't open file '/home/vitaliy/coding/flask-poetry-issue-example/main.py': [Errno 2] No such file or directory
```
