import charge
import DB
import farm
import inv
import shop
import style
import streamlit as st

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

# --- ページパラメータ取得の安全化 ---
try:
  if hasattr(st, "query_params"):
    current_page = st.query_params.get("page", "home")
  else:
    params = st.experimental_get_query_params()
    current_page = params.get("page", ["home"])[0]
except Exception:
  current_page = "home"


# ホームに戻る処理
def go_home():
  try:
    if hasattr(st, "query_params"):
      st.query_params.clear()
    else:
      st.experimental_set_query_params()
  except Exception:
    pass
  st.rerun()


# ---------------------------------------------------------
# メイン画面（ホーム：2x2グリッドナビゲーション）
# ---------------------------------------------------------
if current_page == "home":
  st.title("🌱 AGRI-CONTAINER")
  st.caption("都市型スマートアグリ遠隔栽培プラットフォーム")

  # 所持コインの表示
  try:
    coins = DB.get_coins()
  except Exception:
    coins = 0

  st.info(f"💰 所持コイン: **{coins:,} Coins**")

  st.write("")  # 余白

  # HTML/CSSによる強力な2x2正方形グリッド
  st.markdown(
      """
    <style>
    .mobile-2x2-grid {
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 12px !important;
        width: 100% !important;
        max-width: 400px !important;
        margin: 0 auto !important;
        box-sizing: border-box !important;
    }

    .nav-card {
        background-color: #FFFFFF !important;
        border: 2px solid #E5E7EB !important;
        border-radius: 18px !important;
        aspect-ratio: 1 / 1 !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
        text-decoration: none !important;
        color: #111827 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
        transition: all 0.2s ease-in-out !important;
        padding: 8px !important;
        box-sizing: border-box !important;
    }

    .nav-card:hover, .nav-card:active {
        border-color: #059669 !important;
        background-color: #ECFDF5 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 18px rgba(5, 150, 105, 0.15) !important;
    }

    .nav-card .card-icon {
        font-size: 2.2rem !important;
        line-height: 1.1 !important;
        margin-bottom: 6px !important;
    }

    .nav-card .card-title {
        font-family: 'Zen Maru Gothic', sans-serif !important;
        font-size: clamp(1.0rem, 4vw, 1.2rem) !important;
        font-weight: 900 !important;
        color: #111827 !important;
        margin: 0 !important;
    }
    </style>

    <div class="mobile-2x2-grid">
        <a href="?page=farm" target="_self" class="nav-card">
            <div class="card-icon">🌾</div>
            <div class="card-title">ファーム</div>
        </a>
        <a href="?page=shop" target="_self" class="nav-card">
            <div class="card-icon">🛒</div>
            <div class="card-title">ショップ</div>
        </a>
        <a href="?page=inv" target="_self" class="nav-card">
            <div class="card-icon">🎒</div>
            <div class="card-title">もちもの</div>
        </a>
        <a href="?page=charge" target="_self" class="nav-card">
            <div class="card-icon">💳</div>
            <div class="card-title">チャージ</div>
        </a>
    </div>
    """,
      unsafe_allow_html=True,
  )

# ---------------------------------------------------------
# サブ画面へのルーティング処理（固有の key を設定してID重複を回避）
# ---------------------------------------------------------
elif current_page == "farm":
  if st.button("← ホームに戻る", key="btn_back_farm"):
    go_home()
  farm.show()

elif current_page == "shop":
  if st.button("← ホームに戻る", key="btn_back_shop"):
    go_home()
  shop.show()

elif current_page == "inv":
  if st.button("← ホームに戻る", key="btn_back_inv"):
    go_home()
  inv.show()

elif current_page == "charge":
  if st.button("← ホームに戻る", key="btn_back_charge"):
    go_home()
  charge.show()