from __future__ import annotations

import json
import os
import random

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field()
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode="after")
    def validate_mission_id(self) -> SpaceMission:
        if self.mission_id.startswith("M"):
            return self
        raise ValueError("Mission ID must start with 'M'")

    @model_validator(mode="after")
    def validate_crew_ranks(self) -> SpaceMission:
        needed_ranks = [m for m in self.crew
                        if m.rank in [Rank.COMMANDER, Rank.CAPTAIN]]
        if not needed_ranks:
            raise ValueError("Mission must have at least one Commander "
                             "or Captain")
        return self

    @model_validator(mode="after")
    def validate_crew_experience(self) -> SpaceMission:
        crew_size = len(self.crew)
        experienced_crew: list[CrewMember] = [
            mem for mem in self.crew if mem.years_experience >= 5
        ]
        experienced_size = len(experienced_crew)
        if self.duration_days > 365 and experienced_size * 2 < crew_size:
            raise ValueError("Long missions (> 365 days) need 50% "
                             "experienced crew (5+ years)")
        return self

    @model_validator(mode="after")
    def validate_crew_statuses(self) -> SpaceMission:
        is_crew_active = all([member.is_active for member in self.crew])
        if not is_crew_active:
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    module_dir: str = os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))
    )
    data_path: str = os.path.join(
        module_dir, "generated_data", "space_missions.json"
    )
    try:
        with open(data_path, encoding="utf-8") as file:
            missions: list[dict[str,str]] = json.load(file)

        mission_data: dict[str,str] = random.choice(missions)
        mission: SpaceMission = SpaceMission.model_validate(mission_data)
    except (OSError, json.JSONDecodeError, ValidationError) as e:
        print(f"Error: {e}")
        return
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) "
              f"- {member.specialization}")
    print("\n=========================================")
    print("Expected validation error:")

    invalid_mission = mission.model_dump()
    for member_data in invalid_mission["crew"]:
        if member_data["rank"] in (Rank.COMMANDER, Rank.CAPTAIN):
            member_data["rank"] = Rank.OFFICER
    try:
        SpaceMission.model_validate(invalid_mission)
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
