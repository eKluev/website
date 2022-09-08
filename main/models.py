from django.db import models
from typing import Optional


class About(models.Model):
    name = models.CharField('Name', max_length=64)
    description = models.TextField('Description')
    mail = models.CharField('Mail', max_length=64)
    telegram = models.CharField('Telegram', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Project(models.Model):
    name = models.CharField('Project name', max_length=64)
    type = models.CharField('Project type', max_length=64)
    description = models.TextField('Description', blank=True, default='')
    stack = models.TextField('Stack')
    link = models.CharField('Link', max_length=256, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Certificate(models.Model):
    name = models.CharField('Certificate name', max_length=64)
    provider = models.CharField('Provider', max_length=64)
    link = models.CharField('Link', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    @property
    def get_logo(self):
        return f"img/logos/{self.provider.lower()}.png"
