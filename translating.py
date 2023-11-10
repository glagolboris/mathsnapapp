from translatepy.translators.google import GoogleTranslate


def translate(txt):
    gtranslate = GoogleTranslate()
    return gtranslate.translate(txt, 'Russian')
