import tweepy
import environ

# ---------------------Twitter APIを使うための設定-------------------
# 各種キー、トークンを格納
# 機密情報は.envファイルに管理しておく

def load_env_var(env_path='.env'):
    env = environ.Env()
    env.read_env(env_path)
    return env

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
    tweet_urls = ['https://twitter.com/i/web/status/' + str(tweet.id) for tweet in tweets]
    tweet_texts = [tweet for tweet in tweets]  # TODO: Literally from object to text
    return tweet_urls, tweet_texts
