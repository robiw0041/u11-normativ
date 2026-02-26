from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class BaseQuerySet(models.QuerySet):
    def delete(self):
        return super().update(is_deleted=True)


class DeletedManager(models.Manager):
    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db).filter(is_deleted=False)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = DeletedManager()
    all_objects = models.Manager()

    def __str__(self):
        return self.title