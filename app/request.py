from app import app
import urllib.request,json
from .models import News
# Getting api key
api_key = '63df4926bb9a41218025771acc1674f6'


# Getting the news base url
base_url = 'https://newsapi.org/v2/top-headlines/sources?category={}&apiKey={}'



def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
    return news_results
def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')

        news_object = News(id,name,description)
        news_results.append(news_object)
    return news_results