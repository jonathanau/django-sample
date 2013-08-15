from django.contrib import admin

from southtut.models import Knight

class KnightAdmin(admin.ModelAdmin):
  list_display = (
      'name',
      'of_the_round_table',
      'dances_whenever_able',
      'shrubberies',
      )

admin.site.register(Knight, KnightAdmin)
