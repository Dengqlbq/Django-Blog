from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间')
    last_modified_time = models.DateTimeField('修改时间')
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=100, blank=True, null=True,help_text="可选，如若为空将摘取正文的前100个字符")

    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)

    category = models.ForeignKey('Category', verbose_name='分类',null=True,on_delete=models.SET_NULL)
    archives = models.ForeignKey('Archives',verbose_name='档案日期',null=True,on_delete=models.SET_NULL)
    tag = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'article_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']


class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间')
    last_modified_time = models.DateTimeField('修改时间')

    def __str__(self):
        return self.name
class Archives(models.Model):
    name = models.CharField('档案日期', max_length=20)
    created_time = models.DateTimeField('创建时间',auto_now=True)
    last_modified_time = models.DateTimeField('修改时间',auto_now=True)

    def __str__(self):
        return self.name

class BlogComment(models.Model):
    user_name = models.CharField('评论者名字', max_length=100)
    body = models.TextField('评论内容')
    created_time = models.DateTimeField('评论发表时间', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]

class Tag(models.Model):
    name = models.CharField('标签名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name