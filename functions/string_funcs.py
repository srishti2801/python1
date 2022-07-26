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