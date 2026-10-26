import streamlit as st
import random
import string

def show():
  
  st.subheader("🎒 収穫物インベントリ")
  st.write("ここであなたが育てて収穫した作物を確認できます。")

  # 収穫リストが空かどうかチェック
  if "harvested_crops" not in st.session_state:
    st.session_state.harvested_crops = []

  if "passcode" not in st.session_state:
    st.session_state.passcode = None

  # --- 1. 収穫した作物の表示 ---
  if len(st.session_state.harvested_crops) == 0:
    st.info("まだ収穫した作物がありません。ファームでトマトを育てて収穫しよう！")
  else:
    st.success(f"🎉 収穫済みの作物: {len(st.session_state.harvested_crops)} 個")

    # リストの中身を一つずつ表示
    for index, crop in enumerate(st.session_state.harvested_crops):
      st.write(f"🍅 {index + 1}: {crop['name']} （収穫完了！）")

    st.write("---")

    # --- 2 & 3. パスワード発行セクション ---
    st.subheader("🔑 現地入場パスワードの発行")
    st.write("収穫した作物を現地の植物園で受け取るための、入場パスワードを発行できます。")

    if st.session_state.passcode is None:
      if st.button("✨ 入場パスワードを発行する"):
        # パスワードを自動生成（例：OSAKA-FARM-xxxx）
        rand_num = "".join(random.choice(string.hexdigits) for _ in range(4))
        st.session_state.passcode = f"OSAKA-FARM-{rand_num}"
        st.rerun()
    else:
      # すでに発行されている場合
      st.success(f"あなたの入場パスワード: **{st.session_state.passcode}**")
      st.caption("※この画面を現地の自動化植物園の受付で見せてください。")

      if st.button("🔄 パスワードを再発行する"):
        st.session_state.passcode = None
        st.rerun()

  st.write("---")
  if st.button("インベントリを閉じる（ホームへ）"):
    st.session_state.current_screen = "home"
    st.rerun()
