import streamlit as st


def apply_custom_css():
    st.markdown(
        """
    <link href="https://fonts.googleapis.com/css2?family=Zen+Maru Gothic:wght@500;700;900&display=swap" rel="stylesheet">

    <style>
    /* 全体背景（白〜明るいグレーに固定） */
    html, body, .stApp, [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        font-family: 'Zen Maru Gothic', -apple-system, sans-serif !important;
        color: #0F172A !important;
    }

    /* 全テキスト要素の文字色固定 */
    p, span, div, label, h1, h2, h3, h4, h5, h6, .stMarkdown {
        color: #0F172A !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
    }

    /* 上部ヘッダー透明化 */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    /* アプリ枠幅調整 */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 440px !important;
        margin: 0 auto !important;
    }

    /* 白枠の角丸カードデザイン */
    .custom-card {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 20px !important;
        padding: 16px 20px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
        margin-bottom: 16px !important;
    }

    /* 通常ボタンのスタイリング */
    .stButton > button {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 16px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
        transition: all 0.2s ease !important;
        padding: 12px 16px !important;
        width: 100% !important;
    }
    
    /* ホーム画面の2x2ナビゲーションボタンを完全正方形化 */
    div[data-testid="stColumn"] .stButton > button {
        aspect-ratio: 1 / 1 !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        font-size: 1.15rem !important;
        white-space: pre-wrap !important;
        line-height: 1.3 !important;
        margin-bottom: 12px !important;
    }

    .stButton > button:hover {
        border-color: #10B981 !important;
        color: #10B981 !important;
        background-color: #ECFDF5 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 18px rgba(16, 185, 129, 0.12) !important;
    }

    /* テキスト入力フォーム（白背景に固定） */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
    }
    
    div[data-baseweb="input"] input {
        color: #0F172A !important;
        background-color: #FFFFFF !important;
    }

    /* アラート通知ボックス */
    div[data-testid="stNotification"] {
        border-radius: 14px !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
