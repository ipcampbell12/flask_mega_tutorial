from app import app, db, cli

from app.models import User, Post

#creates a shell context that adds database instance and models to shell sesssion, so you don't need to import them
#but need to type in "flask shell" in terminal, instead of "python"
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

#need to tell Flaks how to import app by setting FLASK_APP environment varaible
# export FLASK_APP=microblog.py


#or you can registers environment variables to be automatically imported when you run the app
#need this package: pip install python-dotenv