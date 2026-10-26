# style.py
import streamlit as st


def apply_custom_css():
  st.markdown(
      """
    <!-- 丸ゴシックフォントの読み込み -->
    <link href="https://fonts.googleapis.com/css2?family=Zen+Maru Gothic:wght@500;700;900&display=swap" rel="stylesheet">

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

    /* ★★★ スマホ（モバイル）での1列化を強力に打ち消すCSS ★★★ */
    [data-testid="stColumn"] {
        width: calc(50% - 6px) !important;
        min-width: calc(50% - 6px) !important;
        max-width: calc(50% - 6px) !important;
        flex: 1 1 calc(50% - 6px) !important;
    }

    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 12px !important;
        width: 100% !important;
    }

    /* 画面がどれだけ狭くても横並びを維持 */
    @media (max-width: 640px) {
        [data-testid="stColumn"] {
            width: calc(50% - 6px) !important;
            min-width: calc(50% - 6px) !important;
            flex: 1 1 calc(50% - 6px) !important;
        }
        [data-testid="stHorizontalBlock"] {
            flex-direction: row !important;
        }
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
        padding: 6px !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* ホバー時 */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button:hover {
        border-color: #059669 !important;
        background-color: #ECFDF5 !important;
        box-shadow: 0 8px 20px rgba(5, 150, 105, 0.15) !important;
        transform: translateY(-2px) !important;
    }

    /* ボタン内のテキスト（スマホ画面サイズにぴったりフィット） */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button p {
        color: #111827 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
        font-size: clamp(1.1rem, 4.5vw, 1.4rem) !important;
        font-weight: 900 !important;
        line-height: 1.2 !important;
        margin: 0 !important;
    }

    /* 通常ボタン（← ホームに戻る など） */
    .stButton > button {
        background-color: #FFFFFF !important;
        color: #111827 !important;
        border: 2px solid #D1D5DB !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
    }

    /* コンテナの余白調整 */
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
        max-width: 520px !important;
    }
    </style>
    """,
      unsafe_allow_html=True,
  )