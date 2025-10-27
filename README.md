# 通貨換算アプリ 操作マニュアル 

## 概要
このアプリは、Exchange Rate APIを使用して日本円（JPY）を韓国ウォン（KRW）やシンガポールドル（SGD）に換算するツールです。逆方向の換算も可能です。GUIベースで動作します。

## 必要環境
- Python 3.x（Tkinter標準搭載）
- requestsライブラリ（`pip install requests`）
- Exchange Rate APIのAPIキー（環境変数 `EXCHANGE_RATE_API_KEY` に設定）

## インストールと実行
1. リポジトリをクローン: `git clone https://github.com/Toshikakeki/currency-converter-app.git`
2. ディレクトリに移動: `cd currency-converter-app`
3. APIキーを設定: `export EXCHANGE_RATE_API_KEY=your_api_key_here`（Windowsの場合は `set`）
4. 実行: `python currency_converter_gui.py`

## 使用方法
1. アプリ起動後、ウィンドウが開きます。
2. 「換算モード」ドロップダウンからモードを選択（例: 円 → ウォン）。
3. 「金額」フィールドに数値を入力（例: 100）。
4. 「換算」ボタンをクリック。
5. 「結果」ラベルに換算結果が表示されます。
6. 終了するには「終了」ボタンをクリック。

## 注意事項
- レートはAPIからリアルタイム取得（無料プランは1日1回更新）。
- 金額は数値のみ入力してください。
- API制限を超えるとエラーメッセージが表示されます。
