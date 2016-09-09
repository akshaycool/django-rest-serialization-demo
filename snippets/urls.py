# from django.conf.urls import url,include
# from . import views
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets.views import SnippetViewSet,UserViewSet ,api_root
# from rest_framework import renderers
# from rest_framework.routers import DefaultRouter


# # snippet_list=SnippetViewSet.as_view({
# #     'get':'list',
# #     'post':'create'
# # })

# # snippet_detail=SnippetViewSet.as_view({
# #     'get':'retrieve',
# #     'put':'update',
# #     'patch':'partial_update',
# #     'delete':'destroy'
# # })

# # snippet_highlight=SnippetViewSet.as_view({
# #     'get':'retrieve'
# # },renderers_classes=[renderers.StaticHTMLRenderer])

# # user_list=UserViewSet.as_view({
# #     'get':'list'
# # })

# # user_detail=UserViewSet.as_view({
# #     'get':'retrieve'
# # })


# """ DefaultRouter creates the api root automatically 
#     And also explicitly setting the api is not needed
# """
# router=DefaultRouter()
# router.register(r'snippets',views.SnippetViewSet)
# router.register(r'users',views.UserViewSet)

# #API endpoints
# # urlpatterns=format_suffix_patterns([
# #     #url(r'^$',api_root),
# #     url(r'^$',include(router.urls)),
# #     url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
# #     # url(r'^snippets/$', snippet_list,name='snippets-list'),
# #     # url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail,name='snippet-detail'),
# #     # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',snippet_highlight,name='snippet-highlight'),
# #     # url(r'^users/$',user_list,name='user-list'),
# #     # url(r'^users/(?P<pk>[0-9]+)/$', user_detail,name='user-detail'),
# # ])

# urlpatterns=[
#     url(r'^$',include(router.urls)),
#     url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
# ]
# #urlpatterns=format_suffix_patterns(urlpatterns)

# #Login and Logout views for browsable API
# # urlpatterns+=[
# #     url(r'^api-auth/',include('rest_framework.urls',namespace='rest_franework')),
# # ]