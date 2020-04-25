import spacy

models = {}


def get_model(lang):
    # if models is already loaded
    if lang in models:
        return models[lang]

    # load model from disk
    if lang == 'en':
        model = spacy.load('en_core_web_sm')
        # put model in models dict
        models[lang] = model
        return model
    else:
        raise ValueError('No such model, sorry')
