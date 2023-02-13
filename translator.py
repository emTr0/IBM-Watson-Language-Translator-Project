'''Functions to translate from English to French and German'''

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
URL= os.getenv('URL')

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def englishtofrench(english):
    '''
    Translate English to French
    '''
    translation = language_translator.translate(
    text=english,
    model_id='en-fr').get_result()
    french_translation = translation['translations'][0]['translation']
    return french_translation

def englishtogerman(english):
    '''
    Translates English to German
    '''
    translation = language_translator.translate(
    text=english,
    model_id='en-de').get_result()
    german_translation = translation['translations'][0]['translation']
    return german_translation
