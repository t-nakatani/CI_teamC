from django.shortcuts import render, redirect
from functions.search_tweets import get_tweepy_client, get_tweets
from functions.sentiment_analyze import SentimentAnalysis
from easynmt import EasyNMT
import requests  # TODO: remove

sa_model = SentimentAnalysis()
trans_model = EasyNMT('opus-mt')
trans_model.translate('これはサンプルテキストです', target_lang='en', max_new_tokens=500)  # for load model

def home(request):
    """ホームページ"""
    if request.method == 'POST':
        print('===========  POST  ===============')
        region = request.POST['region']
        return redirect('search_tweets', region)

    return render(request, 'home.html')


def search_tweets(request, region):
    """地域(ex. 大阪)のボタンを押した際に動作"""
    if request.method == 'POST':
        region = request.POST['region']
        return redirect('search_tweets', region)

    if request.method == 'GET':
        print('=============  search_tweets  ================')
        tweepy_client = get_tweepy_client()
        responses, texts = get_tweets(tweepy_client, region)
        sentiments = [sa_model.get_label(txt) for txt in texts]
        positive_responses = [r for r, s in zip(responses, sentiments) if s == 'ポジティブ']
        positive_texts = [t for t, s in zip(texts, sentiments) if s == 'ポジティブ']
        translated_pos_texts = [
            trans_model.translate(text, target_lang='en', max_new_tokens=500) for text in positive_texts
        ]
        tweet_items = [
            {'response': response, 'en_text': en_text} for response, en_text in zip(responses, translated_pos_texts)
        ]

    return render(request, 'home.html', {'tweet_items': tweet_items})
