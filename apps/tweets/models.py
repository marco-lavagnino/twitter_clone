from django.db import models


class Tweet(models.Model):
    name = models.CharField("Tweet's author", max_length=50)
    content = models.CharField("Tweet's content", max_length=50)
    timestamp = models.DateTimeField(
        "Tweet's creation timestamp",
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return f"@{self.name} at {self.timestamp}"
