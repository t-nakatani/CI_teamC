import tweepy
import environ
import re
# ---------------------Twitter APIを使うための設定-------------------
# 各種キー、トークンを格納
# 機密情報は.envファイルに管理しておく

def load_env_var(env_path='.env'):
    env = environ.Env()
    env.read_env(env_path)
    return env


def get_api():
    env = load_env_var()
    """Gets the API object after authorization
    and authentication.
    """
    auth = tweepy.OAuthHandler(
        env('TW_API_KEY'),
        env('TW_API_KEY_SECRET')
    )
    auth.set_access_token(
        env('ACCESS_TOKEN'),
        env('ACCESS_TOKEN_SECRET')
    )
    return tweepy.API(auth)


def get_tweepy_client():
    env = load_env_var()
    bearer_token = env('BEARER_TOKEN')
    api_key = env('TW_API_KEY')
    api_key_secret = env('TW_API_KEY_SECRET')
    access_token = env('ACCESS_TOKEN')
    access_token_secret = env('ACCESS_TOKEN_SECRET')

    # Twitterオブジェクトの生成
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=api_key, consumer_secret=api_key_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )
    return client
# -------------------------------------------------------------------



# -------------------この部分をアプリ画面で操作する------------------
# 例えば、「大阪」の「グルメ」を知りたいとする

def get_tweets(tweepy_client, prefecture='大阪', purpose='グルメ'):
    """
    prefecture: '京都','兵庫','奈良','滋賀'など
    purpose: '観光'など
    """
    api = get_api()

    # -------------------------------------------------------------------

    # ---------------------------ハッシュタグ検索------------------------
    query_hashtag = '#' + prefecture + purpose
    query_hashtag += ' lang:ja -is:retweet'  # リツイートを除外

    # query（検索クエリ）で検索するハッシュタグを指定
    tweets = tweepy_client.search_recent_tweets(
        query=query_hashtag,
        tweet_fields=['id', 'public_metrics', 'text'],
        max_results=10
    ).data
    texts = [tweet.text for tweet in tweets]

    tweet_ids = [tweet.id for tweet in tweets]
    detailed_tweets = [tweepy_client.get_tweet(id=int(tw.id), expansions=["author_id"], user_fields=["username"]) for tw in tweets]

    user_ids = [tweet.includes["users"][0] for tweet in detailed_tweets]
    tweet_urls = [f'https://twitter.com/{uid}/status/{tid}' for tid, uid in zip(tweet_ids, user_ids)]
    responses = [api.get_oembed(url)['html'] for url in tweet_urls]

    before = '<blockquote class="twitter-tweet">'
    after = '<blockquote class="twitter-tweet" data-width="300">'
    responses = [resp.replace(before, after) for resp in responses]
    return responses, texts

if __name__ == '__main__':
    client = get_tweepy_client()
    responses, texts = get_tweets(client)
    print(responses[0], texts[0])
