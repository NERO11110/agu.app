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

    /* ★★★ スマホ（画面幅に関わらず）強制2列（2x2）化の極小突破CSS ★★★ */
    
    /* 1. 横並び親コンテナの1列化解除 */
    div[data-testid="stHorizontalBlock"],
    div[data-testid="column"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 8px !important;
        width: 100% !important;
    }

    /* 2. 各カラム（列）の幅を強制的に50%へ固定 */
    div[data-testid="stColumn"],
    div[data-testid="column"],
    div[data-testid="stHorizontalBlock"] > div {
        width: calc(50% - 4px) !important;
        min-width: calc(50% - 4px) !important;
        max-width: calc(50% - 4px) !important;
        flex: 1 1 calc(50% - 4px) !important;
    }

    /* 3. モバイル画面幅のレスポンシブメディアクエリに対する完全上書き */
    @media (max-width: 768px) {
        div[data-testid="stHorizontalBlock"] {
            flex-direction: row !important;
            display: flex !important;
        }
        div[data-testid="stColumn"],
        div[data-testid="column"],
        div[data-testid="stHorizontalBlock"] > div {
            width: calc(50% - 4px) !important;
            min-width: calc(50% - 4px) !important;
            flex: 1 1 calc(50% - 4px) !important;
        }
    }

    /* 正方形ボタンのスタイリング */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button {
        width: 100% !important;
        aspect-ratio: 1 / 1 !important; /* 正方形 */
        height: auto !important;
        background-color: #FFFFFF !important;
        border: 2px solid #E5E7EB !important;
        border-radius: 16px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        padding: 4px !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* ホバー時 */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button:hover {
        border-color: #059669 !important;
        background-color: #ECFDF5 !important;
        box-shadow: 0 8px 20px rgba(5, 150, 105, 0.15) !important;
        transform: translateY(-2px) !important;
    }

    /* ボタン内のテキスト（スマホ画面サイズに合わせて文字を自動フィッティング） */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button p {
        color: #111827 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
        font-size: clamp(1.0rem, 4vw, 1.3rem) !important;
        font-weight: 900 !important;
        line-height: 1.2 !important;
        margin: 0 !important;
    }

    /* 通常ボタン */
    .stButton > button {
        background-color: #FFFFFF !important;
        color: #111827 !important;
        border: 2px solid #D1D5DB !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
    }

    /* コンテナの余白最適化 */
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 500px !important;
    }
    </style>
    """,
      unsafe_allow_html=True,
  )