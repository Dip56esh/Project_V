from directs.views import inbox, Directs, SendDirect, UserSearch, NewConversation, map_view,CallView
from django.urls import path



urlpatterns = [
    path('', inbox, name="message"),
    path('direct/<username>', Directs, name="directs"),
    path('send/', SendDirect, name="send-directs"),
    path('search/', UserSearch, name="search-users"),
    path('new/<username>', NewConversation, name="conversation"),
    path('map/', map_view, name='map_view'),
    path('call/<username>', CallView, name="call"),
  
    
]

