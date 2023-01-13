from django.shortcuts import render, redirect
from functions.search_tweets import get_tweepy_client, get_tweets
from functions.sentiment_analyze import SentimentAnalysis
import requests

sa_model = SentimentAnalysis()

def home(request):
    """ホームページ"""
    if request.method == 'POST':
        print('===========  POST  ===============')
        region = request.POST['region']
        return redirect('search_tweets', region)

    return render(request, 'home.html')


def search_tweets(request, region):
    """地域(ex. 大阪)のボタンを押した際に動作"""
    if request.method == 'GET':
        print('=============  search_tweets  ================')
        tweepy_client = get_tweepy_client()
        responses, texts = get_tweets(tweepy_client, region)
        sentiments = [sa_model.get_label(txt) for txt in texts]
        positive_responses = [r for r, s in zip(responses, sentiments) if s == 'ポジティブ']
        if len(positive_responses) < 6:
            return render(request, 'home.html', {'responses': positive_responses})

    return render(request, 'home.html', {'responses': positive_responses[:6]})
