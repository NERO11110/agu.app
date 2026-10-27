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
# メイン画面（ホーム：2x2グリッドナビゲーション）
# ---------------------------------------------------------
if current_page == "home":
    st.markdown("<h1 style='text-align: center; margin-bottom: 20px;'>🌱 スマートアグリ</h1>",
                unsafe_allow_html=True)

    # 所持コインカード
    st.markdown(
        f"""
        <div class="custom-card" style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-weight: 700; color: #475569;">所持コイン</span>
            <span style="font-size: 1.25rem; font-weight: 900; color: #0F172A;">{st.session_state.coin:,} <span style="font-size: 0.85rem; font-weight: 500;">yen</span></span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # 2x2 グリッドボタン
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌾  ファーム", use_container_width=True, key="nav_farm"):
            st.session_state.current_screen = "farm"
            st.rerun()
        st.write("")
        if st.button("🛒  ショップ", use_container_width=True, key="nav_shop"):
            st.session_state.current_screen = "shop"
            st.rerun()

    with col2:
        if st.button("🎒  もちもの", use_container_width=True, key="nav_inv"):
            st.session_state.current_screen = "inv"
            st.rerun()
        st.write("")
        if st.button("💳  チャージ", use_container_width=True, key="nav_charge"):
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
