from django.db import models
from core import models as core_models


class Conversations(core_models.TimeStampedModel):

    participants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversations", related_name="messages", on_delete=models.CASCADE
    )

    def __str___(self):
        return f"{self.user} says : {self.message}"
