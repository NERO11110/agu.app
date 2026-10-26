# style.py
import streamlit as st


def apply_custom_css():
  st.markdown(
      """
    <!-- 丸ゴシックフォントの読み込み -->
    <link href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@500;700;900&display=swap" rel="stylesheet">

    <style>
    /* 1. アプリ全体：横スクロールを絶対禁止 */
    html, body, .stApp, [data-testid="stAppViewContainer"], .main {
        overflow-x: hidden !important;
        max-width: 100vw !important;
        background-color: #FAFAFA !important;
        font-family: 'Zen Maru Gothic', -apple-system, sans-serif !important;
    }

    /* 2. ヘッダー余白詰めで見切れ防止 */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    .block-container {
        padding-top: 1.0rem !important;
        padding-bottom: 2.0rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    /* タイトルの自動折り返し・縮小 */
    h1, h2, h3 {
        color: #111827 !important;
        font-weight: 900 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
        word-break: break-word !important;
        white-space: normal !important;
        line-height: 1.3 !important;
    }
    h1 { font-size: clamp(1.3rem, 5vw, 1.8rem) !important; }

    /* 文字色・フォント統一 */
    body, p, span, div, label, .stMarkdown {
        color: #1F2937 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
    }

    /* ★★★ 3. JavaScript直塗りのインラインスタイル(style=...)を直接ぶち破る極小指定 ★★★ */
    
    /* 横並びブロックを強制的に flex-row に維持 */
    [data-testid="stHorizontalBlock"],
    div[style*="flex-direction: column"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 8px !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    /* カラムの幅をインラインスタイル含めて 50%（半分）に完全強制 */
    [data-testid="stColumn"],
    div[style*="width:"],
    div[data-testid="stHorizontalBlock"] > div {
        width: calc(50% - 4px) !important;
        min-width: calc(50% - 4px) !important;
        max-width: calc(50% - 4px) !important;
        flex: 0 0 calc(50% - 4px) !important;
        box-sizing: border-box !important;
    }

    /* 4. 正方形ボタンのスタイリング */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button {
        width: 100% !important;
        aspect-ratio: 1 / 1 !important;
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

    /* ボタン内のテキスト調整 */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button p {
        color: #111827 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
        font-size: clamp(0.9rem, 3.5vw, 1.2rem) !important;
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
