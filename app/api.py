from datetime import datetime
import requests

def get_data_from_url():
    """
    Retrieves the current temperature for Zagreb from the Weather API.

    Returns:
    float: The temperature value of the current hour for Zagreb.
    str: If it fails to connect to the API, it returns "Cannot connect."
    """
    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=45.81&longitude=15.98&hourly=temperature_2m")
        if response.status_code == requests.codes.ok:
            json_from_url = response.json()
            date = datetime.now().isoformat()[:14] + "00"
            list_index = json_from_url["hourly"]["time"].index(date)
            current_temp = float(json_from_url["hourly"]["temperature_2m"][list_index])
            return current_temp
        else:
            return 'Cannot connect.'
    except Exception as e:
        print(f"Error: {e}")
        return 'Cannot connect.'

