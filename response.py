



import streamlit as st

# タイトルの設定
st.title('悩み相談アプリ')

# ユーザー入力の受け取り
user_input = st.text_input("あなたの悩みを教えてください:")

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
    response = generate_response(user_input)
    st.write(response)
