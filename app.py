from datetime import datetime
import streamlit as st
import DB

CROPS = {
    "ミニトマト": {"seed_price": 297, "market_price": 330, "harvest_val": 500, "icon": "🍅", "grow_minutes": 60},
    "いちご": {"seed_price": 540, "market_price": 600, "harvest_val": 800, "icon": "🍓", "grow_minutes": 120},
    "サニーレタス": {"seed_price": 180, "market_price": 200, "harvest_val": 300, "icon": "🥬", "grow_minutes": 30},
    "バジル": {"seed_price": 225, "market_price": 250, "harvest_val": 350, "icon": "🌿", "grow_minutes": 45},
    "ベビーリーフ": {"seed_price": 198, "market_price": 220, "harvest_val": 320, "icon": "🧹", "grow_minutes": 20},
}


def get_latest_snapshot():
    current_hour = datetime.now().hour
    if current_hour < 9:
        return "昨日の 21:00"
    elif current_hour < 15:
        return "本日の 09:00"
    elif current_hour < 21:
        return "本日の 15:00"
    else:
        return "本日の 21:00"


def calculate_growth(crop_data):
    if not crop_data or "planted_at" not in crop_data:
        return crop_data.get("growth", 0)

    if crop_data.get("growth", 0) >= 100:
        return 100

    planted_time = datetime.fromisoformat(crop_data["planted_at"])
    elapsed_seconds = (datetime.now() - planted_time).total_seconds()

    crop_info = CROPS.get(crop_data["name"], {})
    total_grow_seconds = crop_info.get("grow_minutes", 60) * 60

    calculated = int((elapsed_seconds / total_grow_seconds) * 100)
    return min(calculated, 100)


def show():
    col_nav, col_debug = st.columns([3, 1])
    with col_nav:
        if st.button("← ホームに戻る", key="farm_back_home"):
            st.session_state.current_screen = "home"
            st.rerun()

    with col_debug:
        debug_mode = st.checkbox("🛠️ デバッグ")

    st.markdown("<h2 style='margin-top: 10px;'>🌾 スマート農業コンテナ・ファーム</h2>",
                unsafe_allow_html=True)

    # 所持金・種カード
    seeds_status = " | ".join([
        f"{data['icon']} {name}:{st.session_state.get(f'{name}_seeds', 0)}個"
        for name, data in CROPS.items()
    ])

    st.markdown(
        f"""
        <div class="custom-card">
            <p style="margin: 0; font-weight: 700;">💰 所持金: {st.session_state.coin:,} yen</p>
            <p style="margin: 4px 0 0 0; font-size: 0.8rem; color: #64748B;">📦 所持中の種: {seeds_status}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    photo_time = get_latest_snapshot()
    st.markdown("### 🪴 栽培・定時監視エリア（3区画）")
    st.caption(f"📷 定時カメラ更新: {photo_time} (時間経過により作物が自然生長します)")

    cols = st.columns(3)

    for i in range(3):
        with cols[i]:
            st.markdown(f"#### 【区画 {i + 1}】")
            crop_data = st.session_state.farms[i]

            if crop_data is None:
                st.info("📷 カメラ: 区画空き")
                selected_crop = st.selectbox(
                    "植える作物", list(CROPS.keys()), key=f"select_{i}")

                if st.button(f"{CROPS[selected_crop]['icon']} 植える", key=f"plant_{i}"):
                    seed_key = f"{selected_crop}_seeds"
                    current_seeds = st.session_state.get(seed_key, 0)

                    if current_seeds > 0:
                        st.session_state[seed_key] -= 1
                        st.session_state.farms[i] = {
                            "name": selected_crop,
                            "growth": 0,
                            "icon": CROPS[selected_crop]["icon"],
                            "planted_at": datetime.now().isoformat(),
                            "is_watered": False,
                        }

                        DB.save_farm_data(st.session_state.farms,
                                          st.session_state.harvested_crops)
                        DB.save_data(
                            st.session_state.coin,
                            st.session_state.get("ミニトマト_seeds", 0),
                            st.session_state.get("いちご_seeds", 0),
                            st.session_state.get("サニーレタス_seeds", 0),
                        )

                        st.success(f"{selected_crop} を定植しました。")
                        st.rerun()
                    else:
                        st.warning("種がありません。ショップで購入してください。")

            else:
                growth = calculate_growth(crop_data)
                crop_data["growth"] = growth

                crop_icon = crop_data.get("icon", "🌱")
                crop_name = crop_data["name"]
                is_watered = crop_data.get("is_watered", False)

                camera_image_url = "https://smartagri-jp.com/images/upload/2024/03/150aac2b245774b9f802e38d7e3b0acb.jpg"
                st.image(
                    camera_image_url, caption=f"区画{i + 1} 撮影: {photo_time}", use_container_width=True)

                st.success(f"{crop_icon} {crop_name}\n(生長度: {growth}%)")
                st.progress(growth / 100)

                if growth < 100:
                    if not is_watered:
                        st.warning("⚠️ 土壌: 乾いています")
                        if st.button(f"💧 給水", key=f"water_{i}"):
                            crop_data["is_watered"] = True
                            DB.save_farm_data(
                                st.session_state.farms, st.session_state.harvested_crops)
                            st.toast(f"区画{i + 1}への自動給水が完了しました。")
                            st.rerun()
                    else:
                        st.info("💧 土壌: 最適")
                else:
                    st.info("🎉 収穫適期")

                if debug_mode and growth < 100:
                    if st.button(f"⚡ [DBG] 100%", key=f"dbg_{i}"):
                        crop_data["growth"] = 100
                        DB.save_farm_data(st.session_state.farms,
                                          st.session_state.harvested_crops)
                        st.rerun()

                if growth >= 100:
                    if st.button(f"✂️ 収穫", key=f"harvest_{i}"):
                        harvested_item = {"name": crop_name, "icon": crop_icon}
                        st.session_state.farms[i] = None

                        if "harvested_crops" not in st.session_state:
                            st.session_state.harvested_crops = []
                        st.session_state.harvested_crops.append(harvested_item)

                        DB.save_farm_data(st.session_state.farms,
                                          st.session_state.harvested_crops)
                        st.balloons()
                        st.success(f"{crop_name} の収穫完了。")
                        st.rerun()
