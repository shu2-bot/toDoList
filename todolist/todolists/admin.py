from django.contrib import admin

from todolists.models import TopItem

# 以下を追記することでadmin管理画面に表示される
admin.site.register(TopItem)
