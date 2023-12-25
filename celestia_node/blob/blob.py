from .types import Blob
from typing import List


class Blob:

    def __init__(self, client: "Client") -> None:
        self.client = client

    def get(self, height: int, namespace: str, commitment: str) -> Blob.BlobData:
        """
        Retrieves the blob by its commitment under the specified namespace and height.

        :param height: The blockchain height at which to retrieve the blob.
        :param namespace: The namespace of the blob.
        :param commitment: The commitment (Merkle subtree root) of the blob.
        :return: Response object containing the requested blob.
        """
        method = "blob.Get"

        return self.client.request('GET')

    def get_all(self, height: int, namespaces: List[str]) -> List[Blob.BlobData]:
        """
        Returns all blobs under the specified namespaces and height.

        :param height: The blockchain height at which to retrieve blobs.
        :param namespaces: A list of namespaces to retrieve blobs from.
        :return: Response object containing all the requested blobs.
        """
        method = "blob.GetAll"
        return self.client.request('GET', f"{self.path}/all/{height}/" + ",".join(namespaces))

    def get_proof(self, height: int, namespace: str, commitment: str) -> Blob.Proof:
        """
        Retrieves proofs of the blob in the given namespace at the specified height by commitment.

        :param height: The blockchain height for the proof retrieval.
        :param namespace: The namespace of the blob.
        :param commitment: The commitment of the blob.
        :return: Response object containing the proof of the blob.
        """
        method = "blob.GetProof"
        return self.client.request('GET', f"{self.path}/proof/{height}/{namespace}/{commitment}")

    def included(self, height: int, namespace: str, proof: Blob.Proof, commitment: Blob.Comitment) -> bool:
        """
        Checks whether a blob's given commitment is included at the given height and under the specified namespace.

        :param height: The blockchain height to check for inclusion.
        :param namespace: The namespace of the blob.
        :param proof: The proof of the blob.
        :param commitment: The commitment of the blob.
        :return: Boolean response indicating whether the blob is included.
        """
        method = "blob.Included"
        
        return self.client.request(method, json={"blobs": payload, "options": options.__dict__})

    def submit(self, blobs: List[Blob.BlobData], options: Blob.SubmitOptions) -> int:
        payload = [blob.__dict__ for blob in blobs]
        method = "blob.Submit"
        print(payload)
        return self.client.request(method, json={"blobs": payload, "options": options.__dict__})

