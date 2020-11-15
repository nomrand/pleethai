from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.conf.urls import url
from django.contrib import messages
from django.shortcuts import redirect
from pleethai.models import Word, SysWordJapanese, SysWordConnector, WordClass, Example, Constituent, Tag, TaggedItem
from pleethai.common import Common
from django.db import models

class WordResource(resources.ModelResource):

    class Meta:
        model = Word

class WordClassResource(resources.ModelResource):

    class Meta:
        model = WordClass

class ExampleResource(resources.ModelResource):

    class Meta:
        model = Example

class ConstituentResource(resources.ModelResource):

    class Meta:
        model = Constituent

class TagResource(resources.ModelResource):

    class Meta:
        model = Tag

class WordAdmin(ImportExportModelAdmin):
    resource_class = WordResource
    # Add "UPDATE SYS_WORD TABLES" button
    change_list_template = "admin/pleethai/Word/change_list.html"

    # URL for update system tables
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url(r'^updatesystables/$', self.admin_site.admin_view(self.update_system_tables)),
        ]
        return my_urls + urls

    # Condition of search
    def exist_japanese(self, sys_ja: SysWordJapanese, word: Word) -> bool:
        if not isinstance(sys_ja, SysWordJapanese) or not isinstance(word, Word):
            return False
        return sys_ja.japanese == word.japanese and sys_ja.hiragana == word.hiragana

    def delete_all(self, model: models.Model):
        while model.objects.count():
            ids = model.objects.values_list('pk', flat=True)[:100]
            model.objects.filter(pk__in = ids).delete()
            
    # Create SysWordJapanse table and SysWordConnector table from Word table
    def update_system_tables(self, request):
        all_words = Word.objects.all()
        sys_japanese = []
        sys_word_con = []
        temp_constituent = []
        try:
            for word in all_words:
                # Add a Word record (japanese & hiragana unique) to SysWordJapanese table
                if not Common.contains(sys_japanese, word, self.exist_japanese):
                    sys_japanese.append(SysWordJapanese.create(word))
                # Add a Word record to SysWordConnector table
                tempConnect = SysWordConnector.create(word, sys_japanese)
                if tempConnect != None:
                    sys_word_con.append(tempConnect)
            # delete and recreate
            for con_dict in Constituent.objects.values():
                temp_constituent.append(Constituent(**con_dict))
            self.delete_all(Constituent)
            self.delete_all(SysWordConnector)
            self.delete_all(SysWordJapanese)
            SysWordJapanese.objects.bulk_create(sys_japanese)
            SysWordConnector.objects.bulk_create(sys_word_con)
            Constituent.objects.bulk_create(temp_constituent)
            messages.info(request, "Succeeded to update system tables")
        except Exception as e:
            messages.error(request, "Failed to update system tables")
            messages.error(request, str(e))
        return redirect(request.META['HTTP_REFERER'])

class WordClassAdmin(ImportExportModelAdmin):
    resource_class = WordClassResource

class ExampleAdmin(ImportExportModelAdmin):
    resource_class = ExampleResource

class ConstituentAdmin(ImportExportModelAdmin):
    resource_class = ConstituentResource

class TaggedItemInline(admin.StackedInline):
    model = TaggedItem
    
class TagAdmin(ImportExportModelAdmin):
    resource_class = TagResource
    inlines = [TaggedItemInline]

admin.site.register(Word, WordAdmin)
admin.site.register(SysWordJapanese)
admin.site.register(SysWordConnector)
admin.site.register(WordClass,WordClassAdmin)
admin.site.register(Example, ExampleAdmin)
admin.site.register(Constituent, ConstituentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(TaggedItem)

