from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from . import views

router = DefaultRouter()
router.register(r'viewsets/posts', views.PostViewSet)
router.register(r'viewsets/groups', views.GroupViewSet)

comment_router = routers.NestedDefaultRouter(
    router,
    r'viewsets/posts',
    lookup='post'
)
comment_router.register(
    r'comments',
    views.CommentViewSet,
    basename='post-comments'
)

urlpatterns = [
    # api_view decorator
    path('', include(router.urls)),
    path('view_func/posts/', views.post_list_create),
    path('view_func/posts/<int:post_id>/', views.post_update_delete),
    path('view_func/groups/', views.group_list_create),
    path('view_func/groups/<int:group_id>/', views.group_update_delete),
    path('view_func/posts/<int:post_id>/comments/', views.comment_list_create),
    path(
        'view_func/posts/<int:post_id>/comments/<int:comment_id>/',
        views.comment_update_delete
    ),

    # APIView classes
    path('api_class/posts/', views.PostView.as_view()),
    path('api_class/posts/<int:post_id>/', views.PostDetailView.as_view()),
    path('api_class/groups/', views.GroupView.as_view()),
    path('api_class/groups/<int:group_id>/', views.GroupDetailView.as_view()),
    path(
        'api_class/posts/<int:post_id>/comments/',
        views.CommentView.as_view()
    ),
    path(
        'api_class/posts/<int:post_id>/comments/<int:comment_id>/',
        views.CommentDetailView.as_view()
    ),

    # Generic View classes
    path('api_generic_class/posts/', views.PostGenericView.as_view()),
    path(
        'api_generic_class/posts/<int:post_id>/',
        views.PostDetailGenericView.as_view()
    ),
    path('api_generic_class/groups/', views.GroupGenericView.as_view()),
    path(
        'api_generic_class/groups/<int:group_id>/',
        views.GroupDetailGenericView.as_view()
    ),
    path(
        'api_generic_class/posts/<int:post_id>/comments/',
        views.CommentGenericView.as_view()
    ),
    path(
        'api_generic_class/posts/<int:post_id>/comments/<int:comment_id>/',
        views.CommentDetailGenericView.as_view()
    ),

    # Viewsets
    path('', include(router.urls)),
    path('', include(comment_router.urls))
]
