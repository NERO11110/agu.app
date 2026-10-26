import DB  # データベースモジュール
import streamlit as st

# --- 市場価格より10%安い5種類の作物・種の価格定義 ---
CROPS = {
    "ミニトマト": {
        "seed_price": 297,
        "market_price": 330,
        "icon": "🍅",
        "desc": "鮮度による味が抜群。甘くて美味しい定番。",
    },
    "いちご": {
        "seed_price": 540,
        "market_price": 600,
        "icon": "🍓",
        "desc": "コンテナ環境制御に最適。芳醇な香りと甘み。",
    },
    "サニーレタス": {
        "seed_price": 180,
        "market_price": 200,
        "icon": "🥬",
        "desc": "すくすく育つ。シャキシャキ食感の新鮮レタス。",
    },
    "バジル": {
        "seed_price": 225,
        "market_price": 250,
        "icon": "🌿",
        "desc": "摘みたての香りが格別。料理を引き立てます。",
    },
    "ベビーリーフ": {
        "seed_price": 198,
        "market_price": 220,
        "icon": "🧹",
        "desc": "短期間で収穫可能。初心者にも安心のミックス。",
    },
}


def show():
  st.subheader("🛒 ショップ")

  # ホームに戻るボタン
  if st.button("← ホームに戻る"):
    st.session_state.current_screen = "home"
    st.rerun()

  st.write("---")

  # --- 残高表示とチャージ画面への移動ボタン ---
  col_balance, col_link = st.columns([2, 1])

  with col_balance:
    st.markdown(f"### 💰 現在の所持コイン: **{st.session_state.coin:,} yen**")

  with col_link:
    if st.button("💳 コインをチャージする", use_container_width=True):
      st.session_state.current_screen = "charge"
      st.rerun()

  st.write("---")
  st.markdown("### 🌱 種（苗）の購入")
  st.caption(
      "※ 表示価格は市場一般価格より約10%引きの特別価格となっています。"
  )

  # 5種類の種購入カードを表示
  for name, info in CROPS.items():
    seed_key = f"{name}_seeds"
    if seed_key not in st.session_state:
      st.session_state[seed_key] = 0

    with st.container():
      col1, col2, col3 = st.columns([3, 2, 2])

      with col1:
        st.markdown(f"#### {info['icon']} {name} の種")
        st.caption(info["desc"])

      with col2:
        st.write(f"価格: **{info['seed_price']} yen**")
        st.caption(f"（市場参考価格: ~{info['market_price']} yen）")
        st.write(f"所持数: **{st.session_state[seed_key]} 個**")

      with col3:
        if st.button(f"購入する", key=f"buy_{name}"):
          if st.session_state.coin >= info["seed_price"]:
            st.session_state.coin -= info["seed_price"]
            st.session_state[seed_key] += 1

            # DB保存
            DB.save_data(
                st.session_state.coin,
                st.session_state.get("ミニトマト_seeds", 0),
                st.session_state.get("いちご_seeds", 0),
                st.session_state.get("サニーレタス_seeds", 0),
            )

            st.success(f"{name} の種を購入しました！")
            st.rerun()
          else:
            st.warning("残高が不足しています！チャージしてください。")

      st.write("---")
