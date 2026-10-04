import DB  # DB保存用
import streamlit as st

# チャージ金額の選択肢（500円〜10,000円）
CHARGE_AMOUNTS = [500, 1000, 2000, 3000, 5000, 10000]


# --- 最終確認ダイアログ（ポップアップ） ---
@st.dialog("💳 決済の最終確認")
def confirm_charge_dialog(amount, pay_method):
  # ダイアログ内の文字色を濃い色に強制固定するCSSスタイル
  st.markdown(
      """
        <style>
        /* ダイアログ内の全文字色をくっきり固定 */
        div[role="dialog"] *, div[role="dialog"] p, div[role="dialog"] span, div[role="dialog"] div {
            color: #111827 !important;
            font-weight: 600 !important;
        }
        div[role="dialog"] strong {
            color: #059669 !important; /* 強調部分は深緑 */
            font-weight: 800 !important;
        }
        </style>
    """,
      unsafe_allow_html=True,
  )

  st.write("以下の内容でチャージ処理を実行します。")
  st.markdown(f"- **チャージ金額**: **¥{amount:,}**")
  st.markdown(f"- **お支払い方法**: **{pay_method}**")
  st.write("よろしいですか？")

  st.write("")  # スペース

  col1, col2 = st.columns(2)
  with col1:
    if st.button("はい（決済確定）", type="primary", use_container_width=True):
      # コインを追加 (1円 = 1コイン)
      st.session_state.coin += amount

      # DBに保存
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
  st.subheader("💳 コインチャージ（決済）")

  # ホームに戻るボタン
  if st.button("← ホームに戻る"):
    st.session_state.current_screen = "home"
    st.rerun()

  st.write("---")

  # 現在の残高表示
  st.markdown(f"### 💰 現在の所持コイン: **{st.session_state.coin:,} yen**")
  st.caption(
      "※ チャージしたコインは、スマートコンテナでの栽培に必要な種（苗）の購入等に使用します。"
  )

  st.write("---")
  st.markdown("### 1. チャージ金額の選択")

  # 6つの金額をラジオボタンで選択
  selected_amount = st.radio(
      "購入する金額を選択してください（1 yen = 1 コイン）",
      CHARGE_AMOUNTS,
      format_func=lambda x: f"{x:,} 円",
      horizontal=True,
  )

  st.write("---")
  st.markdown("### 2. 決済方法の選択")

  pay_method = st.radio(
      "お支払い方法",
      ["クレジットカード", "Apple Pay / Google Pay", "銀行振込・コンビニ決済"],
      horizontal=True,
  )

  # クレジットカード入力フォーム（モック）
  if pay_method == "クレジットカード":
    st.write("")
    col_card1, col_card2 = st.columns(2)
    with col_card1:
      st.text_input("カード番号", "•••• •••• •••• 1234")
    with col_card2:
      st.text_input("有効期限 / CVC", "12/28  123")

  st.write("---")

  # 決済手続きへ進むボタン（ダイアログを開く）
  if st.button(
      f"¥{selected_amount:,} をチャージする", type="primary", use_container_width=True
  ):
    confirm_charge_dialog(selected_amount, pay_method)