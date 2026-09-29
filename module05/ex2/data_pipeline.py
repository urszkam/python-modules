from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    @abstractmethod
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        output = [
            tup[1] if "," not in tup[1] else f'"{tup[1]}"'
            for tup in data
        ]

        print("CSV OUTPUT:")
        print(",".join(output))


class JsonExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        output = [f'"item_{rank}": "{value}"' for rank, value in data]

        print("JSON OUTPUT:")
        print("{" + ",".join(output) + "}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors.values():
            proc_data: list[tuple[int, str]] = []
            try:
                for _ in range(nb):
                    proc_data.append(proc.output())
            except IndexError:
                pass
            finally:
                plugin.process_output(proc_data)

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


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

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

    print("Send 3 processed data from each processor to a CSV plugin:")

    csv_plugin = CsvExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    print()
    stream.print_processors_stats()

    data_batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print(f"Send another batch of data: {data_batch2}")
    stream.process_stream(data_batch2)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JsonExportPlugin()
    stream.output_pipeline(5, json_plugin)
    print()
    stream.print_processors_stats()
