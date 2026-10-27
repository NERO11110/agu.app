import streamlit as st


def apply_custom_css():
    st.markdown(
        """
    <link href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@500;700;900&display=swap" rel="stylesheet">

    <style>
    /* 全体背景 */
    html, body, .stApp, [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        font-family: 'Zen Maru Gothic', -apple-system, sans-serif !important;
        color: #0F172A !important;
    }

    /* 文字色固定 */
    p, span, div, label, h1, h2, h3, h4, h5, h6, .stMarkdown {
        color: #0F172A !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
    }

    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 420px !important;
        margin: 0 auto !important;
    }

    /* 所持コインカード */
    .custom-card {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 18px !important;
        padding: 18px 24px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
        margin-bottom: 20px !important;
    }

    /* ========================================================
       ★ ボタン部分を【完全な正方形（1:1）】に強制するCSS (修正版)
       ======================================================== */
    /* ラッパーおよびボタン要素の高さ・余白制限を完全解除 */
    div[data-testid="stColumn"] div[data-testid="stButton"],
    div[data-testid="stColumn"] div[data-testid="stButton"] > button {
        width: 100% !important;
        height: auto !important;
        min-height: 0 !important;
        max-height: none !important;
    }

    /* ボタン要素本体：aspect-ratio と padding で正方形化 */
    div[data-testid="stColumn"] button[aria-label] {
        aspect-ratio: 1 / 1 !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 20px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
        transition: all 0.2s ease !important;
        padding: 8px !important;
        box-sizing: border-box !important;
    }

    /* ボタン内部コンテナの高さを自動にし、テキスト中央配置を邪魔させない */
    div[data-testid="stColumn"] button[aria-label] > div {
        height: auto !important;
        min-height: 0 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* ボタン内部のテキスト要素 */
    div[data-testid="stColumn"] button[aria-label] div,
    div[data-testid="stColumn"] button[aria-label] p {
        font-size: 1.15rem !important;
        font-weight: 800 !important;
        color: #0F172A !important;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1.3 !important;
        white-space: pre-wrap !important;
        text-align: center !important;
    }

    /* ホバー時の挙動 */
    div[data-testid="stColumn"] button[aria-label]:hover {
        border-color: #10B981 !important;
        background-color: #FFFFFF !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 18px rgba(16, 185, 129, 0.12) !important;
    }

    div[data-testid="stColumn"] button[aria-label]:hover div,
    div[data-testid="stColumn"] button[aria-label]:hover p {
        color: #10B981 !important;
    }

    /* テキスト入力フォーム */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
    }
    
    div[data-baseweb="input"] input {
        color: #0F172A !important;
        background-color: #FFFFFF !important;
    }

    div[data-testid="stNotification"] {
        border-radius: 14px !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
