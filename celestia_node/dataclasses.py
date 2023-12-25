from dataclasses import dataclass
from typing import Union


class Blob:
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


class Das:

    @dataclass
    class SamplingStats:

        @dataclass
        class Worker:
            job_type: str
            current: int
            start: int
            end: int


        head_of_sampled_chain: int
        head_of_catchup: int
        network_head_height: int
        workers: list[Worker]
        concurrency: int
        catch_up_done: bool
        is_running: bool



RESPONSE_TYPES = Union[Blob, Das]

@dataclass
class JsonRPCResponse:
    id: int
    jsonrpc: str
    result: list[RESPONSE_TYPES]