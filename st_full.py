

import csv
import streamlit as st
import random

#---悩み相談入力-------------------------------------------------------------------#


# タイトルの設定
st.title('悩み相談アプリ')

# ユーザー入力の受け取り
user_input = st.text_input("あなたの悩みを教えてください:")

#---悩みへの応答-------------------------------------------------------------------＃
def generate_response(user_input):
    # 悩みのキーワードに基づいた応答の生成
    if "仕事" in user_input:
        return "仕事の悩みは多様ですが、具体的な対策が効果的です。例えば、タスクの整理や時間管理の見直しにより、仕事の効率を上げることが可能です。また、ストレスを感じたら適切な休息を取ることも大切です。"
    elif "恋愛" in user_input:
        return "恋愛における悩みはデリケートですが、対話が鍵となります。例えば、感じている不安や期待をパートナーに正直に伝えることで、理解し合える可能性が高まります。信頼とコミュニケーションが大切です。"
    elif "健康" in user_input:
        return "健康の悩みは個々の生活習慣や体質に大きく左右されます。例えば、バランスの良い食事と適度な運動を組み合わせることで、体調を改善することが期待できます。また、十分な休息も重要です。"
    else:
        return "あなたの悩みについてもっと詳しく教えてください。もっと具体的なアドバイスができるかもしれません。"

# 入力がある場合に応答を表示
if user_input:
    input_text = generate_response(user_input)
#    st.write(response)
    # リクエストデータのためのPydanticモデル
    # このモデルは、クライアントから受け取るデータの構造を定義します


    
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
    f = open('名言.txt','r',encoding='UTF-8')
    meigenn_list = f.readlines()
    meigenn = random.choice(meigenn_list)
    st.write('今日の名言は「',meigenn,'」です')

    # 最後の挨拶
    g = open('最後の挨拶.txt','r',encoding='UTF-8')
    aisatu_list = g.readlines()
    ran_list = [0, 1]
    w = [1, 5]
    aisatu = random.choices(aisatu_list, k=1, weights=w)
    print(aisatu[0])
    st.write(aisatu[0])

    # 今日のスクワット
    def get_random_squat_count():
        return random.randint(10, 1000)
    # ランダムなスクワット回数を取得
    squat_count = get_random_squat_count()
    # 画面に表示
    st.write(f"P.S.本日は片足：{squat_count}回のブルガリアンスクワットをします")