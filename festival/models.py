from django.db import models
from ckeditor.fields import RichTextField
from numberedmodel.models import NumberedModel

class Element(NumberedModel):
    TYPES = (
        ('Photo', 'Photo'),
        ('Video', 'Video'),
        ('Text', 'Text'),
    )
    position = models.PositiveIntegerField(blank=True)
    type = models.CharField(max_length=16, choices=TYPES)
    image = models.ImageField(blank=True)
    youtube_url = models.URLField(blank=True)
    text = RichTextField(blank=True)

    def __str__(self):
        return '{}. {} element'.format(self.position, self.type)

    class Meta:
        ordering = ['position']
