# This file is under MIT license. The license file can be obtained in the root directory of this module.

from sacn.messages.data_packet import DataPacket


class Output:
    """
    This class is a compact representation of an sending with all relevant information
    """

    def __init__(self, packet: DataPacket, last_time_send: int = 0, destination: str = '127.0.0.1',
                 multicast: bool = False, ttl: int = 8,destination_port: int= 5568):
        self._packet: DataPacket = packet
        self._last_time_send: int = last_time_send
        self.destination: str = destination
        self.destination_port: int = destination_port
        self.multicast: bool = multicast
        self.ttl: int = ttl
        self._changed: bool = False

    @property
    def dmx_data(self) -> tuple:
        return self._packet.dmxData

    @dmx_data.setter
    def dmx_data(self, dmx_data: tuple):
        self._packet.dmxData = dmx_data
        self._changed = True

    @property
    def priority(self) -> int:
        return self._packet.priority

    @priority.setter
    def priority(self, priority: int):
        self._packet.priority = priority

    @property
    def destinationPort(self) -> int:
        return self._packet.destination_port

    @destinationPort.setter
    def destinationPort(self, destination_port: int):
        self._packet.destination_port = destination_port
        
    
