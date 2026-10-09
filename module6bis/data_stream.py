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

    def get_stats(self) -> tuple[int, int]:
        return self._rank + len(self._data), len(self._data)

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


class DataStream():
    def __init__(self) -> None:
        self._processors: dict[str, DataProcessor] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        name = proc.__class__.__name__.removesuffix("Processor")
        self._processors[name] = proc

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            for proc in self._processors.values():
                if proc.validate(data):
                    proc.ingest(data)
                    break
            else:
                print(
                    "DataStream error - Can't process element in stream:",
                    data
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data\n")
            return

        for name, proc in self._processors.items():
            total, remaining = proc.get_stats()
            print(
                f"{name} Processor: total {total} items processed, " +
                f"remaining {remaining} on processor"
            )
        print()

    def output_element(self, name: str) -> tuple[int, str]:
        return self._processors[name].output()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Numeric Processor")
    stream.register_processor(NumericProcessor())

    data_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {data_batch}")
    stream.process_stream(data_batch)
    stream.print_processors_stats()

    print("Registering other data processors\n")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print("Send the same batch again")
    stream.process_stream(data_batch)
    stream.print_processors_stats()

    print("Consume some elements from the data processors:" +
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        stream.output_element("Numeric")
    for _ in range(2):
        stream.output_element("Text")
    stream.output_element("Log")
    stream.print_processors_stats()
