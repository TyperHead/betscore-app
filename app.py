import streamlit as st
import json
import pandas as pd

# Prosty system logowania
def load_users():
    with open("users.json", "r") as f:
        return json.load(f)

def login(email, password):
    users = load_users()
    return users.get(email) == password

# Przykładowe dane meczowe
def get_matches():
    data = [
        {"Mecz": "Arsenal vs Chelsea", "Wynik": "2:1", "Kurs": 2.3, "Prawdopodobieństwo": 0.55},
        {"Mecz": "Barcelona vs Real Madrid", "Wynik": "1:1", "Kurs": 3.1, "Prawdopodobieństwo": 0.30},
        {"Mecz": "Bayern vs Dortmund", "Wynik": "3:2", "Kurs": 2.0, "Prawdopodobieństwo": 0.60}
    ]
    for d in data:
        d["Value"] = round(d["Prawdopodobieństwo"] * d["Kurs"], 2)
    return pd.DataFrame(data)

# Interfejs użytkownika
st.title("BetScore ⚽")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("🔐 Zaloguj się")
    email = st.text_input("Email")
    password = st.text_input("Hasło", type="password")
    if st.button("Zaloguj"):
        if login(email, password):
            st.session_state.logged_in = True
            st.success("Zalogowano pomyślnie!")
        else:
            st.error("Nieprawidłowy email lub hasło.")
else:
    st.success("Jesteś zalogowany!")
    st.subheader("📊 Mecze na dziś")
    st.dataframe(get_matches(), use_container_width=True)
