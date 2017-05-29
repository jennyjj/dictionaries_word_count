# put your code here.
def count_word(file_name):
    """given a text file, counts number of time a word appers in a text file and returns the word and number of times it appears"""
    # open_file = 

    count_of_words = {}


    with open(file_name) as open_file:
        for line in open_file:
            line = line.strip()
            data = line.split()
            for word in data:
                count_of_words[word] = count_of_words.get(word, 0) + 1

    # open_file.close()

    for word, count in count_of_words.iteritems():
        print '%s %d' % (word, count)




count_word("twain.txt")
