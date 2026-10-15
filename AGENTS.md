# harness-init-trial-py の規約

ハーネスの版: 1

この行は、このプロジェクトにハーネス（規約と検査の一式）を導入済みであることを示す印である。
`scripts/harness/check-docs.sh` が、この版で必須のファイルが揃っているかを確かめる。印の書式（「ハーネスの版: 」に
整数を続けた 1 行）は、ハーネスの規約が定めたものに合わせている。版の数は、必須のファイルが増えるときに上げ、
同じ変更で `check-docs.sh` の版ごとの一覧を足す。

## このプロジェクト

文章の語を数え、回数の多い語を出す小さなコマンド `wordtally` である。Python の標準ライブラリだけで書いた、
ハーネスの導入を試すためのサンプルである（`README.md`）。

使うのは、ハーネスの導入を試す開発者（このリポジトリの所有者）1 人だけである。ほかの人に使ってもらうことも、
配布することも想定しない。

## コードから推測できない決定

- 標準ライブラリだけを使う。外部のパッケージを足すときは、先に利用者へ相談する（`CLAUDE.md`）。
- Python 3.9 以上で動く形を保つ（`pyproject.toml`。CI で試験を実行する版は `.github/workflows/ci.yml`）。
- `src/wordtally/core.py` には入出力を置かない。入出力は `cli.py` に置き、依存の向きは `cli.py` から `core.py` への一方向だけにする（`ARCHITECTURE.md`）。

## 秘匿値と個人情報（必須）

- 秘匿値（API の鍵、トークン、Cookie、パスワード）をリポジトリのファイルに書かない。
- `.env` で始まるファイルは `.gitignore` で除外する。例外は、変数の名前だけを書く `.env.example` だけで、値は書かない。
- CI の `secret-scan`（`.github/workflows/secret-scan.yml`）が gitleaks で履歴の全体を調べる。秘匿値が検出されるとジョブが失敗する。
  検出された秘匿値は、発行元で失効させて再発行する（push した時点で公開されているため）。失効させた後と誤検知のときは、
  gitleaks が出す指紋（Fingerprint）を `.gitleaksignore` に足して、検査を通る状態に戻す。
- `.gitleaksignore`、`.gitleaks.toml`、行の中の `gitleaks:allow`、`.github/workflows/secret-scan.yml` を変える変更は、
  検査を通すために秘匿値を見逃す形になっていないかを、レビューで必ず確かめる。
- コミットするファイルに個人情報（アカウント名、姓名、メールアドレス）とホームの絶対パスを書かない。パスは `~/...` か
  プレースホルダーで書く。

## 検査のコマンド

| 何を確かめるか | コマンド |
|---|---|
| 全部（手元の Python で、試験と文書の検査を順に実行する。CI は Python 3.9 と 3.12 の 2 つの版で試験を実行し、gitleaks は別の検査で実行するので、この 1 行には含まない） | `python3 -m unittest && bash scripts/harness/check-docs.sh && bash scripts/harness/check-docs.test.sh` |
| lint | なし |
| 型 | なし |
| 試験 | `python3 -m unittest` |
| 文書（必須のファイル、CLAUDE.md、地図、リンク、目録、行数、計画の必須の節、受け入れ確認の記録、製品の仕様の目録と状態） | `bash scripts/harness/check-docs.sh` |
| 文書の検査の試験（`check-docs.sh` の計画、受け入れ確認の記録、仕様の検査） | `bash scripts/harness/check-docs.test.sh` |
| 秘匿値の混入（CI で実行。手元で実行するには gitleaks の導入が要る） | `gitleaks git --redact` |

リンクの検査が見るのは、インラインのリンクと画像（角括弧の文字の直後に、丸括弧で囲んだ先を続ける形）で、先に空白も
`)` も含まないものだけである。参照形式のリンク、山括弧で囲んだ先、タイトル付きの先、自動リンク、HTML の a 要素は検査しないので、
文書の中のリンクはインラインの形で書く。

## 文書の地図

| 種類 | パス | 読む条件 |
|---|---|---|
| 設計の正本（層、依存の向き、不変条件） | `ARCHITECTURE.md` | コードを変える前 |
| 設計判断の記録 | `docs/adr/README.md` | 設計を変える前、過去の判断の理由を知りたいとき |
| 製品の前提 | `docs/PRODUCT_SENSE.md` | 新しい機能や画面を考えるとき |
| 製品の仕様（書式と目録） | `docs/product-specs/README.md` | 新しい機能や画面の仕様を書くとき、仕様を引く計画を書くとき・確かめるとき |
| 計画の書式 | `docs/PLANS.md` | 計画を書くとき、計画を読むとき |
| アプリの起動の手順 | `.claude/skills/run-harness-init-trial-py/SKILL.md` | アプリを起動して画面を確かめるとき（受け入れ確認を含む） |
| 進行中の計画 | `docs/exec-plans/active/` | 作業を再開するとき |
| 完了した計画 | `docs/exec-plans/completed/` | 過去の作業の経緯を知りたいとき |
| 品質目標 | `docs/QUALITY_SCORE.md` | 設計の品質を判断するとき |

## 落とし穴

- Claude Code は、`CLAUDE.md` があるとこのファイルを自分からは読まない。そのため `CLAUDE.md` に `@AGENTS.md` だけの行を
  置いている。この行を消さず、指示はこのファイルに書く（`bash scripts/harness/check-docs.sh` が、`@AGENTS.md` だけの行があることを確かめる）。
