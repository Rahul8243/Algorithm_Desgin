import heapq
from collections import defaultdict, Counter

# Node for Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq

# Step 1: Build Huffman Tree
def build_huffman_tree(text):
    freq_table = Counter(text)
    heap = [Node(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left, merged.right = node1, node2
        heapq.heappush(heap, merged)

    return heap[0], freq_table

# Step 2: Generate Huffman Codes
def generate_codes(node, prefix="", code_map={}):
    if node:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    return code_map

# Step 3: Encode
def encode(text, code_map):
    return "".join(code_map[ch] for ch in text)

# Step 4: Decode
def decode(encoded_text, root):
    decoded = []
    node = root
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.char:
            decoded.append(node.char)
            node = root
    return "".join(decoded)

# Step 5: Compression Ratio
def compression_ratio(text, encoded_text):
    original_bits = len(text) * 8
    compressed_bits = len(encoded_text)
    return compressed_bits / original_bits

# -----------------------------
# Driver Code
# -----------------------------
if __name__ == "__main__":
    text = "huffman coding is fun"

    root, freq_table = build_huffman_tree(text)
    code_map = generate_codes(root)

    print("Frequency Table:", dict(freq_table))
    print("Huffman Codes:", code_map)

    encoded = encode(text, code_map)
    decoded = decode(encoded, root)

    print("\nEncoded Text:", encoded)
    print("Decoded Text:", decoded)
    print("Compression Ratio:", compression_ratio(text, encoded))
