from django.db import models
from django.contrib.auth.models import User

class ResumeAnalysis(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    score = models.FloatField()

    semantic_score = models.FloatField(
        default=0
    )

    recommended_role = models.CharField(
        max_length=100,
        default=""
    )

    matched_skills = models.TextField()

    missing_skills = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.score}"
