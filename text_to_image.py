"""
promptで入力されたワードを基にOpenAIのモデルを使って画像生成、ファイル名を指定して画像を保存するスクリプト
"""

import openai
import os
from PIL import Image
import requests
from io import BytesIO
from dotenv import load_dotenv

#環境変数からOpenAIのAPIキー読み込み
load_dotenv(override=True)
openai.api_key = os.getenv("openai_api_key")

# テキストプロンプトを設定
prompt = 'A walking chicken.'

# OpenAIのモデルを使用して画像を生成
response = openai.Image.create(
  prompt=prompt,
  size="512x512",   # 画像のサイズを文字列で設定
)

# 生成された画像のURLを取得
image_url = response['data'][0]['url']

# 画像をダウンロードして保存
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))

# ファイル名を指定して画像を保存
output_file = "output.png"
img.save(output_file)  

print(f"Output file: {output_file}")
