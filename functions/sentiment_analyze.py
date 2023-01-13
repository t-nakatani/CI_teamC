from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

class SentimentAnalysis:

    # コンストラクタ(モデルの読み込み)
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("daigo/bert-base-japanese-sentiment")
        self.model = AutoModelForSequenceClassification.from_pretrained("daigo/bert-base-japanese-sentiment")
        self.nlp = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)

    # テキストを渡すとネガポジを返す
    def get_label(self, text):
        return self.nlp(text)[0]["label"]

    # テキストを渡すとネガポジの度合いを返す
    def get_score(self, text):
        return self.nlp(text)[0]["score"]

if __name__ == '__main__':
    model = SentimentAnalysis()
    text = "今日はいい天気ですね"
    print(model.get_label(text))  # ポジティブ
    print(model.get_score(text))  # 0.9780256152153015
