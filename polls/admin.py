from django.contrib import admin
from polls.models import PollQuestion


@admin.register(PollQuestion)
class PollQuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'option_one', 'option_two', 'option_three', 'option_four',
                    'option_one_votes', 'option_two_votes', 'option_three_votes', 'option_four_votes']


