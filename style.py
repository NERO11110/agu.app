# style.py
import streamlit as st


def apply_custom_css():
  st.markdown(
      """
    <!-- 丸ゴシックフォントの読み込み -->
    <link href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@500;700;900&display=swap" rel="stylesheet">

    <style>
    /* 1. 全体設定：横スクロールの発生を物理的にシャットアウト */
    html, body, .stApp {
        overflow-x: hidden !important;
        max-width: 100vw !important;
        background-color: #FAFAFA !important;
        font-family: 'Zen Maru Gothic', -apple-system, sans-serif !important;
    }

    /* 2. ヘッダー余白と文字切れの防止 */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }

    .block-container {
        padding-top: 1.0rem !important;
        padding-bottom: 2.0rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 480px !important; /* PC版表示の横幅基準 */
        margin: 0 auto !important;
    }

    /* タイトル文字の見切れ防止 */
    h1, h2, h3 {
        color: #111827 !important;
        font-weight: 900 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
        word-break: break-word !important;
        white-space: normal !important;
        line-height: 1.3 !important;
    }
    h1 { font-size: 1.6rem !important; }

    /* 文字色・フォント統一 */
    body, p, span, div, label, .stMarkdown {
        color: #1F2937 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
    }

    /* ★★★ 3. スマホ画面で崩さず全体をジャストフィット縮小させる設定 ★★★ */
    @media (max-width: 640px) {
        /* アプリ全体の幅を400px相当で描画し、画面幅に合わせて自動スケーリング */
        .main .block-container {
            width: 100% !important;
            box-sizing: border-box !important;
        }

        /* 横並びカラムを2列（50%）に強制保持 */
        [data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            gap: 10px !important;
            width: 100% !important;
        }

        [data-testid="stColumn"],
        div[data-testid="stHorizontalBlock"] > div {
            width: 50% !important;
            min-width: 50% !important;
            max-width: 50% !important;
            flex: 1 1 50% !important;
        }
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
        padding: 6px !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* ボタン内のテキスト設定 */
    div.element-container:has(div.square-btn) + div.element-container .stButton > button p {
        color: #111827 !important;
        font-family: 'Zen Maru Gothic', sans-serif !important;
        font-size: 1.1rem !important;
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
