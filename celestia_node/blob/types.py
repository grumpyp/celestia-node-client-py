from dataclasses import dataclass
from typing import Union


class BlobTypes:
    @dataclass
    class BlobData:
        """
        {
          "namespace": "AAAAAAAAAAAAAAAAAAAAAAAAAAECAwQFBgcICRA=",
          "data": "VGhpcyBpcyBhbiBleGFtcGxlIG9mIHNvbWUgYmxvYiBkYXRh",
          "share_version": 0,
          "commitment": "AD5EzbG0/EMvpw0p8NIjMVnoCP4Bv6K+V6gjmwdXUKU="
        }
        """
        namespace: str
        data: str
        share_version: int
        commitment: str

    @dataclass
    class Proof:
        """
        {
        "end": 4,
        "nodes": [
          "dGVzdA=="
        ],
        "is_max_namespace_ignored": true
      }
      """
        end: int
        nodes: list[str]
        is_max_namespace_ignored: bool

    @dataclass
    class Commitment:
        """
        Bw==
        """
        commitment: str

    @dataclass
    class SubmitOptions:
        """
        {
        "Fee": 42,
        "GasLimit": 42
        }
        """
        fee: int
        gas_limit: int