📊 Streamlit Data App Monorepo

Python を始めたばかりの人でも楽しく学べる **強化版** データ可視化アプリ です。
Streamlit を使い、CSVファイルをアップロードすると表やグラフが表示されます。
**新機能**: 複数グラフタイプ、サイドバー設定、ダウンロード機能、美しいUIデザイン

🚀 使用技術

Python 3.10+

Streamlit → Webアプリフレームワーク

pandas → CSVやデータ解析

numpy → 数値処理

TailwindCSS（必要なら） → 見た目の調整

shadcn/ui（必要なら） → UIコンポーネント

📂 ディレクトリ構成（モノレポ）
streamlit-data-app/
├── README.md
├── apps/
│   └── csv_viewer/
│       ├── app.py          # メインアプリ（強化版UI）
│       ├── requirements.txt # 依存関係
│       └── sample.csv      # サンプルデータ
├── frontend/          # 見た目拡張用（任意）
└── docs/
    └── guide.md       # 詳細ガイド


👉 最初は apps/csv_viewer/app.py だけ触ればOKです。

🛠️ セットアップ方法
# 1. リポジトリを取得
git clone https://github.com/yourname/streamlit-data-app.git
cd streamlit-data-app/apps/csv_viewer

# 2. 仮想環境を作成
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3. 必要ライブラリをインストール
pip install -r requirements.txt

# 4. アプリを起動
streamlit run app.py


ブラウザが開いてアプリが動きます。

📖 強化版アプリの使い方

✅ **ファイルアップロード**
- CSVファイルをアップロード
- 「サンプルデータを使用」ボタンでテスト可能

✅ **データ概要**
- データの行数・列数・データ型数を確認
- 最初の10行をプレビュー表示

✅ **統計情報**
- pandas describe() で基本統計量を表示
- 平均・中央値・標準偏差などの詳細

✅ **ビジュアライゼーション**
- **グラフタイプ選択**: 折れ線グラフ・棒グラフ・面グラフ
- **カラム選択**: 数値カラムのみ表示可能
- **追加インサイト**: 選択カラムの平均・中央値・標準偏差

✅ **ダウンロード機能**
- 処理済みデータをCSVとしてダウンロード

🎨 **UI特徴**
- モダンなデザインとカラースキーム
- サイドバー設定パネル
- レスポンシブレイアウト
- インタラクティブなボタンとホバー効果

✅ requirements.txt
streamlit
pandas
numpy

📝 アプリの特徴（apps/csv_viewer/app.py）
- カスタムCSSによる美しいUI
- サイドバー設定（グラフタイプ選択など）
- 複数カラムレイアウト
- メトリクス表示
- データダウンロード機能
- エラーハンドリングの改善
