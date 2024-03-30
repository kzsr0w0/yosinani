

import csv
import streamlit as st
import random

#---悩み相談入力-------------------------------------------------------------------#


# タイトルの設定
st.title('悩み相談アプリ')

# ユーザー入力の受け取り
user_input = st.text_input("あなたの悩みを教えてください:")

#---悩みへの応答-------------------------------------------------------------------＃
# テキストファイルから質問と応答を読み込む関数
def load_qa_pairs(filepath):
    qa_pairs = {}
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 2:
                qa_pairs[parts[0]] = parts[1]
    return qa_pairs

# 質問と応答のペアを読み込む
qa_pairs = load_qa_pairs("QA.txt")

if user_input:
    input_text = qa_pairs.get(user_input, "申し訳ありませんが、その質問には答えられません。")

   
#辞書を作成   
def read_csv_to_dict(file_path):
    style_dict = {}
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # ヘッダー行をスキップ
        for row in reader:
            style, key, value = row
            if style not in style_dict:
                style_dict[style] = {}
            style_dict[style][key] = value
    return style_dict

# CSVファイルパス
file_path = '口癖辞書.txt'

# CSVファイルを読み込んで辞書に変換
style_dict = read_csv_to_dict(file_path)

#style_dict = {
    #"スタイル1": {"こんにちは": "やあ！", "ありがとう": "サンキュー！"},
    #"スタイル2": {"こんにちは": "こんにちはなのです", "ありがとう": "感謝するのです"}   
#}

def convert_text(input_text, style):
    for key, value in style_dict[style].items():
        input_text = input_text.replace(key, value)
    return input_text



#input_text = st.text_area("メッセージを入力してください")
style = st.selectbox("スタイルを選択してください", ["スタイル1", "スタイル2", "スタイル3"])
if st.button('相談'):
    #response = requests.post("http://127.0.0.1:8000/convert/", json={"text": input_text, "style": style})
    converted_text = convert_text(input_text, style)
    st.write(converted_text)

    #名言
    #meigenn_list = f.readlines()
    #meigenn = random.choice(meigenn_list)
    #st.write('今日の名言は「',meigenn,'」です')

    #ヤタベザウルス表示
    image = "./image1.png"
    image2 = "./image2.png"
    col1, col2 = st.columns(2)

    with col1:
        #名言
        f = open('名言.txt','r',encoding='UTF-8')
        meigenn_list = f.readlines()
        meigenn = random.choice(meigenn_list)
        st.write('今日のM名言は「',meigenn,'」です')
        st.image(image, width=250)
        
    with col2:
        #y名言
        f = open('y_名言.txt','r',encoding='UTF-8')
        meigenn_list = f.readlines()
        meigenn = random.choice(meigenn_list)
        st.write('今日のY名言は「',meigenn,'」です')
        st.image(image2, width=250)

    # 最後の挨拶
    g = open('最後の挨拶.txt','r',encoding='UTF-8')
    aisatu_list = g.readlines()
    ran_list = [0, 1]
    w = [1, 5]
    aisatu = random.choices(aisatu_list, k=1, weights=w)
    st.write(aisatu[0])

    # 今日のスクワット
    def get_random_squat_count():
        return random.randint(10, 1000)
    # ランダムなスクワット回数を取得
    squat_count = get_random_squat_count()
    # 画面に表示
    st.write(f"P.S.本日は片足：{squat_count}回のブルガリアンスクワットをします")

        
    
