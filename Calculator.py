import streamlit as st

st.title("🎯 ELO Rating Calculator (Best of 5)")

# Input ELO ratings
elo_a = st.number_input("Enter Player A's ELO", min_value=1000)
elo_b = st.number_input("Enter Player B's ELO", min_value=1000)

# Input match result
games_a = st.number_input("Games won by Player A (0–3)", min_value=0, max_value=3)
games_b = st.number_input("Games won by Player B (0–3)", min_value=0, max_value=3)

# Calculate ELO
if st.button("Calculate New ELO Ratings"):
    if games_a + games_b > 5 or (games_a != 3 and games_b != 3):
        st.error("⚠️ Match must end when one player has 3 wins and total games ≤ 5.")
    else:
        s_a = games_a / (games_a + games_b)
        s_b = games_b / (games_a + games_b)
        expected_a = 1 / (1 + 10 ** ((elo_b - elo_a) / 400))
        expected_b = 1 / (1 + 10 ** ((elo_a - elo_b) / 400))
        k = 64
        delta_a = k * (s_a - expected_a)
        delta_b = k * (s_b - expected_b)
        if games_a > games_b and delta_a < 0:
            delta_a = 0
        if games_b > games_a and delta_b < 0:
            delta_b = 0

        new_elo_a = max(1000, round(elo_a + delta_a))
        new_elo_b = max(1000, round(elo_b + delta_b))


        st.success(f"🏆 Player A's new ELO: **{new_elo_a}**")
        st.success(f"🎮 Player B's new ELO: **{new_elo_b}**")
