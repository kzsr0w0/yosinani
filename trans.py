import streamlit as st
from transformers import pipeline

st.title('悩み相談アプリ')

# ファインチューニング済みのモデルを使用
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
classifier = pipeline('text-classification', model=model_name)

user_input = st.text_input("あなたの悩みを教えてください:")

if user_input:
    # モデルによる応答の生成
    response = classifier(user_input)
    st.write(response)