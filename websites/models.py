# websites/models.py

from django.db import models
import os


def upload_location(instance, filename):
    file_path = 'website_image/{}'.format(filename)
    return file_path


class Index(models.Model):
    key_words = models.CharField(max_length=2083, null=True)
    address = models.CharField(max_length=2083, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_click_date = models.DateTimeField(null=True, blank=True)
    click_times = models.IntegerField(default=0, null=True)

    website_image_url = models.CharField(max_length=2083, null=True, blank=True)
    website_image = models.ImageField(upload_to=upload_location, null=True)
    website_index_position_num = models.IntegerField(default=999, null=True)

    def get_fields_dict(self):
        return {field.name: getattr(self, field.name) for field in self._meta.fields}

    def delete(self, *args, **kwargs):
        # Delete the associated website_image file before deleting the Index object
        if self.website_image:
            image_path = os.path.join('media', str(self.website_image))
            if os.path.isfile(image_path):
                os.remove(image_path)

        super(Index, self).delete(*args, **kwargs)

