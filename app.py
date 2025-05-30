import streamlit as st
import pandas as pd
import requests

def get_odds():
    url = "https://api-football-v1.p.rapidapi.com/v2/odds/league/39/bookmaker/5"
querystring = {"page": "1"}


    headers = {
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
        "x-rapidapi-key": "48accb8b3cmsh0f6f533f6ec90bbp105f4djsna91c5c497224"
    }

    response = requests.get(url, headers=headers, params=querystring)
    st.json(response.json())

    if response.status_code != 200:
        return pd.DataFrame([{"Błąd": "Nie udało się pobrać danych"}])

    data = response.json()
    odds_list = []

    for item in data.get("api", {}).get("odds", []):
        try:
            match = f"{item['teams']['home']} vs {item['teams']['away']}"
            league = item['league']['name']
            bookmaker = item['bookmakers'][0]['name']
            bets = item['bookmakers'][0]['bets']
            for bet in bets:
                if bet['label_name'].lower() == "match winner":
                    for val in bet['values']:
                        odds_list.append({
                            "Mecz": match,
                            "Zakład": val['value'],
                            "Kurs": val['odd'],
                            "Liga": league,
                            "Bukmacher": bookmaker
                        })
        except Exception as e:
            continue

    return pd.DataFrame(odds_list)

# Streamlit app
st.title("⚽ Kursy bukmacherskie z API-Football (bet365)")

df = get_odds()
if df.empty:
    st.warning("Brak danych.")
else:
    st.dataframe(df, use_container_width=True)

