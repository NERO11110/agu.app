import streamlit as st
import DB
import style
import farm
import shop
import inv
import charge
import string

# DB初期化
DB.init_db()

# ページ基本設定
st.set_page_config(
    page_title="スマートアグリ・プラットフォーム",
    page_icon="🌱",
    layout="centered"
)

# 白基調CSSの適用
style.apply_custom_css()

# セッション状態初期化
if "current_screen" not in st.session_state:
    st.session_state.current_screen = "home"

if "coin" not in st.session_state:
    coin, t_seeds, s_seeds, l_seeds = DB.load_data()
    st.session_state.coin = coin
    st.session_state.ミニトマト_seeds = t_seeds
    st.session_state.いちご_seeds = s_seeds
    st.session_state.サニーレタス_seeds = l_seeds

if "farms" not in st.session_state:
    farms, harvested_crops = DB.load_farm_data()
    st.session_state.farms = farms
    st.session_state.harvested_crops = harvested_crops


# --- 1. ホーム画面 ---
if st.session_state.current_screen == "home":
    # タイトル
    st.markdown("<h2 style='text-align: center; color: #111827; margin-bottom: 20px; font-weight: 900;'>🌱 スマートアグリ</h2>", unsafe_allow_html=True)

    # 所持コイン（コントラストの高い黒文字・緑アクセント）
    st.markdown(f"""
        <div style="background: #FFFFFF; border: 2px solid #E5E7EB; border-radius: 16px; padding: 14px 20px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
            <span style="font-size: 1.05rem; color: #374151; font-weight: 700;">所持コイン</span>
            <span style="font-size: 1.5rem; font-weight: 900; color: #059669;">{st.session_state.coin:,} <span style="font-size: 1rem; color: #111827;">yen</span></span>
        </div>
    """, unsafe_allow_html=True)

    # 2×2 正方形ボタンレイアウト
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        # 🌾 ファーム
        st.markdown('<div class="square-btn"></div>', unsafe_allow_html=True)
        if st.button("🌾\n\nファーム", key="btn_farm", use_container_width=True):
            st.session_state.current_screen = "farm"
            st.rerun()

        st.write("")  # 余白

        # 🛒 ショップ
        st.markdown('<div class="square-btn"></div>', unsafe_allow_html=True)
        if st.button("🛒\n\nショップ", key="btn_shop", use_container_width=True):
            st.session_state.current_screen = "shop"
            st.rerun()

    with col2:
        # 🎒 もちもの
        st.markdown('<div class="square-btn"></div>', unsafe_allow_html=True)
        if st.button("🎒\n\nもちもの", key="btn_inv", use_container_width=True):
            st.session_state.current_screen = "inv"
            st.rerun()

        st.write("")  # 余白

        # 💳 チャージ
        st.markdown('<div class="square-btn"></div>', unsafe_allow_html=True)
        if st.button("💳\n\nチャージ", key="btn_charge", use_container_width=True):
            st.session_state.current_screen = "charge"
            st.rerun()

# --- 2. 各画面分岐 ---
elif st.session_state.current_screen == "farm":
    farm.show()
elif st.session_state.current_screen == "shop":
    shop.show()
elif st.session_state.current_screen == "inv":
    inv.show()
elif st.session_state.current_screen == "charge":
    charge.show()
