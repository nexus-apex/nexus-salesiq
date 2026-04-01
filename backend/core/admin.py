from django.contrib import admin
from .models import Visitor, Conversation, CannedResponse

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "page_url", "country", "browser", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "email", "country"]

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ["visitor_name", "agent", "channel", "status", "messages", "created_at"]
    list_filter = ["channel", "status"]
    search_fields = ["visitor_name", "agent"]

@admin.register(CannedResponse)
class CannedResponseAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "shortcut", "usage_count", "active", "created_at"]
    search_fields = ["title", "category", "shortcut"]
