import streamlit as st
import numpy as np

# Median計算用関数
def calculate_median(values):
    return np.median(values)

# StreamlitアプリのUI
st.title("MedianAverage計算ツール")

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
    # 各式を計算してリストに格納
    values = [
        0.987905 + (0.000174027 * DonorAge * preCre * RecipentHeight * RecipientMale * 116.25) /
        (DonorVolumeofExcisedKidney * (1.771 + HLAAmismatch)),
        -1.53277 + (0.00733625 * DonorAge) + (77.7114 / DonorVolumeofExcisedKidney) +
        (0.00115201 * 14.0) + (0.0111148 * Recip







