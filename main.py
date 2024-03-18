# FastAPIサーバーサイド
from fastapi import FastAPI
from pydantic import BaseModel
import csv

# FastAPIインスタンスの作成
app = FastAPI()

# リクエストデータのためのPydanticモデル
# このモデルは、クライアントから受け取るデータの構造を定義します
class Message(BaseModel):
    text: str  # ユーザーからのメッセージテキスト
    style: str  # ユーザーが選択するスタイル

# POSTリクエストを処理するためのルート
# "/convert/" はクライアントからのメッセージ変換リクエストを処理します
    
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
file_path = 'C:\\folder\\make\\Python\\yosinani\\口癖辞書.csv'

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

@app.post("/convert/")
async def convert_message(message: Message):
    converted_text = convert_text(message.text, message.style)
    return {'converted_text':converted_text}

    # ここでメッセージを特定のスタイルに変換
    # 現在は、単に受け取ったメッセージをそのまま返している
    # 本番では、ここに変換ロジックを実装する