# RLE - run length encoding 

RLE is one of the most early made data compression algorithm ever made, which checks the constructive occurances of the same data and how they are actually sotred. 

## examples
- for example a sequesnce of the colour - red, "red red red red red red" in an image built up from coloured dots could be shortened to "red X 5" 
- or if you are storing a letter more than one time it will store the letter and the number of times the letter appeared as a string of character (example: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa will appear as a50)

---

# LZ77 & LZ78 algorithm 

LZ77 and LZ78 both of them are lossless datacompression algorithms known as lempel-ziv1 (LZ1) and lempel-Ziv2 (LZ2) algorithms lresppectively. Both of them are theaoritically dictionary decoders. 

## LZ77

LZ77 maintains a sliding window during the compression process if a character that is already in the sliding window and it repeats itself while being in the sliding window then rather than storing the whole character we store the distance from the character to the replica that is in the sliding window and the the number of repeated character with that string 

### examples
- so as example if the sliding window has a character "h" and the current character is also "h", and it is 4 characters away than the number that we are viewing right now then we will store <4,1> (<distance, number of characters>). 
- if there was a match in the string of characters meaning the sequence of characters "sun" was in the slising window and then "sun" appears one by one in the current viewing window and the s is 7 charaters away from the "s" itself then we will store <7,3> (3 because the number of characters that matchesthe current entered string) - this is the how the compression works 

## LZ78

LZ78 is a lossless compression algorithm not so similler to LZ77, it does not have a sliding window. LZ78 algorithm builds a sictionary of tokens in sequence from their input, then replacing the sub subsequent occurance of sequence in the data stream with a reference to the dictionary entry. The observation is that the number of repeated seauences is a good measure of non random nature of a sequence. the algo represents the dictionary as an n-ary tree, where the number of tokns used to form token sequence 

### examples
- as example lets take the string of characters "ABABABABABAB" a will be selected as token 1, then b will be denoted as token 2, after that when the window comes to A it will extend the window to the next chacarter because the character A already exists so then the character becomes AB and that gets saved as the token 3, then again we atart with A which extents to B so the token becomes AB, whcich is also in the dictionary so then it extends to ABA(new character) that gets saved in the dictionary as a new token, 4. this is how it will extend for the whole string
- smillerly if we had a sentence, in that we could have found repeating characters in that. if we had a bigger paraghaph then we would have had a better chance of finding characters that repeating the paragraph hence making the compression percentage better and more effectove in the longer riun 

**N.B**: to pick up the compression speed LZ78 algo needs a bit of time to scink up with the file it is compressing first, and when it is done running and capturing the first few 100-200 tokens then it can encode much faster because then it will have the the similler patterns in the paragraph which theaoritically would be much faster to encode 

---

# Huffman encoding 

---

# Deflate 
> appearently we need to combine LZ77 and Huffman to perform this algorithm, will learn later