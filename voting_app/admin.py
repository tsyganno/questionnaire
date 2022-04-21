from django.contrib import admin
from .models import Vote, QuestionType, ImageQuestion, AudioQuestion, VideoQuestion, Choice


class VoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'content')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)


admin.site.register(Vote, VoteAdmin)
admin.site.register(QuestionType)
admin.site.register(ImageQuestion)
admin.site.register(AudioQuestion)
admin.site.register(VideoQuestion)
admin.site.register(Choice)

