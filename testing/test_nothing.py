from pkt.core import Packet


def test_nothing():
    assert Packet(b"123")
