from django.shortcuts import render
from django.views import generic
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models import Q, Count
from pleethai.models import SysWordJapanese, SysWordThai, Example, Constituent, Tag

PAGENATE_BY = 20

class SearchView(generic.ListView):
    model = SysWordJapanese
    template_name = "search.html"
    
    def get(self, *args, **kwargs):
        # session clear
        self.request.session.clear()
        return super().get(self, *args, **kwargs)

#Search Word
def search_word(request):
    # Get page number
    page = int(request.GET.get("page"))
    if page < 1:
        return
    offset = (page -1) * PAGENATE_BY
    limit = page * PAGENATE_BY

    # Get keyword and tags from request
    keyword = request.GET.get("keyword").strip()
    tags = request.GET.get("tags")

    # Create filter object
    filter_obj = Q()
    if keyword:
        # Search and get japanese id list from SysWordThai
        id_list = SysWordThai.objects.filter( \
            Q(japanese_id__japanese__icontains=keyword) | \
            Q(japanese_id__hiragana__icontains=keyword) | \
            Q(japanese_id__roman__icontains=keyword) | \
            Q(thai__icontains=keyword) | \
            Q(pronunciation_kana__icontains=keyword) | \
            Q(english__icontains=keyword) \
            ).select_related('japanese_id').values_list("japanese_id", flat=True).distinct()
        filter_obj.add(Q(id__in=id_list), Q.AND)

    if tags:
        filter_obj.add(Q(tags__id__in=tags.split('+')), Q.AND)

    # Get word list
    result_list = SysWordJapanese.objects.filter(filter_obj).distinct() \
        .select_related('wordclass_id').order_by("-searchs")[offset:limit]

    # Return html
    htmlstr = ""
    for wordobj in result_list:
        htmlstr += render_to_string('parts/word_item.html', { 'object': wordobj })
    return HttpResponse(htmlstr)

#Search Example
def search_example(request):
    # Get page number
    page = int(request.GET.get("page"))
    if page < 1:
        return
    offset = (page -1) * PAGENATE_BY
    limit = page * PAGENATE_BY

    # Get keyword and tags from request
    keyword = request.GET.get("keyword").strip()
    tags = request.GET.get("tags")

    # Create filter object
    filter_obj = Q()
    if keyword:
        filter_obj.add(Q(japanese__icontains=keyword), Q.OR)
        filter_obj.add(Q(hiragana__icontains=keyword), Q.OR)
        filter_obj.add(Q(roman__icontains=keyword), Q.OR)
        filter_obj.add(Q(thai__icontains=keyword), Q.OR)
        filter_obj.add(Q(pronunciation_kana__icontains=keyword), Q.OR)
        filter_obj.add(Q(english__icontains=keyword), Q.OR)

    if tags:
        id_list = Constituent.objects.filter(word_id__japanese_id__tags__id__in=tags.split('+')) \
            .select_related('word_id').select_related('japanese_id').values_list('example_id', flat= True).distinct()
        filter_obj.add(Q(id__in=id_list), Q.AND)
    
    # Get example list
    result_list = Example.objects.filter(filter_obj).order_by("id")[offset:limit]

    # Return html
    htmlstr = ""
    for exampleobj in result_list:
        htmlstr += render_to_string('parts/example_item.html', { 'object': exampleobj })
    return HttpResponse(htmlstr)

class WordDetailView(generic.DetailView):
    model = SysWordJapanese
    template_name = "word_detail.html"

class ExampleDetailView(generic.DetailView):
    model = Example
    template_name = "example_detail.html"

def tags_all(request):
    tags = Tag.objects.all() \
        .annotate(num_times=Count('pleethai_taggeditem_items')) \
        .order_by('-num_times')
    return render(request, 'tags.html', {'object_list': tags})
