from random import uniform, choices
from app.database import Data
from app.api import get_data_from_url
import datetime

class MockSimulatedPotData:
    def __init__(self):
        self.temp = Sensor(name="Temperature", rand_min=-5, rand_max=45)
        self.hydration = Sensor(name="Hydration", rand_min=0, rand_max=100)
        self.pH = Sensor(name="pH", rand_min=0, rand_max=14)
        self.light = Sensor(name="Light", rand_min=0, rand_max=2)

    def send_data(self, pot_id: int, plant_id: int) -> Data:
        """
        Class method that returns Data object used for adding
        sensor readings to the database.

        Parameters:
        pot_id (int): Pot ID.
        plant_id (int): Plant ID.

        Returns:
        Data: Data object with sensor readings and metadata.
        """
        data = Data()
        data.sen_temp = self.temp.generate_random_value()
        data.sen_pH = self.pH.generate_random_value()
        data.sen_hydration = self.hydration.generate_random_value()
        data.sen_light = self.light.generate_random_light()
        data.sen_date = datetime.datetime.utcnow()
        data.pot_id = pot_id
        data.plant_id = plant_id
        data.api_temp = get_data_from_url()
        return data


class Sensor:
    def __init__(self, name: str, rand_min: float, rand_max: float):
        self.name = name
        self.rand_min = rand_min
        self.rand_max = rand_max

    def generate_random_value(self) -> float:
        """
        Class method used to generate a random float value
        for sensor readings simulation.

        Returns:
        float: Random float value within the specified range.
        """
        return round(uniform(self.rand_min, self.rand_max), 2)

    def generate_random_light(self) -> str:
        """
        Class method used to generate a random light level.

        Returns:
        str: Random light level ('High', 'Mid', or 'Low').
        """
        options = ["High", "Mid", "Low"]
        return choices(options)[0]
