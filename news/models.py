from django.db import models
from django.contrib.auth.models import User


class Author (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()


class Category (models.Model):
    name = models.CharField(max_length=30, unique=True,)


class Post (models.Model):
    article = 'ar'
    news = 'nw'

    VIEW = [
        (article, 'Статья'),
        (news, 'Новость')
        ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    view = models.CharField(max_length=2, choices=VIEW, default=article)
    create_time = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    heading = models.CharField(max_length=255)
    text_post = models.TextField()
    rating_post = models.IntegerField(default=0)

    def like(self):
        self.rating_post = + 1
        self.save()

    def dislike(self):
        self.rating_post = - 1
        self.save()

    def preview(self):
        size = 124 if len(self.text_post) > 124 else len(self.text_post)
        return self.text_post[:size] + "..."


class PostCategory (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment = + 1
        self.save()

    def dislike(self):
        self.rating_comment = - 1
        self.save()