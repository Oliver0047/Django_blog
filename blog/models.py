from __future__ import unicode_literals
from DjangoUeditor.models import UEditorField
from django.db import models
 
# Create your models here.
 
class Article(models.Model):
    title = models.CharField(u"博客标题",max_length = 100)        #博客标题
    category = models.CharField(u"博客标签",max_length = 50,blank = True)       #博客标签
    pub_date = models.DateTimeField(u"发布日期",auto_now_add = True,editable=True)       #博客发布日期
    update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)
    content = UEditorField(u"文章正文",height=300,width=1000,default=u'',blank=True,imagePath="uploads/blog/images/",
                           toolbars='besttome',filePath='uploads/blog/files/')  # 博客文章正文
 
    def __unicode__(self):
        return self.title
 
    class Meta:     #按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "博客"
        verbose_name_plural = "我的博客集"

class UserInfo(models.Model):  
  
    username=models.CharField(max_length=64)  
    sex=models.CharField(max_length=64)  
    email=models.CharField(max_length=64) 
    advice=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.username
 
    class Meta: 
        verbose_name = "建议"
        verbose_name_plural = "收集的所有建议"  
