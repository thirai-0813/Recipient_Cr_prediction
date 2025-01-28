import streamlit as st
import numpy as np

# Median計算用関数
def calculate_median(values):
    return np.median(values)

# タイトルと概要
st.title("移植後2週間目の予測Cr値")
st.write("""
このアプリは術前のドナー、レシピエントのデータを入力して
移植後2週間目のクレアチニン値を計算するツールです。
""")

# ユーザー入力
DonorAge = st.number_input("Donor Age (ドナーの年齢)", min_value=0.0, value=30.0, step=1.0)
preCre = st.number_input("Pre-creatinine (ドナーの術前クレアチニン値)", min_value=0.0, value=1.0, step=0.1)
RecipentHeight = st.number_input("Recipient Height (レシピエントの身長)", min_value=0.0, value=170.0, step=1.0)
RecipientMale = st.selectbox("Recipient Male (レシピエントの性別)", options=[0, 1], format_func=lambda x: "男性" if x == 1 else "女性")
DonorVolumeofExcisedKidney = st.number_input("Donor Volume of Excised Kidney (ドナー提供腎の体積)", min_value=0.1, value=150.0, step=1.0)
HLAAmismatch = st.number_input("HLA-A Mismatch (HLA-Aミスマッチ数)", min_value=0, value=2, step=1)
RecipientAge = st.number_input("Recipient Age (レシピエントの年齢)", min_value=0.0, value=50.0, step=1.0)

# 計算ボタン
if st.button("計算する"):
    try:
        # 各式を計算してリストに格納
        values = [
            0.987905 + (0.000174027 * DonorAge * preCre * RecipentHeight * RecipientMale * 116.25) /
            (DonorVolumeofExcisedKidney * (1.771 + HLAAmismatch)),
            -1.53277 + (0.00733625 * DonorAge) + (77.7114 / DonorVolumeofExcisedKidney) +
            (0.00115201 * 14.0) + (0.0111148 * RecipentHeight) +
            (0.118117 * 0.0) - (0.00614365 * RecipientAge) +
            (0.353654 * RecipientMale),
            0.986798 + (0.00302141 * DonorAge * (4 - HLAAmismatch) * preCre * RecipentHeight * RecipientMale) /
            DonorVolumeofExcisedKidney,
            -0.882776 + (74.8909 / DonorVolumeofExcisedKidney) -
            (0.076707 * HLAAmismatch) + (0.0100095 * RecipentHeight) -
            (0.00315926 * RecipientAge) +
            (0.00783757 * DonorAge * preCre * RecipientMale),
            -1.57956 + (0.00672586 * DonorAge) + (71.0255 / DonorVolumeofExcisedKidney) -
            (0.0953619 * HLAAmismatch) + (0.0112839 * RecipentHeight) +
            (0.418101 * preCre * RecipientMale),
            -0.879596 + (73.9811 / DonorVolumeofExcisedKidney) -
            (0.0944157 * HLAAmismatch) + (0.00915676 * RecipentHeight) +
            (0.0000474954 * DonorAge * preCre * RecipentHeight * RecipientMale),
            -1.02652 + (72.5871 / DonorVolumeofExcisedKidney) -
            (0.0954122 * HLAAmismatch) + (0.0101525 * RecipentHeight) +
            (0.0000306179 * DonorAge**2 * RecipientMale) +
            (0.00508625 * DonorAge * preCre * RecipientMale),
            -1.1774 + (0.00690542 * DonorAge) + (3422.33 / DonorVolumeofExcisedKidney) -
            (0.0731686 * HLAAmismatch) + (0.0100687 * RecipentHeight) -
            (3415.66 / (DonorVolumeofExcisedKidney + 60.0 / RecipientAge)) +
            (0.263214 * RecipientMale),
            0.989414 + (0.0294984 * DonorAge * preCre * RecipientMale**2 * 116.25) /
            (DonorVolumeofExcisedKidney * (1.771 + HLAAmismatch)),
            -0.16405 - (0.0020643 * DonorVolumeofExcisedKidney) -
            (0.099984 * HLAAmismatch) + (0.00983841 * RecipentHeight) +
            ((1.13413 * DonorAge * preCre * RecipientMale) / DonorVolumeofExcisedKidney),
            0.00780254 - (0.00199575 * DonorVolumeofExcisedKidney) -
            (0.0987313 * HLAAmismatch) + (0.00867225 * RecipentHeight) +
            ((0.00697395 * DonorAge * preCre * RecipentHeight * RecipientMale) / DonorVolumeofExcisedKidney)
        ]
        
        # Medianの計算
        median_average = calculate_median(values)

        # 小数点2桁にフォーマット
        formatted_result = round(median_average, 2)

        st.success(f"あなたの移植後2週間目の予測クレアチニン値は以下の通りです（単位mg/dL): {formatted_result}")

        # 注意書き
        st.write("""
        **この結果は東京女子医科大学泌尿器科で実際に腎提供された患者さまのデータを元に算出しています。
        実際の測定値とは異なる可能性があることをご了承ください。**
        """)
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")



