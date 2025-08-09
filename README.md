# 🔐 パスワードメーカー

安全で使いやすいパスワード生成ツール。カスタマイズ可能なパスワード生成・強度評価・履歴管理で、セキュアなパスワード作成を実現。

## 🌐 ライブデモ

**[🔗 パスワードメーカーを試す](https://hamada-shinichiro9351.github.io/password-maker/)**

GitHub PagesでホストされているWeb版デモです。ブラウザ上でパスワード生成、強度評価、コピー機能をお試しください。

## 🎯 主な機能

- 🔐 カスタマイズ可能なパスワード生成
- 📊 パスワード強度の評価システム
- 📋 クリップボードへのワンクリックコピー
- 📚 パスワード履歴の保存と管理
- 🖥️ GUI版とコマンドライン版の両方を提供
- 🌐 Web版デモ（ブラウザ上で動作）
- 🔤 文字種の選択（大文字・小文字・数字・記号）
- 📏 パスワード長のカスタマイズ

## 🛠️ 技術スタック

- **Python 3.13.6** - メイン言語
- **tkinter** - GUIフレームワーク（標準ライブラリ）
- **argparse** - コマンドライン引数処理
- **random** - ランダムパスワード生成
- **string** - 文字列操作
- **json** - データ保存
- **os** - ファイル操作
- **datetime** - タイムスタンプ

## 🚀 クイックスタート

### 1. リポジトリのクローン

```bash
git clone https://github.com/yourusername/password-maker.git
cd password-maker
```

### 2. アプリケーションの実行

**GUI版（推奨）：**
```bash
python password_generator.py
```

**コマンドライン版：**
```bash
python password_generator_cli.py
```

**Web版デモ：**
- ブラウザで `index.html` を開く
- または [GitHub Pages](https://hamada-shinichiro9351.github.io/password-maker/) にアクセス

## 📖 使用方法

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

## 📊 パスワード強度の評価基準

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

## 🌐 Web版デモ

プロジェクトにはWeb版のデモも含まれています：

- **ファイル**: `index.html`
- **機能**: ブラウザ上でパスワード生成、強度評価、コピー機能
- **アクセス**: 
  - ローカル: ブラウザで `index.html` を開く
  - オンライン: [GitHub Pages](https://hamada-shinichiro9351.github.io/password-maker/)

## 📁 プロジェクト構造

```
password-maker/
├── index.html                     # Web版デモ（GitHub Pages用）
├── password_generator_web.html    # Web版デモ（元ファイル）
├── password_generator.py          # GUI版メインアプリケーション
├── password_generator_cli.py      # コマンドライン版
├── test_password_generator.py     # テストスクリプト
├── requirements.txt               # 依存関係（標準ライブラリのみ）
├── README.md                      # このファイル
└── .gitignore                     # Git除外ファイル
```

## 🔧 開発・貢献

### ローカル開発環境のセットアップ

1. リポジトリをクローン
2. Python 3.13.6以上をインストール
3. プロジェクトディレクトリに移動
4. アプリケーションを実行

```bash
git clone https://github.com/yourusername/password-maker.git
cd password-maker
python password_generator.py  # GUI版
python password_generator_cli.py  # CLI版
```

### テスト

```bash
python test_password_generator.py
```

## 🎨 アーキテクチャ

- **MVCパターンの採用**: モデル、ビュー、コントローラーの分離
- **モジュラー設計**: 保守性の向上
- **共通ロジックの分離**: GUI版とCLI版で共通のパスワード生成ロジック
- **標準ライブラリのみ使用**: 外部依存関係なし

## 📈 パフォーマンス

- **軽量**: 標準ライブラリのみ使用
- **高速**: 即座にパスワード生成
- **効率的**: 最小限のメモリ使用量

## 🔒 セキュリティ

- **ローカル実行**: パスワードはローカルでのみ生成・保存
- **履歴管理**: パスワード履歴はJSON形式でローカル保存
- **強度評価**: 包括的なパスワード強度評価システム

## 🚀 デプロイ

### GitHub Pages

このプロジェクトはGitHub Pagesでホストされています：

- **URL**: https://hamada-shinichiro9351.github.io/password-maker/
- **ファイル**: `index.html`がメインページとして表示されます

### ローカルデプロイ

1. リポジトリをクローン
2. `index.html`をブラウザで開く
3. または、ローカルサーバーを起動

```bash
# Pythonの簡易サーバーを使用
python -m http.server 8000
# ブラウザで http://localhost:8000 にアクセス
```

## 📞 サポート

問題が発生した場合は：

1. **GitHub Issues**で問題を報告
2. **ブラウザの開発者ツール**でエラーを確認
3. **Pythonバージョン**を確認（3.13.6以上）

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 👨‍💻 作者

- **開発者**: [Your Name]
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **プロジェクト**: [パスワードメーカー](https://github.com/yourusername/password-maker)

## 🙏 謝辞

- Pythonコミュニティ
- tkinter開発チーム
- オープンソースコミュニティ

---

**⭐ このプロジェクトが役に立ったら、スターを付けてください！**
