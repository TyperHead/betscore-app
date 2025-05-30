import streamlit as st
import requests

st.set_page_config(page_title="BetScore", page_icon="⚽")

st.title("⚽ Kursy bukmacherskie z API-Football (bet365)")

# Dane do zapytania
url = "https://api-football-v1.p.rapidapi.com/v2/odds/league/39/bookmaker/5"
querystring = {"page": "1"}

headers = {
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
    "x-rapidapi-key": "48accb8b3cmsh0f6f533f6ec90bbp105f4djsna91c5c497224"  # <- tu twój klucz
}

# Wysyłanie zapytania
response = requests.get(url, headers=headers, params=querystring)

try:
    data = response.json()

    # Sprawdzenie czy są dane
    if data.get("api") and data["api"].get("odds"):
        st.success("Dane zostały załadowane.")
        for match in data["api"]["odds"]:
            st.write(match)
    else:
        st.warning("Brak danych.")
except Exception as e:
    st.error(f"Błąd podczas ładowania danych: {e}")
