


#---悩み相談入力-------------------------------------------------------------------#
import streamlit as st

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
# Streamlitクライアントサイド
import streamlit as st
import requests
import random

#st.title('口調変換アプリ')

#input_text = st.text_area("メッセージを入力してください")
style = st.selectbox("スタイルを選択してください", ["スタイル1", "スタイル2", "スタイル3"])
if st.button('相談'):
    response = requests.post("http://localhost:8000/convert/", json={"text": input_text, "style": style})
    if response.status_code == 200:
        st.write(response.json()['converted_text'])

    #名言
    f = open('C:\\folder\\make\\Python\\yosinani\\名言.txt','r',encoding='UTF-8')
    meigenn_list = f.readlines()
    meigenn = random.choice(meigenn_list)
    st.write('今日の名言は「',meigenn,'」です')

    # 最後の挨拶
    g = open('C:\\folder\\make\\Python\\yosinani\\最後の挨拶.txt','r',encoding='UTF-8')
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