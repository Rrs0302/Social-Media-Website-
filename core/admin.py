from django.contrib import admin
from .models import Profile,Post, LikePost,FollowersCount

# Register the models for migration into the database here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
