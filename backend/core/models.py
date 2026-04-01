from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    page_url = models.URLField(blank=True, default="")
    country = models.CharField(max_length=255, blank=True, default="")
    browser = models.CharField(max_length=255, blank=True, default="")
    visits = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("online", "Online"), ("offline", "Offline"), ("away", "Away")], default="online")
    last_seen = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Conversation(models.Model):
    visitor_name = models.CharField(max_length=255)
    agent = models.CharField(max_length=255, blank=True, default="")
    channel = models.CharField(max_length=50, choices=[("website", "Website"), ("whatsapp", "WhatsApp"), ("facebook", "Facebook"), ("email", "Email")], default="website")
    status = models.CharField(max_length=50, choices=[("open", "Open"), ("active", "Active"), ("waiting", "Waiting"), ("closed", "Closed")], default="open")
    messages = models.IntegerField(default=0)
    started_at = models.DateField(null=True, blank=True)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.visitor_name

class CannedResponse(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, default="")
    shortcut = models.CharField(max_length=255, blank=True, default="")
    content = models.TextField(blank=True, default="")
    usage_count = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
