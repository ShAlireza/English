import os

from django.db import models

from model_utils.models import TimeStampedModel, UUIDModel, SoftDeletableModel
from model_utils.managers import SoftDeletableManager


class Word(UUIDModel, TimeStampedModel, SoftDeletableModel):
    soft_objects = SoftDeletableManager

    def upload_path(self, filename):
        return os.path.join('english', 'words', self.word, filename)

    word = models.CharField(max_length=256)
    synonyms = models.CharField(max_length=512)
    image = models.ImageField(upload_to=upload_path, blank=True, null=True)
    helper_link = models.URLField(max_length=256, blank=True, null=True)


class Sentence(UUIDModel, TimeStampedModel, SoftDeletableModel):
    soft_objects = SoftDeletableManager

    word = models.ForeignKey('english.Word', related_name='sentences',
                             on_delete=models.CASCADE)
    sentence = models.CharField(max_length=1024)


