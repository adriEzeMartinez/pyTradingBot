class Position:
    """ Currently held asset position. """
    def __init__(self, broker: 'Broker', symbol: str, position: Positions):
        self._id = str(uuid.uuid4())
        self._symbol = symbol
        self._broker = broker
        self._position = position
    def describe(self):
        return f"<Position id: {self._id} symbol: {self._symbol} position: {self._position} Size: {self.size} stop: {self.profit_loss}>"
    #  Getters
    @property
    def size(self) -> float:
        total_size = 0
        for trade in self._broker.trades:
            if trade.symbol != self.symbol or trade.position != self._position:
                continue
            total_size += trade.size
        return total_size
    @property
    def profit_loss(self) -> float:
        """ P/L of current position in cash units. """
        return sum(trade.profit_loss for trade in self._broker.trades)
    @property
    def position(self) -> Positions:
        return self._position