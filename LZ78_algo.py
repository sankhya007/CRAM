import io

def encoder(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): chr(i) for i in range(dict_size)}

    w = ""
    result = []
    for k in uncompressed:
        wk = w + k
        if wk in dictionary:
            w = wk
        else:
            result.append(dictionary[w])
            # Add wk to the dictionary.
            dictionary[wk] = dict_size
            dict_size += 1
            w = k

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result


def decoder(compressed):
    """Decompress a list of output ks to a string."""

    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): chr(i) for i in range(dict_size)}

    # use io.StringIO(), otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = io.StringIO()
    w = compressed.pop(0)
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()



SEPERATOR = "\x00SPLIT\x00"  #something like this has a really low chance of appearing in a normal text file 

# encode block 
try: 
    with open("example.txt", "r") as a, open("example1.txt", "r") as b: 
        encode_text = (a.read() + SEPERATOR + b.read())
    with open("compressed_LZ78.bin", "w") as f: 
        compressed = encoder(encode_text)
        print(compressed, file=f)
except FileNotFoundError:
    print("file not found. please check if the file exist in the root folder....") 
    raise
print("compression complete.")

# decode block 
decompressed = decoder(compressed)
     
parts = decompressed.split(SEPERATOR)  #split the decompressed text into parts using the separator
try:
    for i, part in enumerate(parts): 
        with open(f"decompressed_LZ78_part{i+1}.txt", "w") as f: 
            print(part, file=f)
except FileNotFoundError:
    print("file not found. please check if the file exist in the root folder....") 
    raise 
print("decompression complete.")

print()
