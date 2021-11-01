from flask import render_template
from newsapi import NewsApiClient
from app import app


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    newsapi=NewsApiClient(api_key= "63df4926bb9a41218025771acc1674f6")
    
    headlines=newsapi.get_headlines(sources="bbc-news")
    articles=headlines("articles")
    
    
    
    img =[]
    decs=[]
    news=[]
    
    

    
    return render_template('index.html')