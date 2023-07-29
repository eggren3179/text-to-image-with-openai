# OpenAIのAPIを利用した画像生成コード
OpenAIのAPIを利用して文字列から画像を生成するコードのサンプルです。Githubアカウントのアイコンはこのスクリプトにより作成しました。
 ## 0. 事前準備
  - 任意のディレクトリでgit cloneする
    ```bash
    git clone https://github.com/eggren3179/text-to-image-with-openai.git
    ```
  - リポジトリのディレクトリに移動し、下記コマンドにより実行環境を準備する。
    ```bash
    pip install -r requirements.txt
    ```
  - OpenAIのAPIキーを取得し、.envファイルに下記のように環境変数を設定する。 
    > openai_api_key='YOUR_OPEN_API_KEY'

 ## 1. 実行方法
  - 下記コマンドによりOpenAIのAPIを利用して画像を生成し、画像ファイルに保存する。
    ```bash
    python text_to_image.py
    ```
  - 上記の実行結果として、保存された画像ファイル名が出力されるので画像を確認する。
    ```bash
    # 実行例
    $ python text_to_image.py
    Output file:output.png
    ```
  