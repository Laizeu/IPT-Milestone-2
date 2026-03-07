from django.urls import path
from .views import (
    UserListView, UserCreateView, UserRetrieveUpdateDestroy,
    PostListCreate, PostRetrieveUpdateDestroy, LikePostView,
    PostCommentCreate, PostAllCommentsList,
    CommentRetrieveUpdateDestroy, LikeCommentView,
    UserPostCommentsList, UserPostCommentDetail, UserAllCommentsList,
    PostCommentDetail, UserPostList, UserSpecificPost,
    FollowUserView, UserFollowersView, AllUsersFollowersView,
    NewsFeedView
)

urlpatterns = [
    # -------------------- USER ENDPOINTS --------------------
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),

    # -------------------- POST ENDPOINTS --------------------
    path('', PostListCreate.as_view(), name='post-list-create'),
    path('<int:pk>/like/', LikePostView.as_view(), name='post-like'),

    # -------------------- COMMENT ENDPOINTS --------------------
    path('<int:pk>/comment/', PostCommentCreate.as_view(), name='post-comment-create'),
    path('<int:pk>/comments/', PostAllCommentsList.as_view(), name='post-comments-list'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroy.as_view(), name='comment-retrieve-update-destroy'),
    path('comments/<int:pk>/like/', LikeCommentView.as_view(), name='comment-like'),

    # -------------------- COMMENT TRACKING ENDPOINTS --------------------
    path('<int:post_id>/comments/<int:comment_id>/', PostCommentDetail.as_view(), name='post-comment-detail'),

    # -------------------- USER COMMENT TRACKING --------------------
    path('<int:post_id>/users/<int:user_id>/comments/', UserPostCommentsList.as_view(), name='user-post-comments-list'),
    path('<int:post_id>/users/<int:user_id>/comments/<int:comment_id>/', UserPostCommentDetail.as_view(), name='user-post-comment-detail'),
    path('users/<int:user_id>/comments/', UserAllCommentsList.as_view(), name='user-all-comments-list'),

    # -------------------- USER POST TRACKING --------------------
    path('users/<int:user_id>/posts/', UserPostList.as_view(), name='user-post-list'),
    path('<int:post_id>/users/<int:user_id>/', UserSpecificPost.as_view(), name='user-specific-post'),

    # -------------------- FOLLOW USER ENDPOINTS --------------------
    path('users/<int:user_id>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('users/<int:user_id>/followers/', UserFollowersView.as_view(), name='user-followers'),
    path('users/followers/', AllUsersFollowersView.as_view(), name='all-users-followers'),

    # -------------------- NEWS FEED ENDPOINT --------------------
    path('feed/', NewsFeedView.as_view(), name='news-feed'),

    # -------------------- POST DETAIL ENDPOINT --------------------
    # IMPORTANT: generic pk route must be last
    path('<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post-retrieve-update-destroy'),
]
