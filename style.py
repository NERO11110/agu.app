import streamlit as st


def apply_custom_css():
    st.markdown(
        """
    <link href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@500;700;900&display=swap" rel="stylesheet">

    <style>
    /* 全体背景 */
    html, body, .stApp {
        background-color: #F8FAFC !important;
        font-family: 'Zen Maru Gothic', -apple-system, sans-serif !important;
    }

    body, p, span, div, label, .stMarkdown {
        color: #1E293B !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #0F172A !important;
        font-weight: 900 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
        word-break: break-word !important;
    }

    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 440px !important;
        margin: 0 auto !important;
    }

    /* 角丸カードコンテナ */
    .custom-card {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 16px !important;
        padding: 16px 20px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
        margin-bottom: 16px !important;
    }

    /* ボタンの共通デザイン */
    .stButton > button {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03) !important;
        transition: all 0.2s ease !important;
        padding: 10px 16px !important;
    }
    
    .stButton > button:hover {
        border-color: #10B981 !important;
        color: #10B981 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.12) !important;
    }

    /* 入力フォームの丸み */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
        background-color: #1E293B !important;
        color: #FFFFFF !important;
    }
    div[data-baseweb="input"] input {
        color: #FFFFFF !important;
    }

    /* Info / Warning / Success アラート表示の角丸統一 */
    div[data-testid="stNotification"] {
        border-radius: 14px !important;
        border: none !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03) !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
