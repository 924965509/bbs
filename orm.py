import os
import sys
import django
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbs.settings")
    django.setup()

    from blog import models
    from django.db.models import Count

    user = models.UserInfo.objects.filter(username="cjkk").first()
    # blog = user.blog
    # user = models.UserInfo.objects.filter(username="cjkk").first()
    # blog = user.blog
    # ret = models.Category.objects.filter(blog=blog)
    # # ret = ret[0].article_set.all()
    # ret.annotate(a=Count("article"))


    ret = models.Article.objects.filter(user=user).extra(
            select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
        ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")
    print(ret)


