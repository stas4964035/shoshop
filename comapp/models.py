from django.db import models


class Company(models.Model):
    country = models.ForeignKey("mainapp.ListOfCountries",
                                on_delete=models.CASCADE)
    region = models.ForeignKey("mainapp.Regions", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название компании',
                            max_length=128, unique=True)
    image = models.ImageField(upload_to='com_img', blank=True)
    short_desc = models.TextField(verbose_name='краткое описание компании',
                                  max_length=60, blank=True)
    description = models.TextField(verbose_name='описание компании',
                                   blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    @staticmethod
    def get_items():
        return
        Company.objects.filter(is_active=True).order_by('country',
                                                        'regions',
                                                        'name')


def __str__(self):
    return f'{self.name} ({self.country.name})'
