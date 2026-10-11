from __future__ import annotations

import json
import os
import random

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_contact_id(self) -> AlienContact:
        if self.contact_id.startswith("AC"):
            return self
        raise ValueError("Contact ID must start with 'AC'")

    @model_validator(mode="after")
    def validate_strong_signal(self) -> AlienContact:
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError("Signals > 7 should include received messages")
        return self

    @model_validator(mode="after")
    def validate_contact(self) -> AlienContact:
        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type is ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================\n")
    module_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    data_path = os.path.join(
        module_dir, "generated_data", "alien_contacts.json"
    )
    try:
        with open(data_path, encoding="utf-8") as file:
            reports = json.load(file)

        contact_data = random.choice(reports)
        ac = AlienContact.model_validate(contact_data)
    except (OSError, json.JSONDecodeError, ValidationError) as e:
        print(f"Error: {e}")
        return
    print("Valid contact report:")
    print(f"ID: {ac.contact_id}")
    print(f"Type: {ac.contact_type.value}")
    print(f"Location: {ac.location}")
    print(f"Signal: {ac.signal_strength}/10")
    print(f"Duration: {ac.duration_minutes} minutes")
    print(f"Witnesses: {ac.witness_count}")
    print(f"Message: {ac.message_received}")
    print("\n======================================")
    print("Expected validation error:")

    invalid_path = os.path.join(
        module_dir, "generated_data", "invalid_contacts.json"
    )
    try:
        with open(invalid_path, encoding="utf-8") as file:
            invalid_reports = json.load(file)
        invalid_contact = random.choice(invalid_reports)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return
    try:
        AlienContact.model_validate(invalid_contact)
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
