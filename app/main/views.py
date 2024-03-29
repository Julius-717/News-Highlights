from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_topnews, get cat_news, get_updates
@main.route('/')
def index():

    top_articles = get_topnews('google-news')
    print(top_articles)
    biz_articles = get_catnews('business')
    tech_articles = get_catnews('technology')
    ent_articles = get_catnews('entertainment')
    sprt-articles = get_catnews('sports')
    title = 'Home -Get breaking news headlines, and search for articles from over 30,000 news sources and blogs'
    return render_template('index.html', title = title, google_news = top_articles, biz = biz_articles, tech = tech_articles, ent = ent_articles, sprt = sprt_articles)

@main.route('/update/<id>')
def article(id):
    detz_articles = get_updates(id)
    print(detz_articles)
    return render_template('news-update.html', detz = detz_articles)

