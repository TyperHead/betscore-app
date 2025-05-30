import streamlit as st
import requests
import json

st.set_page_config(page_title="BetScore", page_icon="⚽")
st.title("⚽ Kursy bukmacherskie z API-Football (bet365)")

# 🔐 Dane dostępowe
api_key = "48accb8b3cmsh0f6f533f6ec90bbp105f4djsna91c5c497224"
headers = {
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
    "x-rapidapi-key": api_key
}

# 📌 Parametry — możesz je zmienić
league_id = "39"         # Premier League
bookmaker_id = "5"       # Bet365
url = f"https://api-football-v1.p.rapidapi.com/v2/odds/league/{league_id}/bookmaker/{bookmaker_id}"

# 🌐 Pobierz dane z API
response = requests.get(url, headers=headers)

# 📦 Przetwórz odpowiedź
if response.status_code == 200:
    data = response.json()

    st.subheader("📊 Surowa odpowiedź JSON z API:")
    st.json(data)

    results = data.get("api", {}).get("results", 0)
    if results == 0:
        st.warning("❌ Brak danych z API dla tej ligi lub bukmachera.")
    else:
        st.success(f"✅ Znaleziono {results} wyników.")
        # Dalsze przetwarzanie możesz dodać tu
else:
    st.error(f"Błąd pobierania danych: {response.status_code}")

