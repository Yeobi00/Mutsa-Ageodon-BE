from django.db import models
from user.models import User
from posts.models import Post

class Order(models.Model):
    OID = models.AutoField(primary_key=True)
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, through='PostOrder')
    

    def __str__(self):
        return f"Order {self.OID} by User {self.user.UID}"


class PostOrder(models.Model):
    post_order_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"PostOrder {self.post_order_id} with Order {self.order.OID} and Post {self.post.PID}"