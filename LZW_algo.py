import json

def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result

def decompress(compressed):
    """Decompress a list of output ks to a string."""

    # Build the dictionary.
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    w = dictionary[compressed[0]]
    result = [w]
    
    for k in compressed[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)

        # Add w+entry[0] to the dictionary.
        result.append(entry)
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
        
    return "".join(result)

# # encode block 
# try:
#     print("file found, processing...")
#     with open("example.txt", "r") as f: # read the file and store
#         encoded_text = f.read()
#     compressed = compress(encoded_text)
#     with open("LZW_compressed.bin", "w") as f: # compress and then store in bin
#         json.dump(compressed, f)
#     print("File was compressed successfully...")
# except FileNotFoundError: 
#     print("file was not found in the root folder...")  


# decode block
try: 
    print("file found, starting to process...")
    with open("lzw_compressed.bin", "r") as f: 
        decode_text = json.load(f)
    decompressed = decompress(decode_text)
    with open("lzw_decoded.txt", "w") as f: 
        f.write(decompressed)
    print("File decompression was done successfully...")
except FileNotFoundError:
    print("file was not found in the root folder...") 
        

print()
    
