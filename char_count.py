
"""Vai su https://docs.python.org/3/howto/argparse.html
per info sul modulo argparse"""

import os
import argparse
import logging
import time
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

start = time.time()
message = 'Measure the relative frequencies of characters in a .txt file'

def charcount(file_path):
    """Main processing routine"""
    # basic check on the text file
    assert file_path.endswith('.txt')
    assert os.path.isfile(file_path)

    logging.info('Opening file %s...', file_path)
    with open(file_path) as input_file:
        data = input_file.read()

    # create a dictionary with all the counts initialized to zero
    letters = 'abcdefghijklmnopqrstuvwxyz'
    occ = {}
    for ch in letters:
        occ[ch] = 0

    # loop over all the data and compute the (total) frequencies
    # for every letter
    for ch in data.lower():
        if ch in letters:
            occ[ch] += 1
    #another loop to compute the relative frequencies
    N_char = sum(occ.values())
    print('{} characters founded'.format(N_char))
    for ch in letters:
        occ[ch] /= N_char
        print('{}: {:.3f}%'.format(ch, occ[ch]*100))

    #time for the istogram!
    plt.bar(list(occ.keys()), occ.values(), color = 'g')
    plt.title('Relative frequencies of characters')
    plt.xlabel('letters')
    plt.ylabel('relative frequencies')
    plt.show()



if __name__=='__main__':
    parser = argparse.ArgumentParser(description=message)
    parser.add_argument('infile', help='path to the input text file')
    args = parser.parse_args() #assegna gli argomenti ai parametri
    charcount(args.infile)
end = time.time()
elapsed = end - start
print('Elapsed time: {:.3f} s'.format(elapsed))
