"""
making a translater
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator.set_service_url(url)
def english_to_french(english_text):
    #write the code here
    french_text = translator.translate(
        text=english_text,
        source='English',
        target='French'
    )
    return french_text


def french_to_english(french_text):
    #write the code here
    english_text=translator.translate(
        text=french_text,
        source='Frensh',
        target='English'
    )
    return english_text
