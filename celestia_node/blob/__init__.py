from .types import BlobTypes
from ..constants import API_PAYLOAD

from typing import List, Dict
from dataclasses import asdict


class Blob:

    def __init__(self, client: "Client") -> None:
        self.client = client

    def get(self, height: int, namespace: str, commitment: str) -> BlobTypes.BlobData:
        """
        Retrieves the blob by its commitment under the specified namespace and height.

        :param height: The blockchain height at which to retrieve the blob.
        :param namespace: The namespace of the blob.
        :param commitment: The commitment (Merkle subtree root) of the blob.
        :return: Response object containing the requested blob.
        """

        API_PAYLOAD["params"] = [height, namespace, commitment]
        API_PAYLOAD["method"] = "blob.Get"

        return self.client.request(API_PAYLOAD)

    def get_all(self, height: int, namespaces: List[str]) -> List[BlobTypes.BlobData]:
        """
        Returns all blobs under the specified namespaces and height.

        :param height: The blockchain height at which to retrieve blobs.
        :param namespaces: A list of namespaces to retrieve blobs from.
        :return: Response object containing all the requested blobs.
        """

        API_PAYLOAD["params"] = [height, namespaces]
        API_PAYLOAD["method"] = "blob.GetAll"

        return self.client.request(API_PAYLOAD)

    def get_proof(self, height: int, namespace: str, commitment: str) -> BlobTypes.Proof:
        """
        Retrieves proofs of the blob in the given namespace at the specified height by commitment.

        :param height: The blockchain height for the proof retrieval.
        :param namespace: The namespace of the blob.
        :param commitment: The commitment of the blob.
        :return: Response object containing the proof of the blob.
        """

        API_PAYLOAD["params"] = [height, namespace, commitment]
        API_PAYLOAD["method"] = "blob.GetProof"

        return self.client.request(API_PAYLOAD)

    def included(self, height: int, namespace: str, proofs: List[Dict], commitment: str) -> bool:
        """
        Checks whether a blob's given commitment is included at the given height and under the specified namespace.

        :param height: The blockchain height to check for inclusion.
        :param namespace: The namespace of the blob.
        :param proofs: The proof of the blob.
        :param commitment: The commitment of the blob.
        :return: Boolean response indicating whether the blob is included.
        """

        proofs_instances = [BlobTypes.Proof(**proof) for proof in proofs]
        proofs_payload = [asdict(proof_instance) for proof_instance in proofs_instances]

        API_PAYLOAD["params"] = [height, namespace, proofs_payload, commitment]
        API_PAYLOAD["method"] = "blob.Included"

        return self.client.request(API_PAYLOAD)

    def submit(self, blobs: List[Dict], options: Dict) -> int:
        """
        Submits blobs and returns the height at which they were included. Allows sending multiple blobs atomically.

        :param blobs: A list of blobs to be submitted.
        :param options: Additional options for the submission.
        :return: The blockchain height at which the blobs were included.
        """

        blobs_instances = [BlobTypes.BlobData(**blob) for blob in blobs]
        options_instance = BlobTypes.SubmitOptions(**options)

        blobs_payload = [asdict(blob) for blob in blobs_instances]
        options_payload = asdict(options_instance)

        API_PAYLOAD["params"] = [blobs_payload, options_payload]
        API_PAYLOAD["method"] = "blob.Submit"

        return self.client.request(API_PAYLOAD)
