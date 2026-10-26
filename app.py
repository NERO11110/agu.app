import streamlit as st
import DB
import farm
import shop
import inv
import charge
import style

# ページ全体の初期設定
st.set_page_config(
    page_title="AGRI-CONTAINER",
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
    st.title("🌱 AGRI-CONTAINER")
    st.caption("都市型スマートアグリ遠隔栽培プラットフォーム")

    # 所持コインの表示
    st.info(f"💰 所持コイン: **{st.session_state.coin:,} Coins**")

    st.write("")  # 余白

    # ボタンによる2x2グリッド
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌾\n\nファーム", use_container_width=True, key="nav_farm"):
            st.session_state.current_screen = "farm"
            st.rerun()
        if st.button("🎒\n\nもちもの", use_container_width=True, key="nav_inv"):
            st.session_state.current_screen = "inv"
            st.rerun()

    with col2:
        if st.button("🛒\n\nショップ", use_container_width=True, key="nav_shop"):
            st.session_state.current_screen = "shop"
            st.rerun()
        if st.button("💳\n\nチャージ", use_container_width=True, key="nav_charge"):
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
