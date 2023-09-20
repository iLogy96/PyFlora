
def check_plant_status(plant:object, data:object):
    """
    Evaluates the plant's status based on sensor readings and plant preferences.

    Parameters:
    plant (object): Object representing the plant's preferences for certain conditions.
    data (object): Object representing the current sensor readings.
                        Example: {'sen_light': 'Mid', 'sen_hydration': 60, 'sen_pH': 7, 'sen_temp': 22}

    Returns:
    str: A message describing the plant's status.
    """
    hidration_status="Hydration => Good"
    pH_status="pH => Good"
    temp_status="Temperature => Good"
    light_status="Light => Good"

    if plant.light == "High" and data.sen_light != "High":
        light_status="Light => Too low. Turning on lamp"

    elif plant.light == "Mid" and data.sen_light == "Low":
        light_status="Light => Too low. Turning on lamp"   

    elif plant.light == "Mid" and data.sen_light == "High":
        light_status="Light => Too high. Turning on shaders"

    elif plant.light == "Low" and data.sen_light != "Low":
        light_status="Light => Too high. Turning on shaders"
    
    if plant.hydration == "High" and data.sen_hydration < 75:
        hidration_status = "Hydration => Too low. Starting watering"
        
    elif plant.hydration == "Mid" and data.sen_hydration < 50:
        hidration_status = "Hydration => Too low. Starting watering"

    elif plant.hydration == "Low" and data.sen_hydration < 25:
        hidration_status = "Hydration => Too low. Starting watering"

    if plant.pH == "High" and data.sen_pH < 10:
        pH_status = "Change soil"

    elif plant.pH == "Mid" and (data.sen_pH < 6 or data.sen_pH > 8):
        pH_status = "Change soil"

    elif plant.pH == "Low" and data.sen_pH > 5: 
        pH_status = "Change soil"
        
    if plant.warmth == "High" and data.sen_temp < 25:
        temp_status = "Temperature => Too low. Turning on heater"

    elif plant.warmth == "Mid" and data.sen_temp > 25:
        temp_status = "Temperature => Too high. Turning on ventilation"
        
    elif plant.warmth == "Mid" and data.sen_temp < 15:
        temp_status = "Temperature => Too low. Turning on heater"
    
    elif plant.warmth == "Low" and data.sen_temp > 15:
        temp_status = "Temperature => Too high. Turning on ventilation"
    
    elif plant.warmth == "Low" and data.sen_temp < 0:
        temp_status = "Temperature => Too low. Turning on heater"

    status = f"{temp_status}\n{hidration_status}\n{pH_status}\n{light_status}"
    return status
   