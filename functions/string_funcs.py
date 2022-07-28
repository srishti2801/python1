from os import supports_effective_ids
from string import punctuation

def remove_punc(text):
    '''
    Remove punctuation from a text and return cleaned text

    `clean_text = remove_punc(text)`
    '''
    for punc in punctuation:
        text = text.replace(punc, '')
    return text



if __name__ == "__main__":
    msg = "_!@#)1this($!)(@# ) is) a) string)"
    cln_text = remove_punc(msg)
    print('original:',msg)
    print('cleaned:', cln_text)


# WAF to replace all the multiple spaces into a single space

def spaces(msg):
    new_msg = " ".join(msg.split())
    return new_msg


if __name__ == "__main__":
    print(spaces("My     name    is     Srishti"))




def word_count(text):
    wordlist = text.lower().split()
    wc = {}
    for word in wordlist:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
    return wc 


def sort(word_dict):
    ans = sorted(word_dict.items(),key=lambda val: val[1],reverse=True)
    return(dict(ans))


if __name__ == "__main__":
    long_text = '''
    The quick brown fox jumps over the lazy dog,
    and attacks the chicken with a flying kick.
    This is real life story about a fox, that could
    kick and jump. If you are really interested in
    this story, then keep reading. The End
    '''
    cl_text = remove_punc(long_text)
    counted_word = word_count(cl_text)
    print(counted_word)
    sorted_word = sort(counted_word)
    print(sorted_word)


