from django.db import models
from django_extensions.db.fields import AutoSlugField, ShortUUIDField, RandomCharField
from django_extensions.db.models import TimeStampedModel
from cloudinary.models import CloudinaryField
import os

def entry_image_upload_path(instance, filename):
    # instance.entry is the related PhotoEntry instance
    entry_id = instance.entry.id if instance.entry else 'unassigned'
    filename = os.path.basename(filename)
    return f'/shutter9ja/uploads/images/{entry_id}/'


# Create your models here.
class Competition(TimeStampedModel):
    id = ShortUUIDField(primary_key=True, unique=True)
    edition = models.CharField(max_length=255)
    reg_due_date = models.DateTimeField()
    concluded = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from="edition", unique=True)


class Entry(TimeStampedModel):
    id = RandomCharField(primary_key=True, unique=True, include_alpha=False, length=8)
    EXPERIENCE_LEVELS = (
        ("Beginer", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Professional", "Professional"),
    )

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    age = models.IntegerField()
    Location = models.TextField()
    theme_of_entry = models.CharField(max_length=255)
    description = models.TextField()
    photography_experience = models.CharField(max_length=255, choices=EXPERIENCE_LEVELS)
    profile_picture = CloudinaryField('Profile Picture')
    instagram_username = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)
    vote_count = models.IntegerField(default=0)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

    # class Meta:
    #     plural_label = "Entries"



class EntryImage(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="images")
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.entry.full_name}"
