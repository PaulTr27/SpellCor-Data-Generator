import random

def return_indices(sentence_1, sentence_2,types_error):
    Error_Dict = {'No Error':0, 
               'Telex Typing Error':1,
               'VNI Typing Error':2,
               'Missing Diacritical Marks':3,
               'Excess Letter Error': 4,
               'Missing Letter Error':5,
               'Wrong Spelling Error': 6
              }
    result = []
    for word_1, word_2 in zip(sentence_1.split(),sentence_2.split()):
        if word_1 == word_2:
            result.append(0)
        else:
            result.append(Error_Dict[types_error])
    return result
def No_Error(text):
    return text

def Telex_Typing_Error(text):
    telex_dict = {'à': 'af', 'á': 'as', 'ả': 'ar', 'ã': 'ax', 'ạ': 'aj',
             'ă': 'aw', 'ằ': ['awf', 'afw'], 'ắ': ['aws' ,'asw'], 'ẳ': ['awr', 'arw'], 'ẵ': ['awx', 'axw'], 'ặ': ['awj','ajw'],
             'â': 'aa', 'ầ': ['aaf', 'afa'], 'ấ': ['aas', 'asa'], 'ẩ': ['aar', 'ara'], 'ẫ': ['aax', 'axa'], 'ậ': ['aaj','aja'],
             'è': 'ef', 'é' : 'es', 'ẻ': 'er', 'ẽ': 'ex', 'ẹ': 'ej',
             'ê': 'ee', 'ề': ['eef', 'efe'], 'ế': ['ees', 'ese'], 'ể': ['eer', 'ere'], 'ễ': ['eex', 'exe'], 'ệ': ['eej','eje'],
             'ì': 'if', 'í': 'is', 'ỉ': 'ir', 'ĩ': 'ix', 'ị':'ij',
              'ò': 'of', 'ó':'os', 'ỏ': 'or', 'õ': 'ox', 'ọ': 'oj',
              'ô': 'oo', 'ồ': ['oof', 'ofo'], 'ố': ['oos', 'oso'], 'ổ': ['oor', 'oro'], 'ỗ': ['oox', 'oxo'], 'ộ': ['ooj', 'ojo'],
              'ơ': 'ow', 'ờ': ['owf', 'ofw'], 'ớ': ['ows', 'osw'], 'ở': ['owr', 'orw'], 'ỡ': ['owx', 'oxw'], 'ợ': ['owj', 'ojw'],
              'ù': 'uf', 'ú': 'us', 'ủ': 'ur', 'ũ': 'ux', 'ụ': 'uj',
              'ư': 'uw', 'ừ': ['uwf', 'ufw'], 'ứ': ['uws', 'usw'], 'ử': ['uwr', 'urw'], 'ữ': ['uwx', 'uxw'], 'ự': ['uwj', 'ujw'],
              'ỳ': 'yf', 'ý': 'ys', 'ỷ': 'yr', 'ỹ': 'yx', 'ỵ': 'yj',
              'đ': 'dd'
              }
    telex_sentence = ''
    true_sentence = text
    for char in text: 
        if char.lower() in telex_dict:
            if type(telex_dict[char.lower()]) == list:
                if random.random() <= 0.8:
                    telex_char = telex_dict[char.lower()][0]
                else:
                    telex_char = telex_dict[char.lower()][1]
            else:

                telex_char = telex_dict[char.lower()]
            if char.isupper():
                    telex_char = telex_char.title()
            telex_sentence += telex_char 
        else:
            telex_sentence += char
    return telex_sentence, return_indices(true_sentence, telex_sentence,'Telex Typing Error')

