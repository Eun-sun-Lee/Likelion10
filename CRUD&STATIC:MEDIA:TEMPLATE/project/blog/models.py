from django.db import models

class Blog(models.Model):
 #   author = models.ForeignKey('auth.User',max_length=40)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,max_length=40)
    title=models.CharField(max_length=20)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True) #처음 객체를 생성할때 데이트 값 업데이트, 수정할때는 업데이트 X-> auto_add
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(default="")
    image=models.ImageField(upload_to="blog/",blank="True",null="True")
    
  #  hits=models.IntegerField(default=0)
    #최소 5개 추가, admin 사이트에서 해보기
    def __str__(self):
        return self.title #models에서 제공, 사용자 입맛에 맞게 customizing
    def summary(self):
        return self.content[:100]


