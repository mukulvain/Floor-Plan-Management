import hashlib


class MerkleTree:
    def __init__(self):
        self.leaves = []  # List to store leaf nodes
        self.root = None  # Root node of the Merkle tree

    def create_tree(self, data):
        self.leaves = [
            self.hash_leaf(d) for d in data
        ]  # Hash each data element to create leaf nodes
        self.root = self.build_tree(self.leaves)  # Build the Merkle tree

    def verify(self, data, root_hash):
        computed_root = self.compute_root_hash(data)
        return (
            computed_root == root_hash
        )  # Compare computed root hash with provided root hash

    def hash_leaf(self, data):
        return hashlib.sha256(
            str(data).encode()
        ).hexdigest()  # Hash function (can use any suitable hash)

    def build_tree(self, nodes):
        if len(nodes) == 1:
            return nodes[0]

        next_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = (
                nodes[i + 1] if i + 1 < len(nodes) else left
            )  # For odd number of nodes, duplicate the last node
            combined_hash = self.combine_hashes(left, right)
            next_level.append(combined_hash)

        return self.build_tree(next_level)

    def combine_hashes(self, left, right):
        return hashlib.sha256(
            (left + right).encode()
        ).hexdigest()  # Combine hashes (e.g., concatenate and hash)

    def compute_root_hash(self, data):
        leaf_hashes = [self.hash_leaf(d) for d in data]
        root = self.build_tree(leaf_hashes)
        return root


if __name__ == "__main__":
    data = ["Data Chunk 1", "Data Chunk 2", "Data Chunk 3", "Data Chunk 4"]
    merkle_tree = MerkleTree()
    merkle_tree.create_tree(data)
    root_hash = merkle_tree.root
    is_valid = merkle_tree.verify(data, root_hash)

    print("Data integrity is valid:", is_valid)
