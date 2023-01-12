import tweepy
import environ

# ---------------------Twitter APIを使うための設定-------------------
# 各種キー、トークンを格納
# 機密情報は別で管理しておく
env = environ.Env()
env.read_env('.env')

bearer_token = env('BEARER_TOKEN')
api_key = env('TW_API_KEY')
api_key_secret = env('TW_API_KEY_SECRET')
access_token = env('ACCESS_TOKEN')
access_token_secret = env('ACCESS_TOKEN_SECRET')

# Twitterオブジェクトの生成
client = tweepy.Client(
    bearer_token = bearer_token,
    consumer_key = api_key, consumer_secret = api_key_secret,
    access_token = access_token, access_token_secret = access_token_secret
)
# -------------------------------------------------------------------

# -------------------この部分をアプリ画面で操作する------------------
# 例えば、「大阪」の「グルメ」を知りたいとする

prefecture = '大阪' # ほかに'京都','兵庫','奈良','滋賀'など
purpose = 'グルメ'  # ほかに'観光'など
# -------------------------------------------------------------------

# ---------------------------ハッシュタグ検索------------------------
query_hashtag = '#' + prefecture + purpose
query_hashtag += ' lang:ja -is:retweet' # リツイートを除外

# query（検索クエリ）で検索するハッシュタグを指定
get_tweets = client.search_recent_tweets(
    query = query_hashtag,
    tweet_fields = ['id', 'public_metrics', 'text'],
    max_results = 4
).data

tweet_num = 0
for tweet in get_tweets:
    tweet_num += 1
    print('・' + str(tweet_num) + 'つ目のツイート\n')
    tweet_id = tweet.id
    tweet_url = 'https://twitter.com/i/web/status/' + str(tweet_id)
    print(tweet)
    print('\n')
    print('url : ' + str(tweet_url))
    print('=' * 80 + '\n')
# -------------------------------------------------------------------