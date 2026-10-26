# style.py
import streamlit as st


def apply_custom_css():
  st.markdown(
      """
    <!-- 丸ゴシックフォントの読み込み -->
    <link href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@500;700;900&display=swap" rel="stylesheet">

    <style>
    /* 1. アプリ全体：横スクロールを強制禁止し、縦スクロールのみ許可 */
    html, body, .stApp, [data-testid="stAppViewContainer"] {
        overflow-x: hidden !important;
        max-width: 100vw !important;
        background-color: #FAFAFA !important;
        font-family: 'Zen Maru Gothic', -apple-system, sans-serif !important;
    }

    /* 2. ヘッダー・タイトルの文字切れ防止＆上部余白の最適化 */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    .block-container {
        padding-top: 1.0rem !important;  /* 上部余白を詰めてヘッダーの見切れを防止 */
        padding-bottom: 2.0rem !important;
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    /* タイトル（H1〜H3）の文字サイズ動的調整と折り返し許可 */
    h1, h2, h3 {
        color: #111827 !important;
        font-weight: 900 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
        word-break: break-word !important;  /* はみ出しによる見切れを防止 */
        white-space: normal !important;
        line-height: 1.3 !important;
    }
    
    h1 { font-size: clamp(1.4rem, 5vw, 2.0rem) !important; }
    h2 { font-size: clamp(1.2rem, 4.5vw, 1.6rem) !important; }
    h3 { font-size: clamp(1.05rem, 4vw, 1.3rem) !important; }

    /* 文字色・フォント統一 */
    body, p, span, div, label, .stMarkdown {
        color: #1F2937 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
    }

    /* 3. スマホ2x2グリッド：画面枠内にぴったり収めて横はみ出し（横スクロール）を防止 */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 8px !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
    }

    div[data-testid="stColumn"],
    div[data-testid="column"],
    div[data-testid="stHorizontalBlock"] > div {
        width: calc(50% - 4px) !important;
        min-width: calc(50% - 4px) !important;
        max-width: calc(50% - 4px) !important;
        flex: 1 1 calc(50% - 4px) !important;
        box-sizing: border-box !important;
    }

    /* 4. 正方形ボタンのスタイリング */
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
        box-sizing: border-box !important;
    }

    /* ホバー時 */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button:hover {
        border-color: #059669 !important;
        background-color: #ECFDF5 !important;
        box-shadow: 0 8px 20px rgba(5, 150, 105, 0.15) !important;
        transform: translateY(-2px) !important;
    }

    /* ボタン内のテキスト（画面幅に合わせて自動縮小） */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button p {
        color: #111827 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
        font-size: clamp(0.95rem, 3.8vw, 1.25rem) !important;
        font-weight: 900 !important;
        line-height: 1.2 !important;
        margin: 0 !important;
        word-break: break-word !important;
    }

    /* 通常ボタン */
    .stButton > button {
        background-color: #FFFFFF !important;
        color: #111827 !important;
        border: 2px solid #D1D5DB !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
    }
    </style>
    """,
      unsafe_allow_html=True,
  )
