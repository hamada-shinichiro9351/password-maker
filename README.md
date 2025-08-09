# パスワード生成器

Pythonで作成された安全で使いやすいパスワード生成器です。GUI版とコマンドライン版の両方を提供しています。

## 機能

- 🔐 カスタマイズ可能なパスワード生成
- 📊 パスワード強度の評価
- �� クリップボードへのワンクリックコピー（pyperclip使用時）
- 📚 パスワード履歴の保存と管理
- 🖥️ GUI版とコマンドライン版の両方を提供

## 前提条件

### Pythonのインストール

1. **Python 3.6以上**をインストールしてください
   - [Python公式サイト](https://www.python.org/downloads/)からダウンロード
   - インストール時に「Add Python to PATH」にチェックを入れてください

2. **インストール確認**
   ```bash
   python --version
   # または
   python3 --version
   ```

## インストール

1. リポジトリをクローンまたはダウンロード
2. プロジェクトディレクトリに移動
3. オプション：クリップボード機能を使用する場合は依存関係をインストール

```bash
# クリップボード機能を使用する場合（オプション）
pip install pyperclip
```

**注意**: 標準ライブラリのみでも動作しますが、クリップボード機能は使用できません。

## 使用方法

### GUI版

```bash
python password_generator.py
```

**機能：**
- パスワード長の設定（デフォルト：12文字）
- 文字種の選択（大文字、小文字、数字、記号）
- パスワード強度の表示
- パスワードの選択（手動コピー）
- パスワード履歴の保存と管理

### コマンドライン版

**基本的な使用方法：**
```bash
python password_generator_cli.py
```

**オプション付き：**
```bash
# 16文字のパスワードを生成
python password_generator_cli.py -l 16

# 記号なしでパスワードを生成
python password_generator_cli.py --no-symbols

# 20文字のパスワードを5個生成
python password_generator_cli.py -l 20 -c 5

# 強度を表示してパスワードを生成
python password_generator_cli.py --show-strength
```

**利用可能なオプション：**
- `-l, --length`: パスワードの長さ（デフォルト：12）
- `-c, --count`: 生成するパスワードの数（デフォルト：1）
- `--no-uppercase`: 大文字を使用しない
- `--no-lowercase`: 小文字を使用しない
- `--no-digits`: 数字を使用しない
- `--no-symbols`: 記号を使用しない
- `--show-strength`: パスワードの強度を表示

## パスワード強度の評価基準

パスワードの強度は以下の基準で評価されます：

- **弱い**: スコア2以下
- **普通**: スコア3-4
- **強い**: スコア5-6

**スコアの計算：**
- 8文字以上: +1点
- 12文字以上: +1点
- 大文字を含む: +1点
- 小文字を含む: +1点
- 数字を含む: +1点
- 記号を含む: +1点

## ファイル構成

```
password_generator/
├── password_generator.py      # GUI版メインアプリケーション
├── password_generator_cli.py  # コマンドライン版
├── test_password_generator.py # テストスクリプト
├── simple_test.py            # 簡単なテストスクリプト
├── requirements.txt           # 依存関係（オプション）
├── README.md                 # このファイル
└── password_history.json     # パスワード履歴（自動生成）
```

## セキュリティについて

- 生成されたパスワードはローカルにのみ保存されます
- 履歴ファイルは暗号化されていないため、機密性の高い環境では注意してください
- パスワード履歴は最新の20件まで保持されます

## 技術仕様

- **Python**: 3.6以上
- **GUI**: tkinter（標準ライブラリ）
- **クリップボード**: pyperclip（オプション）
- **データ保存**: JSON

## トラブルシューティング

### Pythonが見つからない場合

1. Pythonがインストールされているか確認：
   ```bash
   python --version
   ```

2. PATHにPythonが追加されているか確認：
   ```bash
   where python
   ```

3. 必要に応じてPythonを再インストールし、「Add Python to PATH」にチェックを入れる

### モジュールが見つからない場合

標準ライブラリのみを使用するため、追加のインストールは不要です。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 貢献

バグ報告や機能提案は歓迎します。プルリクエストも受け付けています。
