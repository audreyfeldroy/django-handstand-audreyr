from django.conf.urls.defaults import *
from profiles.models import Profile
from profiles.views import ProfileListView, ProfileDetailView, profile_edit

urlpatterns = patterns('profiles.views',
    url(regex=r'^edit/$',
        view=profile_edit,
        name='profile_edit',
    ),
    url(regex=r'^$',
        view=ProfileListView.as_view(),
        name='profile_list',
    ),
    url(regex=r'^(?P<username>[-\w]+)/$',
        view=ProfileDetailView.as_view(),
        name='profile_detail',
    ),
)
