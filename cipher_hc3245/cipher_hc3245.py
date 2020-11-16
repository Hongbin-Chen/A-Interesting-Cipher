def cipher(text, shift, encrypt=True):
    """
    1. Description:
    The Caesar cipher is one of the simplest and most widely known encryption techniques. In short, each letter is replaced by a letter some fixed number of positions down the alphabet. Apparently, Julius Caesar used it in his private correspondence.
    2. Explanation:
    The first input is a string that you want to decipher
    The second input is the amount of shift for each letters in that string
    The output will be the outcome of the orginal string after a certain shifting.
    3. Example:
    If you put "gdkkn" and 1 in the cipher function like this: cipher("gdkkn", 1),
    you will get "hello"
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text