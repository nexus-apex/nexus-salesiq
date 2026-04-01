from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Visitor, Conversation, CannedResponse
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusSalesIQ with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexussalesiq.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Visitor.objects.count() == 0:
            for i in range(10):
                Visitor.objects.create(
                    name=f"Sample Visitor {i+1}",
                    email=f"demo{i+1}@example.com",
                    page_url=f"https://example.com/{i+1}",
                    country=f"Sample {i+1}",
                    browser=f"Sample {i+1}",
                    visits=random.randint(1, 100),
                    status=random.choice(["online", "offline", "away"]),
                    last_seen=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Visitor records created'))

        if Conversation.objects.count() == 0:
            for i in range(10):
                Conversation.objects.create(
                    visitor_name=f"Sample Conversation {i+1}",
                    agent=f"Sample {i+1}",
                    channel=random.choice(["website", "whatsapp", "facebook", "email"]),
                    status=random.choice(["open", "active", "waiting", "closed"]),
                    messages=random.randint(1, 100),
                    started_at=date.today() - timedelta(days=random.randint(0, 90)),
                    rating=random.randint(1, 100),
                )
            self.stdout.write(self.style.SUCCESS('10 Conversation records created'))

        if CannedResponse.objects.count() == 0:
            for i in range(10):
                CannedResponse.objects.create(
                    title=f"Sample CannedResponse {i+1}",
                    category=f"Sample {i+1}",
                    shortcut=f"Sample {i+1}",
                    content=f"Sample content for record {i+1}",
                    usage_count=random.randint(1, 100),
                    active=random.choice([True, False]),
                )
            self.stdout.write(self.style.SUCCESS('10 CannedResponse records created'))
