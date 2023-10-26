from django.contrib.sitemaps import Sitemap
from cuk.models import Paper

class PaperSitemap(Sitemap):
    changefreq='daily'
    priority=0.5
    def items(self):
        return Paper.objects.all()