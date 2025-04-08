## Flask
**WebFramework for python**
```
Flask is a lightweight and flexible web framework.

It is called a "micro-framework" because it doesn’t include built-in tools like form validation or database abstraction—but you can easily add what you need using extensions.
```

```
Flask supports a huge number of extensions like:

    1. Flask-SQLAlchemy for ORM

    2. Flask-Login for authentication

    3. Flask-WTF for forms

    4. Flask-Migrate for migrations

```


## Always make a virtual Environment
```bash
python -m venv venv
```
```bash
source venv/bin/activate
```


## Points to ponder

1.  Flask automatically uses port 5000 by default.
2. Want to use a different port? 
    app.run(debug=True, port=8000)
3. Auto-reloading server with debug=True
4. Flask includes tools to prevent Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), and cookie tampering.
5. Build REST APIs
