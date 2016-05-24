
from modeltranslation.translator import translator, TranslationOptions, register

from zinnia.models import Entry, Category


@register(Entry)
class ZinniaEntryTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'lead', 'image_caption', 'excerpt', 'slug')


@register(Category)
class ZinniaCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'slug')
