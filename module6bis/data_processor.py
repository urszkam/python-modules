from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data in processor.")
        result = (self._rank, self._data.pop(0))
        self._rank += 1

        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        match data:
            case bool():
                return False
            case int() | float():
                return True
            case list() if all([
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            ]):
                return True
            case _:
                return False

    def ingest(
            self,
            data: int | float | list[int] | list[float] | list[int | float]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Incorrect data input")

        match data:
            case int() | float():
                self._data.append(str(data))
            case list():
                self._data.extend([str(val) for val in data])


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        match data:
            case str():
                return True
            case list() if all([isinstance(x, str) for x in data]):
                return True
            case _:
                return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Incorrect data input")

        match data:
            case str():
                self._data.append(data)
            case list():
                self._data.extend(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        match data:
            case dict() if all(
                [isinstance(x, str) for x in [*data.keys(), *data.values()]]
            ):
                return True
            case list() if all(
                isinstance(item, dict) and self.validate(item)
                for item in data
            ):
                return True
            case _:
                return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Incorrect data input")

        logs = [data] if isinstance(data, dict) else data
        for log in logs:
            if "log_level" in log and "log_message" in log:
                self._data.append(
                    f"{log['log_level']}: {log['log_message']}"
                )
            else:
                self._data.append(str(log))


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()

    print("Testing Numeric Processor...")
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")
    num_data = [1, 2, 3, 4, 5]
    print(f" Processing data: {num_data}")
    num_proc.ingest(num_data)
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f" Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    print(f" Trying to validate input '42': {txt_proc.validate(42)}")
    txt_data = ["Hello", "Nexus", "World"]
    print(f" Trying to validate input {txt_data}: "
          f"{txt_proc.validate(txt_data)}")
    print(f" Processing data: {txt_data}")
    txt_proc.ingest(txt_data)
    print(" Extracting 1 value...")
    for _ in range(1):
        rank, val = txt_proc.output()
        print(f" Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f" Trying to validate input {log_data}: "
          f"{log_proc.validate(log_data)}")
    print(f" Processing data: {log_data}")
    log_proc.ingest(log_data)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f" Log value {rank}: {val}")
