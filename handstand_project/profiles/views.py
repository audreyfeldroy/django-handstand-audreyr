from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _
from django.views.generic import DetailView, ListView, UpdateView

from social_auth.signals import pre_update
from social_auth.backends.twitter import TwitterBackend
from social_auth.backends.facebook import FacebookBackend

from profiles.models import Profile
from profiles.forms import ProfileForm

def user_update(profile_instance, new_username, new_fullname):
    if not profile_instance.username:
        profile_instance.username = slugify(new_username)
    if not profile_instance.fullname:
        profile_instance.fullname = new_fullname
    profile_instance.save()
    return True

def twitter_user_update(sender, user, response, details, **kwargs):
    profile_instance, created = Profile.objects.get_or_create(user=user)
    profile_instance.twitter_username = details['username']
    user_update(profile_instance, details['username'], details['fullname'])
    return True

pre_update.connect(twitter_user_update, sender=TwitterBackend)

def facebook_user_update(sender, user, response, details, **kwargs):
    profile_instance, created = Profile.objects.get_or_create(user=user)
    profile_instance.fb_username = details['username']
    user_update(profile_instance, details['username'], details['fullname'])
    return True

pre_update.connect(facebook_user_update, sender=FacebookBackend)


class ProfileListView(ListView):
    context_object_name = 'profile_list'
    template_name = 'profiles/profile_list.html'
    queryset = Profile.objects.order_by('-modified')

class ProfileDetailView(DetailView):
    """ Shows the profile page for a user. """

    context_object_name = 'profile'
    model = Profile
    template_name = 'profiles/profile_detail.html'
    slug_field = 'username'

    def get_object(self):
        username = self.kwargs.get('username', None)
        if username is not None:
            queryset = self.get_queryset().filter(username=username)

            try:
                obj = queryset.get()
            except ObjectDoesNotExist:
                raise Http404(_(u"No profile found matching the query"))

            return obj

@login_required
def profile_edit(request, template_name="profiles/profile_edit.html"):

    profile = request.user.get_profile()
    form = ProfileForm(request.POST or None, instance=profile)

    if form.is_valid():
        form.save()
#        msg = 'Profile edited'
#        messages.add_message(request, messages.INFO, msg)
        return HttpResponseRedirect(reverse("profile_detail", kwargs={"username":profile.username }))

    return render(request, template_name,
        {
            "profile": profile,
            "form": form,
        })
