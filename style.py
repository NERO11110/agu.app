# style.py
import streamlit as st

def apply_custom_css():
  st.markdown("""
    <!-- かわいい丸ゴシックフォントを読み込み -->
    <link href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@500;700;900&display=swap" rel="stylesheet">

    <style>
    /* 全体背景：明るいクリーンホワイト */
    .stApp {
        background-color: #FAFAFA !important;
        font-family: 'Zen Maru Gothic', -apple-system, sans-serif !important;
    }

    /* 文字色を黒・濃いグレーに統一して視認性を確保 */
    body, p, span, div, label, .stMarkdown {
        color: #1F2937 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
    }

    /* タイトル類（濃い黒でクッキリ） */
    h1, h2, h3, h4, h5, h6 {
        color: #111827 !important;
        font-weight: 900 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
    }

    /* 正方形ボタン：白カード枠にクッキリした黒文字 */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button {
        width: 100% !important;
        aspect-ratio: 1 / 1 !important; /* 完全な正方形 */
        height: auto !important;
        background-color: #FFFFFF !important;
        border: 2px solid #E5E7EB !important;
        border-radius: 20px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        padding: 12px !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* ボタンホバー時 */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button:hover {
        border-color: #059669 !important;
        background-color: #ECFDF5 !important;
        box-shadow: 0 8px 20px rgba(5, 150, 105, 0.15) !important;
        transform: translateY(-3px) !important;
    }

    /* ボタンの中のテキスト（大きな濃い黒文字） */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button p {
        color: #111827 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
        font-size: 1.4rem !important; /* 大きなフォント */
        font-weight: 900 !important;
        line-height: 1.4 !important;
        margin: 0 !important;
    }

    /* 通常のStreamlitボタン（「← ホームに戻る」等）の視認性強化 */
    .stButton > button {
        background-color: #FFFFFF !important;
        color: #111827 !important;
        border: 2px solid #D1D5DB !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
    }
    .stButton > button:hover {
        border-color: #059669 !important;
        color: #059669 !important;
    }

    /* 全体コンテナ幅の最適化 */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 520px !important;
    }
    </style>
    """, unsafe_allow_html=True)
