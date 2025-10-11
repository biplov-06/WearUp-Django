import os
from pathlib import Path
from django.conf import settings
settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'wearup_db',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    },
    INSTALLED_APPS=['WearUpBack'],
    ROOT_URLCONF='Backend.urls',
)
import django
django.setup()

from WearUpBack.models import UserProfile, ProductImage

def fix_public_ids():
    # Fix UserProfile cover_image and profile_image
    for profile in UserProfile.objects.all():
        if profile.cover_image:
            old_public_id = str(profile.cover_image)
            if old_public_id.startswith('v1/profiles/'):
                new_public_id = old_public_id.replace('v1/profiles/', 'profiles/')
                profile.cover_image = new_public_id
                profile.save(update_fields=['cover_image'])
                print(f"Fixed cover_image for {profile.user.username}: {new_public_id}")
            if profile.profile_image and old_public_id.startswith('v1/profiles/'):
                new_public_id = old_public_id.replace('v1/profiles/', 'profiles/')
                profile.profile_image = new_public_id
                profile.save(update_fields=['profile_image'])
                print(f"Fixed profile_image for {profile.user.username}: {new_public_id}")

    # Fix ProductImage image
    for img in ProductImage.objects.all():
        if img.image:
            old_public_id = str(img.image)
            if old_public_id.startswith('v1/profiles/'):
                new_public_id = old_public_id.replace('v1/profiles/', 'profiles/')
                img.image = new_public_id
                img.save(update_fields=['image'])
                print(f"Fixed profile image: {new_public_id}")
            elif old_public_id.startswith('v1/products/'):
                new_public_id = old_public_id.replace('v1/products/', 'products/')
                img.image = new_public_id
                img.save(update_fields=['image'])
                print(f"Fixed product image: {new_public_id}")

if __name__ == "__main__":
    fix_public_ids()
    print("Public IDs fixed.")
