import heapq
from collections import Counter

def compress_huffman (sample):
    frequency = Counter(sample)
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    huffman_codes = sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))
    huffman_dict = {char: code for char, code in huffman_codes}
    encoded_string = "".join(huffman_dict[char] for char in sample)
    
    return {'encoded_string':encoded_string,'huffman_codes':huffman_dict}

def decompress_huffman (dict):
    code_to_char = {v: k for k, v in dict['huffman_codes'].items()}
    decoded_string = ""
    temp_code = ""

    for bit in dict['encoded_string']:
        temp_code += bit
        if temp_code in code_to_char:
            decoded_string += code_to_char[temp_code]
            temp_code = ""

    return decoded_string

if __name__ == "__main__":

    text = "this is text to compress"
    print(compress_huffman(text))