# style.py
import streamlit as st


def apply_custom_css():
  st.markdown(
      """
    <!-- 丸ゴシックフォントの読み込み -->
    <link href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@500;700;900&display=swap" rel="stylesheet">

    <style>
    /* 全体背景：クリーンホワイト */
    .stApp {
        background-color: #FAFAFA !important;
        font-family: 'Zen Maru Gothic', -apple-system, sans-serif !important;
    }

    /* 文字色・タイトル統一 */
    body, p, span, div, label, .stMarkdown {
        color: #1F2937 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #111827 !important;
        font-weight: 900 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
    }

    /* ★ スマホ画面でもカラムの縦並び（折り返し）を防止して強制2列表示にする設定 */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 12px !important;
    }
    [data-testid="stColumn"] {
        width: 50% !important;
        min-width: 0 !important;
        flex: 1 1 50% !important;
    }

    /* 正方形ボタンのスタイリング */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button {
        width: 100% !important;
        aspect-ratio: 1 / 1 !important; /* 正方形 */
        height: auto !important;
        background-color: #FFFFFF !important;
        border: 2px solid #E5E7EB !important;
        border-radius: 18px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        padding: 8px !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* ホバー時の装飾 */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button:hover {
        border-color: #059669 !important;
        background-color: #ECFDF5 !important;
        box-shadow: 0 8px 20px rgba(5, 150, 105, 0.15) !important;
        transform: translateY(-2px) !important;
    }

    /* ボタン内のテキスト（スマホ画面サイズに合わせて文字サイズを最適化） */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button p {
        color: #111827 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
        font-size: clamp(1.1rem, 4vw, 1.4rem) !important; /* スマホ画面では自動で程よく縮小 */
        font-weight: 900 !important;
        line-height: 1.3 !important;
        margin: 0 !important;
    }

    /* 通常ボタンのスタイリング */
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

    /* 全体コンテナの幅調整 */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 520px !important;
    }
    </style>
    """,
      unsafe_allow_html=True,
  )
