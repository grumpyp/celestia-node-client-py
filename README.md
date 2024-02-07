# Celestia Node RPC SDK
[![PyPI version](https://badge.fury.io/py/celestia-node.svg)](https://badge.fury.io/py/celestia-node)

This Python SDK provides a convenient way to interact with the [Celestia Node RPC](https://docs.celestia.org/developers/node-tutorial).

**It is currently in development and will be updated as more endpoints are added.**

## Supported Endpoints
https://node-rpc-docs.celestia.org/?version=v0.12.1

- **Blob**
- **Das**
- **Fraud** *(Coming Soon)*
- **Header** *(Coming Soon)*
- **Node** *(Coming Soon)*
- **P2P** *(Coming Soon)*
- **Share** *(Coming Soon)*
- **State** *(Coming Soon)*


### Installation
To install this sdk use the [pip package manager](https://pip.pypa.io/en/stable/):
```
pip install celestia_node
```

### Usage
```
import celestia_node

# Create a Celestia Node client
client = celestia_node.Client()
```
#### For more details please check the `sample.py`-files
