from django.db import models
from django.utils.text import slugify
class Post(models.Model):
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    price = models.CharField(max_length=50)
    daraja = models.CharField(
        max_length=50,
        choices=[
            ('intern', 'Intern'),
            ('junior', 'Junior'),
            ('middle', 'Middle'),
            ('senior', 'Senior'),
            ('head', 'Head'),
        ],
        default='middle'
    )
    region = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    talablar = models.TextField(blank=True, null=True)
    shartlar = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            n = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.title} at {self.company}"
