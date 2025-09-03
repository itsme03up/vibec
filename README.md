📊 Streamlit Data App Monorepo

Python を始めたばかりの人でも楽しく学べる データ可視化アプリ です。
Streamlit を使い、CSVファイルをアップロードすると表やグラフが表示されます。

🚀 使用技術

Python 3.10+

Streamlit → Webアプリフレームワーク

pandas → CSVやデータ解析

TailwindCSS（必要なら） → 見た目の調整

shadcn/ui（必要なら） → UIコンポーネント

📂 ディレクトリ構成（モノレポ）
streamlit-data-app/
├── README.md
├── apps/
│   └── csv_viewer/
│       ├── app.py
│       ├── requirements.txt
│       └── sample.csv
├── frontend/          # 見た目拡張用（任意）
└── docs/
    └── guide.md


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

📖 サンプルアプリの使い方

CSVをアップロードすると表で表示

数値カラムを選ぶと グラフ表示

describe() で 統計情報（平均・最大・最小）を確認

✅ requirements.txt
streamlit
pandas

📝 サンプルコード（apps/csv_viewer/app.py）
import streamlit as st
import pandas as pd

st.title("📊 CSV可視化アプリ")

# ファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

if uploaded_file:
    # データ読み込み
    df = pd.read_csv(uploaded_file)

    st.subheader("データプレビュー")
    st.dataframe(df.head())

    st.subheader("統計情報")
    st.write(df.describe())

    st.subheader("グラフ表示")
    column = st.selectbox("カラムを選択してください", df.columns)
    if pd.api.types.is_numeric_dtype(df[column]):
        st.line_chart(df[column])
    else:
        st.warning("数値カラムを選んでください")
else:
    st.info("サンプルCSVを使うときは `sample.csv` をアップロードしてみましょう！")
