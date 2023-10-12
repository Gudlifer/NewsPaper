from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.FloatField(default=0.0)

    def update_rating(self):
        postRat = self.post_set.all().aggregate(postRating=Sum("rating"))
        pRat = 0
        pRat += postRat.get("postRating")

        comRat = self.authorUser.comment_set.all().aggregate(commentRating=Sum("rating"))
        cRat = 0
        cRat += comRat.get("commentRating")

        self.ratingAuthor = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return self.authorUser.username


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True,)

    def __str__(self):
        return self.name


class Likeable(models.Model):
    rating = models.FloatField(default=0.0)

    def like(self):
        self.rating += 1.0
        self.save()

    def dislike(self):
        self.rating -= 1.0
        self.save()

    class Meta:
        abstract = True


class Post(Likeable):
    News = "NW"
    Article = "AR"
    CATEGORY_CHOICES = [(Article, "Статья"),
                        (News, "Новость"),
                        ]

    choice = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=Article)
    time_create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField(default=0.0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through="PostCategory")

    def __str__(self):
        return f'{self.title}:{self.text},{self.time_create}'

    def preview(self):
        return f'{self.text[0:123]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(Likeable):
    text_com = models.CharField(max_length=255)
    time_com = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
