from django.db import models

# todoリストに出現するitem
class Item(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 10)
    memo = models.TextField(maxlength = 30)

# 用途（購入とか）に該当するクラス
class TopItem(Item):
    memo = models.TextField(maxlength = 100)

# 
class ParentItem(Item):
    parent_id = models.IntegerField()

# 
class ChildItem(Item):
    parent_id = models.IntegerField()

