# 構成

文章の語を数える小さなコマンドで、画面は無い。標準ライブラリだけを使う。

- `src/wordtally/core.py`: 語への分割（`tokenize`）、語ごとの回数（`count_words`）、回数の多い順の一覧（`top_words`）。
  入出力を持たない純粋な処理だけを置く。
- `src/wordtally/cli.py`: 引数の解釈と、ファイルか標準入力からの読み込み、結果の出力。処理は `core.py` を呼ぶ。
- `src/wordtally/__main__.py`: `python3 -m wordtally` の入口。
- `tests/`: 標準の `unittest` の試験。`tests/__init__.py` が `src` を読み込みの対象に足す。

依存の向きは `cli.py` から `core.py` への一方向だけで、`core.py` は `cli.py` を読み込まない。
