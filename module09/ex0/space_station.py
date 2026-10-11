import json
import os
import random

from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime = Field()
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================\n")
    print("Valid station created:")
    module_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    data_path = os.path.join(
        module_dir, "generated_data", "space_stations.json"
    )
    try:
        with open(data_path, encoding="utf-8") as file:
            stations = json.load(file)
        station_data = random.choice(stations)
        station = SpaceStation.model_validate(station_data)
    except (OSError, json.JSONDecodeError, ValidationError) as e:
        print(f"Error: {e}")
        return
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Non-operational"
    print(f"Status: {status}")
    print("\n========================================")
    print("Expected validation error:")
    invalid_path = os.path.join(
        module_dir, "generated_data", "invalid_stations.json"
    )
    try:
        with open(invalid_path, encoding="utf-8") as file:
            invalid_stations = json.load(file)
        invalid_station = random.choice(invalid_stations)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return
    try:
        SpaceStation.model_validate(invalid_station)
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
