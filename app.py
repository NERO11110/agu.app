import streamlit as st
import DB
import farm
import shop
import inv
import charge
import style

# ページ全体の初期設定
st.set_page_config(
    page_title="スマートアグリ",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# データベース初期化
DB.init_db()

# 共通CSSの適用
style.apply_custom_css()

# --- session_state の初期化 ---
if "current_screen" not in st.session_state:
    st.session_state.current_screen = "home"

if "coin" not in st.session_state:
    coin, tomato, strawberry, lettuce = DB.load_data()
    st.session_state.coin = coin
    st.session_state["ミニトマト_seeds"] = tomato
    st.session_state["いちご_seeds"] = strawberry
    st.session_state["サニーレタス_seeds"] = lettuce
    st.session_state["バジル_seeds"] = 0
    st.session_state["ベビーリーフ_seeds"] = 0

if "farms" not in st.session_state or "harvested_crops" not in st.session_state:
    farms, harvested_crops = DB.load_farm_data()
    st.session_state.farms = farms
    st.session_state.harvested_crops = harvested_crops

current_page = st.session_state.current_screen

# ---------------------------------------------------------
# メイン画面（ホーム：2x2正方形カードレイアウト）
# ---------------------------------------------------------
if current_page == "home":
    st.markdown("<h1 style='text-align: center; margin-bottom: 24px; font-size: 1.8rem;'>🌱 スマートアグリ</h1>",
                unsafe_allow_html=True)

    # 所持コインカード（角丸カード）
    st.markdown(
        f"""
        <div style="
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 18px;
            padding: 18px 24px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
            margin-bottom: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        ">
            <span style="font-weight: 700; color: #1E293B; font-size: 1.05rem;">所持コイン</span>
            <span style="font-size: 1.3rem; font-weight: 900; color: #0F172A;">{st.session_state.coin:,} <span style="font-size: 0.85rem; font-weight: 600; color: #475569;">yen</span></span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 正方形ボタン用スタイル注入
    st.markdown(
        """
        <style>
        /* PC・タブレットサイズ（画面幅 768px 以上）のみ正方形を適用 */
        @media (min-width: 768px) {
            div[data-testid="stColumn"] div[data-testid="stButton"] {
                width: 100% !important;
                height: auto !important;
            }

            div[data-testid="stColumn"] div[data-testid="stButton"] > button {
                width: 100% !important;
                aspect-ratio: 1 / 1 !important; /* 正方形化 */
                height: auto !important;
                min-height: 0 !important;
                max-height: none !important;
                background-color: #FFFFFF !important;
                border: 1px solid #E2E8F0 !important;
                border-radius: 24px !important;
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.04) !important;
                display: flex !important;
                flex-direction: column !important;
                justify-content: center !important;
                align-items: center !important;
                padding: 0 !important;
                transition: all 0.2s ease-in-out !important;
            }

            div[data-testid="stColumn"] div[data-testid="stButton"] > button:hover {
                border-color: #10B981 !important;
                background-color: #FFFFFF !important;
                transform: translateY(-3px) !important;
                box-shadow: 0 10px 24px rgba(16, 185, 129, 0.15) !important;
            }

            div[data-testid="stColumn"] div[data-testid="stButton"] > button div[data-testid="stMarkdownContainer"] {
                height: auto !important;
                min-height: 0 !important;
            }

            div[data-testid="stColumn"] div[data-testid="stButton"] > button p {
                font-size: 1.25rem !important;
                font-weight: 800 !important;
                color: #0F172A !important;
                margin: 0 !important;
                line-height: 1.4 !important;
                text-align: center !important;
                white-space: pre-line !important;
            }

            div[data-testid="stColumn"] div[data-testid="stButton"] > button:hover p {
                color: #10B981 !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 2x2 正方形カード配置
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌾\nファーム", use_container_width=True, key="nav_farm"):
            st.session_state.current_screen = "farm"
            st.rerun()

        st.write("")  # 上下カード間隔

        if st.button("🛒\nショップ", use_container_width=True, key="nav_shop"):
            st.session_state.current_screen = "shop"
            st.rerun()

    with col2:
        if st.button("🎒\nもちもの", use_container_width=True, key="nav_inv"):
            st.session_state.current_screen = "inv"
            st.rerun()

        st.write("")  # 上下カード間隔

        if st.button("💳\nチャージ", use_container_width=True, key="nav_charge"):
            st.session_state.current_screen = "charge"
            st.rerun()

# ---------------------------------------------------------
# サブ画面へのルーティング処理
# ---------------------------------------------------------
elif current_page == "farm":
    farm.show()

elif current_page == "shop":
    shop.show()

elif current_page == "inv":
    inv.show()

elif current_page == "charge":
    charge.show()
