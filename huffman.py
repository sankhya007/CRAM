#huffman  

import heapq
from tqdm import tqdm
from collections import Counter

def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

def write_file(filename, encoded_text, codes):
    with open(filename, 'w') as file:
        file.write(''.join(encoded_text) + '\n')
        for char, code in codes.items():
            # included this line because without it the encoding was not storing in the '\n
            escaped = char.replace('\\', '\\\\').replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
            file.write(f'{escaped}: {code}\n')

#encode snippet
def build_huffman_tree(freq_dict): 
    heap = [[wt, [sym, '']] for sym, wt in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]  
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def read_encoded_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    encoded_text = lines[0].strip()
    codes = {}
    for line in lines[1:]:
        parts = line.rstrip('\n').split(': ', 1)
        if len(parts) == 2:
            # same reason as previous
            key = parts[0].replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t').replace('\\\\', '\\')
            codes[key] = parts[1].rstrip('\n')  # strip trailing newline from value
    return encoded_text, codes

def huffman_encode(input_filename, output_filename):
    text = read_file(input_filename)
    if not text:
        print("Input file is empty.")
        return
    freq_dict = Counter(text)
    codes = {sym: code for sym, code in build_huffman_tree(freq_dict)}

    encoded_text = []
    for char in tqdm(text, desc="Encoding", unit="chars"):
        encoded_text.append(codes[char])

    write_file(output_filename, encoded_text, codes)
    print("File encoded successfully.")

def huffman_decode(input_filename, output_filename):
    encoded_text, codes = read_encoded_file(input_filename)
    if not encoded_text:
        print("Input file is empty.")
        return

    reverse_codes = {code: char for char, code in codes.items()}
    max_len = max(len(c) for c in reverse_codes)

    result = []
    i = 0
    total = len(encoded_text)

    with tqdm(total=total, desc="Decoding", unit="bits") as pbar:
        while i < total:
            # try shortest possible match up to max_len
            for length in range(1, max_len + 1):
                chunk = encoded_text[i:i+length]
                if chunk in reverse_codes:
                    result.append(reverse_codes[chunk])
                    pbar.update(length)
                    i += length
                    break
            else:
                print(f"Warning: no match at position {i}")
                break

    with open(output_filename, 'w') as f:
        f.write(''.join(result))
    print("File decoded successfully.")


huffman_encode('all_letters.txt', 'huffman_encoded.txt')
huffman_decode('huffman_encoded.txt', 'huffman_decoded.txt')
