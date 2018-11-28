from apps.users import urls as users_urls
from apps.community import urls as community_urls


urlpatterns = []
urlpatterns += users_urls.urlpatterns
urlpatterns += community_urls.urlpatterns
