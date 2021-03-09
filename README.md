# Python-Blockchain-App


A complete blockchain app with UI.

Can add multiple nodes each with their own locally stored blockchain, a Public Key and a Private key.

The blockchain is stored locally in a .txt file.

Wallet saving,loading, and transaction signature verification.

Real SHA256 hashing for the blocks, and proof of work.

Can transfer coins to other wallets/nodes.

A consensus mechanism and the ability to resolve conflicts between blockchains based on the length of the chain and the validity of the transactions.

Can add nodes as peer nodes and automatically broadcast blocks to them. 

The blockchain app is now complete. 

Thie UI will be changed to a use react later on.

There are still some improvements needed to make it into a production ready blockchain.

To start run:   python node.py(will start a node with the default port)

To add a node run: python node.py -p(enter port number here)

Run multiple nodes at the same time to test the consensus mechanism.

