# This is a sample to show how to use the Celestia Node Python client.
# DAS endpoints are used in this sample.
# https://node-rpc-docs.celestia.org/?version=v0.12.1#das

import celestia_node

# Create a Celestia Node client
client = celestia_node.Client()

# Submit blobs using the 'submit' method
submitted_blob = celestia_node.Das(client).submit(blobs_json, options_json)

# Define variables for height, namespace, proofs, and commitment
height = 42
namespace = "AAAAAAAAAAAAAAAAAAAAAAAAAAECAwQFBgcICRA="
proofs_json = [
    {
        "end": 4,
        "nodes": ["dGVzdA=="],
        "is_max_namespace_ignored": True
    }
]
commitment = "Bw=="

# Check if a blob is included at a specific height
included_result = celestia_node.Blob(client).included(height, namespace, proofs_json, commitment)

# Get a proof for a blob at a specific height and namespace
proof_result = celestia_node.Blob(client).get_proof(height, namespace, commitment)

# Get all blobs for specified namespaces at a specific height
namespaces = [namespace, namespace]
all_result = celestia_node.Blob(client).get_all(height, namespaces)

# Get a specific blob by height, namespace, and commitment
get_result = celestia_node.Blob(client).get(height, namespace, commitment)
