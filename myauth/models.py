from django.contrib import admin
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse


class BlogUser(AbstractUser):
    #需要去settings里面指定使用的用户模型
    nickname = models.CharField('昵称', max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    # objects = BlogUserManager()
    # 下面的方法应该是获取详情的链接，后补
    # def get_absolute_url(self):
    #     return reverse('blog:author_detail', kwargs={'author_name': self.username})

    def __str__(self):
        return self.email

    # def get_full_url(self):
    #     site = Site.objects.get_current().domain
    #     url = "https://{site}{path}".format(site=site, path=self.get_absolute_url())
    #     return url

