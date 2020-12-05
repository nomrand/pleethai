from django import template
from pleethai.models import SysWordJapanese, SysWordConnector, Example, Constituent, Tag, TaggedItem
register = template.Library()

# ### Custom template tag by SysWord ID ###
# Get Words from SysWord(Same-Japanese-group) ID 
# (1 [SysWord] -> 1 or more [SysWordConnector]s -> (1 [Word] for each [SysWordConnector])) 
@register.filter(name='get_word_cons_by_sysword')
def get_word_cons_by_sysword(value):
    return SysWordConnector.objects.filter(japanese_id=value).select_related('word_id').order_by('word_id__order')

# Get Tags from SysWord(Same-Japanese-group) ID 
# (1 [SysWord] -> 1 or more [SysWordConnector]s -> (1 [Word] for each [SysWordConnector]) -> [Tag]s) 
@register.filter(name='get_tags_by_sysword')
def get_tags_by_sysword(sysword_id):
    id_list = get_word_cons_by_sysword(sysword_id) \
        .values_list('tags__id').distinct()
    return Tag.objects.filter(id__in=id_list).order_by('id')

# Get Examples from SysWord(Same-Japanese-group) ID
# (1 [SysWord] -> 1 or more [SysWordConnector]s -> (1 [Word] for each [SysWordConnector]) -> [Example]s) 
@register.filter(name='get_examples_by_sysword')
def get_examples_by_sysword(value):
    id_list = Constituent.objects.filter(word_id__in=get_word_cons_by_sysword(value)) \
        .values_list('example_id').distinct()
    return Example.objects.filter(id__in=id_list).order_by('id')


# ### Custom template tag by Example ID ###
# Get Tags from Example ID
# (1 [Example] -> 0 or more [Constituent]s -> 1 or more [SysWordConnector]s for each [Constituent] -> [Tag]s) 
@register.filter(name='get_tags_by_example')
def get_tags_by_example(value):
    id_list = Constituent.objects.filter(example_id=value).select_related('word_id') \
        .values_list('word_id__tags__id').distinct()
    return Tag.objects.filter(id__in=id_list).order_by('id')

# Get Constituents from Example ID
@register.filter(name='get_consts_by_example')
def get_consts_by_example(value):
    return Constituent.objects.filter(example_id=value).select_related('word_id').select_related('word_id__word_id').order_by('order')
