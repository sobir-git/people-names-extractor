from collections import OrderedDict
import unicodedata
import re
import spacy_models


class PersonExtractor:
    def __init__(self, lang='en'):
        self.lang = lang

    def cleanup(self, name):
        # clean non-printable strange characters
        # see the categories https://www.fileformat.info/info/unicode/category/index.htm
        printable_categories = {'Lu', 'Ll', 'Nd', 'Pd', 'Pf', 'Po'}
        chars = []
        for c in name:
            if unicodedata.category(c) in printable_categories:
                chars.append(c)
            # if any kind of space (newline, tab, etc...) just add a ordinary space
            elif unicodedata.category(c) == 'Zs':
                chars.append(' ')
        name = ''.join(chars)

        # remove multiple spaces
        name = re.sub(r'\s+', ' ', name)
        name = name.strip()
        return name

    def extract_people(self, text):
        model = spacy_models.get_model(self.lang)
        doc = model(text)
        # filter person entities
        person_ents = [ent for ent in doc.ents if ent.label_ == 'PERSON']
        # do some cleanup
        result = map(self.cleanup, (ent.text for ent in person_ents))
        # remove duplicates, preserving order
        result = list(OrderedDict.fromkeys(result))
        return result
