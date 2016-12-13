from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from numberedmodel.models import NumberedModel

class Element(NumberedModel):
    TYPES = (
        ('photo', 'Foto'),
        ('video', 'Video'),
        ('text', 'Tekst'),
        ('header', 'Header'),
        ('tickets', 'Tickets'),
    )
    position = models.PositiveIntegerField('positie', blank=True)
    type = models.CharField(help_text='Kies hier het type element. Een foto-element lat een foto zien, een video element een video, etc.', max_length=16, choices=TYPES)
    image = models.ImageField('afbeelding', blank=True)
    video = EmbedVideoField(help_text="Plak hier een YouTube of Vimeo link", blank=True)
    text = RichTextField('tekst', blank=True)

    def get_absolute_url(self):
        return '/'

    def __str__(self):
        return '{}. {} element'.format(self.position, self.get_type_display())

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'elementen'