def VNI_Typing_Error(text):
    vni_dict = {'à': 'a2', 'á': 'a1', 'ả': 'a3', 'ã': 'a4', 'ạ': 'a5',
             'ă': 'a8', 'ằ': ['a82', 'a28'], 'ắ': ['a81' ,'a18'], 'ẳ': ['a83', 'a38'], 'ẵ': ['a84', 'a48'], 'ặ': ['a85','a58'],
             'â': 'a6', 'ầ': ['a62', 'a26'], 'ấ': ['a61', 'a16'], 'ẩ': ['a63', 'a36'], 'ẫ': ['a64', 'a46'], 'ậ': ['a65','a56'],
             'è': 'e2', 'é' : 'e1', 'ẻ': 'e3', 'ẽ': 'e4', 'ẹ': 'e5',
             'ê': 'e6', 'ề': ['e62', 'e26'], 'ế': ['e61', 'e16'], 'ể': ['e63', 'e36'], 'ễ': ['e64', 'e46'], 'ệ': ['e65','e56'],
             'ì': 'i2', 'í': 'i1', 'ỉ': 'i3', 'ĩ': 'i4', 'ị':'i5',
              'ò': 'o2', 'ó':'o1', 'ỏ': 'o3', 'õ': 'o4', 'ọ': 'o5',
              'ô': 'o6', 'ồ': ['o62', 'o26'], 'ố': ['o61', 'o16'], 'ổ': ['o63', 'o36'], 'ỗ': ['o64', 'o46'], 'ộ': ['o65', 'o56'],
              'ơ': 'o7', 'ờ': ['o72', 'o27'], 'ớ': ['o71', 'o17'], 'ở': ['o73', 'o37'], 'ỡ': ['o74', 'o47'], 'ợ': ['o75', 'o57'],
              'ù': 'u2', 'ú': 'u1', 'ủ': 'u3', 'ũ': 'u4', 'ụ': 'u5',
              'ư': 'u7', 'ừ': ['u72', 'u27'], 'ứ': ['u71', 'u17'], 'ử': ['u73', 'u37'], 'ữ': ['u74', 'u47'], 'ự': ['u75', 'u57'],
              'ỳ': 'y2', 'ý': 'y1', 'ỷ': 'y3', 'ỹ': 'y4', 'ỵ': 'y5',
              'đ': 'd9'
              }
    vni_sentence = ''
    true_sentence = text
    indices = []
    for char in text: 
        if char.lower() in vni_dict:
            if type(vni_dict[char.lower()]) == list:
                if random.random() <= 0.8:
                    vni_char = vni_dict[char.lower()][0]
                else:
                    vni_char = vni_dict[char.lower()][1]
            else:

                vni_char = vni_dict[char.lower()]
            if char.isupper():
                    vni_char = vni_char.title()
            vni_sentence += vni_char 
        else:
            vni_sentence += char
    return vni_sentence, return_indices(true_sentence, vni_sentence, 'VNI Typing Error') 

def Missing_Diacritical_Marks(text):
    non_diacritical_mark_dict = {
        'à': 'a', 'á': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
        'ă': 'a', 'ằ': 'a', 'ắ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
        'â': 'a', 'ầ': 'a', 'ấ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
        'è': 'e', 'é': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
        'ê': 'e', 'ề': 'e', 'ế': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
        'ì': 'i', 'í': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
        'ò': 'o', 'ó': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
        'ô': 'o', 'ồ': 'o', 'ố': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
        'ơ': 'o', 'ờ': 'o', 'ớ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
        'ù': 'u', 'ú': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
        'ư': 'u', 'ừ': 'u', 'ứ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
        'ỳ': 'y', 'ý': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
        'đ': 'd'
    }
    non_diacritic_sentence = ''
    true_sentence = text
    for char in text:
        if char.lower() in non_diacritical_mark_dict:
            new_char = non_diacritical_mark_dict[char.lower()]
            if char.isupper():
               new_char = new_char.title()    
            non_diacritic_sentence += new_char

        else:
            non_diacritic_sentence += char
    return non_diacritic_sentence, return_indices(true_sentence, non_diacritic_sentence, 'Missing Diacritical Marks')
  
def random_words(sentence):
    words = sentence.split()
    long_words = [word for word in words if len(word) > 2]
    num_words = random.randint(1, min(3, len(long_words)))
    return ' '.join(random.sample(long_words, num_words))
def make_longer(word):
    vowels = ['a', 'e', 'i', 'o', 'u','y']
    consonants = ['b', 'c', 'd', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x']
    length = random.randint(1, 2)
    for i in range(length):
        if word[-1] in vowels:
            if random.random() < 0.7:
                word += random.choice(consonants)
            else:
                word += random.choice(vowels)
        else:
            if random.random() < 0.7:
                word += random.choice(vowels)
            else:
                word += random.choice(consonants)
    return word
def Excess_Letter_Error(text):
    true_sentence = text
    words = text.split()
    new_words = []
    for i,word in enumerate(words):
        if word in random_words(text):
            new_words.append(make_longer(word)) 
        else:
            new_words.append(word)
    return ' '.join(new_words), return_indices(true_sentence, ' '.join(new_words), 'Excess Letter Error')
def remove_letters(word):
    length = 1
    indices = random.sample(range(len(word)), length) 
    new_word = ''
    for i in range(len(word)):
        if i in indices:
            new_word += '_'
        else:
            new_word += word[i]
    new_word = new_word.replace("_",'')
    return new_word
def Missing_Letter_Error(text):
    true_sentence = text
    words = text.split()
    new_words = []
    for i, word in enumerate(words):
        if word in random_words(text):
            new_word = remove_letters(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return ' '.join(new_words), return_indices(true_sentence, ' '.join(new_words), 'Missing Letter Error')
