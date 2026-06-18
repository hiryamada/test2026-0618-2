# test2026-0618-2

## プロジェクト概要
FastAPI を使って、天気予報の文字列を返すシンプルな API を提供するプロジェクトです。  
初期実装として、引数なしで固定文字列 `晴れ` を返します。

## 構成
```text
.
├── src/
│   └── main.py          # FastAPI アプリ本体
├── tests/
│   └── test_main.py     # 単体テスト
└── requirements.txt     # 依存関係
```

## 実行方法
1. 依存関係をインストールします。
   ```bash
   pip install -r requirements.txt
   ```
2. API サーバーを起動します。
   ```bash
   uvicorn src.main:app --reload
   ```
3. 以下にアクセスすると、`{"forecast":"晴れ"}` が返ります。
   - `http://127.0.0.1:8000/weather`

## 単体テスト実行方法
以下のコマンドで pytest を実行できます。

```bash
pytest -q
```