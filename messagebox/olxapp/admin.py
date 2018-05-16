from django.contrib import admin
from olxapp.models import Conversation, Message, Answer

admin.site.register(Conversation)
admin.site.register(Message)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('title',)
    search_fields = ('title', 'answer')
    date_hierarchy = 'created_at'


admin.site.register(Answer, AnswerAdmin)

