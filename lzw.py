#Purpose: An implementation of the Lempel-Ziv-Welch compression algorithm

#compress a string to a list of output symbols
def compress(uncompressed_string):

    #build the dictionary
    dict_size = 256
    #d = dict((key, value) for (key, value) in interable
    dictionary = dict((chr(i), i) for i in xrange(dict_size))

    w = ""
    result = []
    for c in uncompressed_string:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            #add w to the output
            result.append(dictionary[w])
            #add wc to the dictionary
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    if w:
        result.append(dictionary[w])

    return result

#count bits assuming algorithm uses variable-width codes
def calculate_bits(result, is_compressed):

    size = len(result)
    total_bits = 0

    #characters are stored in 9-12 bits if compressed
    if is_compressed:
        num_bits = 0 
        for ascii_value in result:
            if (ascii_value >= 0) and (ascii_value < 512) and (num_bits < 9):
                num_bits = 9
            elif (ascii_value >= 512) and (ascii_value < 1024) and (num_bits < 10):
                num_bits = 10
            elif (ascii_value >= 1024) and (ascii_value < 2048) and (num_bits < 11):
                num_bits= 11
            elif (ascii_value >= 2048) and (num_bits < 11):
                num_bits = 12
            else:
                pass
            total_bits += num_bits 

    #characters are stored in 8 bits if uncompressed
    else:
        total_bits = size * 8

    return total_bits
