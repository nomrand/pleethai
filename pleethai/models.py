from django.db import models
from taggit.models import TagBase, GenericTaggedItemBase
from taggit.managers import TaggableManager
from taggit.utils import _parse_tags

class Tag(TagBase):
    thai = models.CharField(max_length=100)
    class Meta:
        ordering = ['id']

class TaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(Tag, related_name="%(app_label)s_%(class)s_items", on_delete=models.CASCADE)
    class Meta:
        index_together = [["content_type", "object_id"]]
        unique_together = [["content_type", "object_id", "tag"]]

class Word (models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    japanese = models.CharField(max_length=127, null=False, blank=False)
    hiragana =  models.CharField(max_length=127, null=False, blank=False)
    roman = models.CharField(max_length=127, null=True, blank=True)
    thai =  models.CharField(max_length=127, null=False, blank=False)
    pronunciation_symbol = models.CharField(max_length=127, null=True, blank=True)
    pronunciation_kana = models.CharField(max_length=127, null=True, blank=True)
    order = models.PositiveSmallIntegerField(default=1)
    english = models.CharField(max_length=127, null=True, blank=True)
    search = models.BigIntegerField(default=0)
    wordclass_id = models.ForeignKey("WordClass", on_delete=models.PROTECT)
    tags = models.CharField(max_length=511, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("japanese", "hiragana", "thai")

    def __str__(self):
        return str(self.id) + " [" + self.japanese + ", " + self.hiragana + ", " + self.thai+ "]"

class SysWordJapanese (models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    japanese = models.CharField(max_length=127, null=False, blank=False)
    hiragana =  models.CharField(max_length=127, null=False, blank=False)
    roman = models.CharField(max_length=127, null=True, blank=True)
    search = models.BigIntegerField(default=0)
    wordclass_id = models.ForeignKey("WordClass", on_delete=models.PROTECT)

    class Meta:
        unique_together = ("japanese", "hiragana")

    def __str__(self):
        return str(self.id) + " [" + self.japanese + ", " + self.hiragana + "]"

    @classmethod
    def create(self, word: Word):
        if word == None:
            return None
        return self( \
            id = word.id, \
            japanese = word.japanese, \
            hiragana = word.hiragana, \
            roman = word.roman, \
            search = word.search, \
            wordclass_id = word.wordclass_id, \
        )

class SysWordConnector (models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    japanese_id = models.ForeignKey("SysWordJapanese", on_delete=models.PROTECT)
    word_id = models.ForeignKey("Word", on_delete=models.PROTECT)
    tags = TaggableManager(through=TaggedItem, blank=True)

    @classmethod
    def create(self, word: Word, sys_japanese):
        if word == None or sys_japanese == None:
            return None
        # Search Japanese_ID in Sys_Word_Japanese table
        japanese = next((item for item in sys_japanese \
            if item.japanese == word.japanese and item.hiragana == word.hiragana), None)
        if japanese == None:
            return None

        instance = self( \
            id = word.id, \
            japanese_id = japanese, \
            word_id = word, \
        )
        instance.tags.add(*_parse_tags(word.tags))
        return instance

class WordClass (models.Model): 
    id = models.PositiveSmallIntegerField(primary_key=True)
    thai = models.CharField(max_length=31, null=True, blank=True)
    japanese = models.CharField(max_length=31, null=True, blank=True)
    slug = models.SlugField(max_length=31, null=True, blank=True)

    def __str__(self):
        return str(self.id) + " [" + self.slug + ", " + self.japanese + ", " + self.thai + "]"

class Example (models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    japanese = models.CharField(max_length=511, null=False, blank=False)
    hiragana =  models.CharField(max_length=511, null=True, blank=True)
    roman =  models.CharField(max_length=511, null=True, blank=True)
    thai =  models.CharField(max_length=511, null=True, blank=True)
    pronunciation_symbol = models.CharField(max_length=511, null=True, blank=True)
    pronunciation_kana = models.CharField(max_length=511, null=True, blank=True)
    english = models.CharField(max_length=511, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " [" + self.japanese + "]"

class Constituent (models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    example_id = models.ForeignKey("Example", on_delete=models.PROTECT)
    word_id = models.ForeignKey("SysWordConnector", on_delete=models.PROTECT)
    order = models.PositiveSmallIntegerField(null=False)

    class Meta:
        unique_together = ("example_id", "word_id", "order")

    def __str__(self):
        return str(self.example_id) + ", " + str(self.word_id) + ", " + str(self.order)
