import requests
from cat.mad_hatter.decorators import tool


@tool
def fetch_gtt_data(stop_id, cat):
    """
    Recupera i dati in tempo reale da una fermata del GTT (Gruppo Torinese Trasporti).

    Args:
        stop_id: Identificativo della fermata di cui si vogliono ottenere i dati.
    Returns:
        Un dizionario contenente i dati della fermata o un messaggio di errore.
    """

    try:
        response = requests.get(f"http://gpa.madbob.org/query.php?stop={stop_id}")
        response.raise_for_status()
        cache[stop_id] = response.json()
        return cache[stop_id]
    except requests.RequestException as e:
        return {"error": str(e)}
