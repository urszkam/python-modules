class InvalidStrategyException(Exception):
    def __init__(self, name: str, strategy: str):
        self._message = (
            f"Battle error, aborting tournament: Invalid Creature '{name}' "
            f"for this {strategy} strategy"
        )
        super().__init__(self._message)
