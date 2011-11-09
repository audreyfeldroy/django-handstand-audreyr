from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel

class Profile(BaseModel):
    """
        Profile model
    """
    NO_EMAIL = 'no'
    NEWSLETTER_EMAIL = 'news'
    EMAIL_PREF_CHOICES = (
        (NO_EMAIL, _('No email unless absolutely needed')),
        (NEWSLETTER_EMAIL, _('Send me occasional updates about the site')),
    )

    user = models.OneToOneField(User)
    username = models.CharField(_('Username'), max_length=100, unique=True, null=True, blank=True)
    fullname = models.CharField(_('Full name'), max_length=100, null=True, blank=True)
    email = models.EmailField(_('Email'), null=True, blank=True)
    email_preference = models.CharField(_('Email preference'), max_length=10, choices=EMAIL_PREF_CHOICES, default=NEWSLETTER_EMAIL)

    twitter_username = models.CharField(_('Twitter username'), max_length=100, null=True, blank=True)
    fb_username = models.CharField(_('Facebook username'), max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['fullname',]

    def __unicode__(self):
        return u'%s' % self.username

