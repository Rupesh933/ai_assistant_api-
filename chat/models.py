import uuid
from django.conf import settings

from django.db import models

class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="conversations"
    )   # which conversation belong to which user
    title = models.CharField(max_length=255, blank=True, default="New Conversation")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Message(models.Model):

    class Role(models.TextChoices):
        USER = 'User', 'user'
        ASSISTANT = "Assistant", "assistant"
        TOOL = "Tool", "tool"

    class Status(models.TextChoices):
        PENDING = "Pending", "pending"
        PROCESSING = "Processing", "processing"
        COMPLETED = "Completed", "completed"
        FAILED = "Failed", "failed"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, default="messages")

    role = models.CharField(max_length=255, choices=Role.choices)
    content = models.CharField(blank=True, default="")
    tool_name = models.CharField(max_length=100, blank=True, default="")
    tool_args = models.JSONField(blank=True, null=True)
    # tool_name or tool_args --> When ai call any backend function, then keep record of it

    status = models.CharField(max_length=16, choices=Status.choices, default=Status.COMPLETED)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.role}]: {self.content[:50]}'