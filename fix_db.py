import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
django.setup()

from WearUpBack.models import ProductImage, UserProfile

print("Updating ProductImage fields...")
for img in ProductImage.objects.all():
    if img.image:
        current = str(img.image)
        if not current.startswith('v1/'):
            img.image = 'v1/' + current
            img.save()
            print(f"Updated ProductImage {img.id}: {img.image}")

print("Updating UserProfile fields...")
for profile in UserProfile.objects.all():
    if profile.profile_image:
        current = str(profile.profile_image)
        if not current.startswith('v1/'):
            profile.profile_image = 'v1/' + current
            profile.save()
            print(f"Updated profile_image for user {profile.user.username}: {profile.profile_image}")
    if profile.cover_image:
        current = str(profile.cover_image)
        if not current.startswith('v1/'):
            profile.cover_image = 'v1/' + current
            profile.save()
            print(f"Updated cover_image for user {profile.user.username}: {profile.cover_image}")

print("All updates completed.")
