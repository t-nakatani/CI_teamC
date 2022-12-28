# -*- coding: utf-8 -*-
"""translate.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wgqo3dbDbsiCWhIsnvp06vnl6Ac9qW6Z
"""

from easynmt import EasyNMT
model = EasyNMT('mbart50_m2m')
  
def get_translate(sentence):
      return model.translate(sentence, target_lang='en', max_new_tokens=1000) #翻訳後文章

#text = 'はじめましてこんにちは。今日はいい天気ですね！' #翻訳前文章
#text_translated=get_translate(text)
#print(text_translated)  #Hello, it's good weather today!