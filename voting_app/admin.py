from django.contrib import admin
from .models import Vote, Question, Choice, TypeQuestion


class VoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'content')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)


admin.site.register(Vote, VoteAdmin)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(TypeQuestion)
