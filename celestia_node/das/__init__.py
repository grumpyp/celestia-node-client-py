from .types import DasTypes
from ..constants import API_PAYLOAD


class Das:

    def __init__(self, client: "Client") -> None:
        self.client = client

    def sampling_stats(self) -> DasTypes.SamplingStats:
        """
        SamplingStats returns the current statistics over the DA sampling process.
        """

        API_PAYLOAD["params"] = []
        API_PAYLOAD["method"] = "das.SamplingStats"

        return self.client.request(API_PAYLOAD)

    def wait_catchup(self) -> DasTypes.CatchupResponse:
        """
        WaitCatchUp blocks until DASer finishes catching up to the network head.
        """

        API_PAYLOAD["params"] = []
        API_PAYLOAD["method"] = "das.WaitCatchUp"

        return self.client.request(API_PAYLOAD)