from django.core.management.base import BaseCommand
from WearUpBack.models import UserProfile, ProductImage, Product

class Command(BaseCommand):
    help = 'Fix public_ids for Cloudinary images by removing extensions and /v1/ prefix'

    def handle(self, *args, **options):
        # Fix UserProfile cover_image and profile_image
        for profile in UserProfile.objects.all():
            if profile.cover_image:
                old_public_id = str(profile.cover_image)
                new_public_id = old_public_id
                if old_public_id.startswith('v1/profiles/'):
                    new_public_id = old_public_id.replace('v1/profiles/', 'profiles/')
                if '.' in new_public_id:
                    new_public_id = new_public_id.rsplit('.', 1)[0]
                if new_public_id != old_public_id:
                    profile.cover_image = new_public_id
                    profile.save(update_fields=['cover_image'])
                    self.stdout.write(f"Fixed cover_image for {profile.user.username}: {new_public_id}")
            if profile.profile_image:
                old_public_id = str(profile.profile_image)
                new_public_id = old_public_id
                if old_public_id.startswith('v1/profiles/'):
                    new_public_id = old_public_id.replace('v1/profiles/', 'profiles/')
                if '.' in new_public_id:
                    new_public_id = new_public_id.rsplit('.', 1)[0]
                if new_public_id != old_public_id:
                    profile.profile_image = new_public_id
                    profile.save(update_fields=['profile_image'])
                    self.stdout.write(f"Fixed profile_image for {profile.user.username}: {new_public_id}")



        # Fix ProductImage image
        for img in ProductImage.objects.all():
            if img.image:
                old_public_id = str(img.image)
                new_public_id = old_public_id
                if old_public_id.startswith('v1/profiles/'):
                    new_public_id = old_public_id.replace('v1/profiles/', 'profiles/')
                elif old_public_id.startswith('v1/products/'):
                    new_public_id = old_public_id.replace('v1/products/', 'products/')
                if '.' in new_public_id:
                    new_public_id = new_public_id.rsplit('.', 1)[0]
                if new_public_id != old_public_id:
                    img.image = new_public_id
                    img.save(update_fields=['image'])
                    self.stdout.write(f"Fixed product image: {new_public_id}")

        self.stdout.write(self.style.SUCCESS('Public IDs fixed successfully.'))
