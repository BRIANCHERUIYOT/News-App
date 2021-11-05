from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():
    

    '''
    View root page function that returns the index page and its data
    '''
    technology = get_news('technology')
    
    return render_template('index.html', technology=technology)

