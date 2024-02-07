from dataclasses import dataclass
from typing import Any, List

class DasTypes:

    @dataclass
    class CatchupResponse:
        """
        {
        "id": 1,
        "jsonrpc": "2.0",
        "result": []
        }
        """
        id: int
        jsonrpc: float
        result: List[Any]


    @dataclass
    class Worker:
        """
        {
        "end": 4,
        "nodes": [
          "dGVzdA=="
        ],
        "is_max_namespace_ignored": true
        }
        """
        job_type: str
        end: int
        nodes: list[str]
        is_max_namespace_ignored: bool

    @dataclass
    class SamplingStats:
        """
        {
            "head_of_sampled_chain": 1092,
            "head_of_catchup": 34101,
            "network_head_height": 470292,
            "workers": [
                {
                    "job_type": "catchup",
                    "current": 1093,
                    "from": 1002,
                    "to": 1101
                },
                {
                    "job_type": "catchup",
                    "current": 33343,
                    "from": 33302,
                    "to": 33401
                },
                {
                    "job_type": "catchup",
                    "current": 34047,
                    "from": 34002,
                    "to": 34101
                },
                {
                    "job_type": "catchup",
                    "current": 1327,
                    "from": 1302,
                    "to": 1401
                },
                {
                    "job_type": "catchup",
                    "current": 1197,
                    "from": 1102,
                    "to": 1201
                },
                {
                    "job_type": "catchup",
                    "current": 1408,
                    "from": 1402,
                    "to": 1501
                }
            ],
            "concurrency": 6,
            "catch_up_done": false,
            "is_running": true
        }
        """
        head_of_sampled_chain: int
        head_of_catchup: int
        network_head_height: int
        workers: List['DasTypes.Worker']
        concurrency: int
        catch_up_done: bool
        is_running: bool