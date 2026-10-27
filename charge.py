import streamlit as st
import DB

CHARGE_AMOUNTS = [500, 1000, 2000, 3000, 5000, 10000]


@st.dialog("💳 決済の最終確認")
def confirm_charge_dialog(amount, pay_method):
    st.write("以下の内容でチャージ処理を実行します。")
    st.markdown(f"- **チャージ金額**: **¥{amount:,}**")
    st.markdown(f"- **お支払い方法**: **{pay_method}**")
    st.write("よろしいですか？")

    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("はい（決済確定）", type="primary", use_container_width=True):
            st.session_state.coin += amount

            DB.save_data(
                st.session_state.coin,
                st.session_state.get("ミニトマト_seeds", 0),
                st.session_state.get("いちご_seeds", 0),
                st.session_state.get("サニーレタス_seeds", 0),
            )

            st.success(f"¥{amount:,} のチャージが完了しました！")
            st.rerun()

    with col2:
        if st.button("キャンセル", use_container_width=True):
            st.rerun()


def show():
    if st.button("← ホームに戻る", key="charge_back_home"):
        st.session_state.current_screen = "home"
        st.rerun()

    st.write("")

    # 所持コインカード
    st.markdown(
        f"""
        <div class="custom-card">
            <h3 style="margin: 0; font-size: 1.15rem;">💰 現在の所持コイン: {st.session_state.coin:,} yen</h3>
            <p style="margin: 6px 0 0 0; font-size: 0.8rem; color: #64748B;">※ チャージしたコインは、スマートコンテナでの栽培に必要な種（苗）の購入等に使用します。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # 1. チャージ金額の選択
    st.markdown("### 1. チャージ金額の選択")
    selected_amount = st.radio(
        "購入する金額を選択してください（1 yen = 1 コイン）",
        CHARGE_AMOUNTS,
        format_func=lambda x: f"{x:,} 円",
        horizontal=True,
    )

    st.write("")

    # 2. 決済方法の選択
    st.markdown("### 2. 入金方法の選択")
    pay_method = st.radio(
        "お支払い方法",
        ["クレジットカード", "Apple Pay / Google Pay", "銀行振込・コンビニ決済"],
        horizontal=True,
    )

    if pay_method == "クレジットカード":
        st.write("")
        col_card1, col_card2 = st.columns(2)
        with col_card1:
            st.text_input("カード番号", "•••• •••• •••• 1234")
        with col_card2:
            st.text_input("有効期限 / CVC", "12/28  123")

    st.write("")

    if st.button(
        f"¥{selected_amount:,} をチャージする", type="primary", use_container_width=True
    ):
        confirm_charge_dialog(selected_amount, pay_method)
