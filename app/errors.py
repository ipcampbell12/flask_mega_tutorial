from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500



#work very similar to view functions
#return contents of their corresponding templates
# also return error code 
#uses database rollback  to reset database session to a clean state
# create html templates to make sure they have same look and feel
# need to register them with Flask by importing to __init__.py page
