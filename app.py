import streamlit as st
import json

# Prosty system logowania
def load_users():
    with open("users.json", "r") as f:
        return json.load(f)

def login(email, password):
    users = load_users()
    return users.get(email) == password

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
    st.write("Tutaj pojawi się lista meczów, kursy, value itd.")