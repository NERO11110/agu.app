import random
import string
import streamlit as st


def show():
    if st.button("← ホームに戻る", key="inv_back_home"):
        st.session_state.current_screen = "home"
        st.rerun()

    st.markdown("<h2 style='margin-top: 10px;'>🎒 収穫物インベントリ（マイバッグ）</h2>",
                unsafe_allow_html=True)
    st.write("ここであなたが育てて収穫した作物を確認できます。")

    if "harvested_crops" not in st.session_state:
        st.session_state.harvested_crops = []

    if "passcode" not in st.session_state:
        st.session_state.passcode = None

    if len(st.session_state.harvested_crops) == 0:
        st.info("まだ収穫した作物がありません。ファームでトマトを育てて収穫しよう！")
    else:
        st.success(f"🎉 収穫済みの作物: {len(st.session_state.harvested_crops)} 個")

        for index, crop in enumerate(st.session_state.harvested_crops):
            icon = crop.get("icon", "🍅")
            st.write(f"{icon} {index + 1}: {crop['name']} （収穫完了！）")

        st.write("---")

        st.subheader("🔑 現地入場パスワードの発行")
        st.write("収穫した作物を現地の植物園で受け取るための、入場パスワードを発行できます。")

        if st.session_state.passcode is None:
            if st.button("✨ 入場パスワードを発行する"):
                rand_num = "".join(random.choice(
                    string.hexdigits.upper()) for _ in range(4))
                st.session_state.passcode = f"OSAKA-FARM-{rand_num}"
                st.rerun()
        else:
            st.success(f"あなたの入場パスワード: **{st.session_state.passcode}**")
            st.caption("※この画面を現地の自動化植物園の受付で見せてください。")

            if st.button("🔄 パスワードを再発行する"):
                st.session_state.passcode = None
                st.rerun()
