"""
promptで入力されたワードを基に、NUM_OF_PNGSで指定された数のバリエーションで画像を編集し、ファイル名を指定して画像を保存するスクリプト
"""

import openai
import os
from PIL import Image
import requests
from io import BytesIO
from dotenv import load_dotenv
import io

#環境変数からOpenAIのAPIキー読み込み
load_dotenv(override=True)
openai.api_key = os.getenv("openai_api_key")

# 生成する編集パターンの数
NUM_OF_PNGS = 3

# 元画像とマスク画像を準備し、PILで開く
original_img = Image.open("output.png")
masked_img = Image.open("masked.png")

# 画像形式を'RGBA'に変換
original_img = original_img.convert("RGBA")
masked_img = masked_img.convert("RGBA")

# Imageオブジェクトをバイト列に変換
def convert_img_objects(img_object):
  img_byte_arr = io.BytesIO()
  img_object.save(img_byte_arr, format='PNG')
  img_byte_arr = img_byte_arr.getvalue()
  return img_byte_arr

original_img_arr = convert_img_objects(original_img)
masked_img_arr = convert_img_objects(masked_img)

# テキストプロンプトを設定
prompt = 'Some trees in the background.'

# OpenAIのモデルを使用して画像を編集
response = openai.Image.create_edit(
  # image=original_img,
  image=original_img_arr,
  # image=Image.open(BytesIO(original_img)),
  mask=masked_img_arr,
  prompt=prompt,
  n=NUM_OF_PNGS,
  size="512x512",   # 画像のサイズを文字列で設定
)

# 生成された画像をすべて取得し保存
for i in range(NUM_OF_PNGS):
  # 生成された画像のURLを取得
  image_url = response['data'][i]['url']

  # 画像をダウンロード
  response_img = requests.get(image_url)
  img = Image.open(BytesIO(response_img.content))

  # ファイル名を指定して画像を保存
  output_file = f"output_{i}.png"
  img.save(output_file)  

  print(f"Output file({i}): {output_file}")
