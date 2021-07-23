from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from main.models import Author


@receiver(pre_save, sender=Author)
def author_pre_save(sender, instance, *args, **kwargs):
    pass
    # print("----------- pre_save")
    # breakpoint()  # c - continue
    # instance.name = instance.name.lower() + ' [author name 2]'
    # instance.email = instance.email + ' [author email 2]'


# @receiver(post_save, sender=Author)
# def author_post_save(sender, instance, created, **kwargs):
#     pass
#     # print("----------- post_save")
#     # breakpoint()
#     if created:
#         # Author.objects.create(user=instance)
#         print('Created')
#     else:
#         print('Exist')
