import os
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from pathlib import Path

# Configure Cloudinary from settings
cloudinary.config(
    cloud_name='dbecoviqc',
    api_key='494726599817793',
    api_secret='cTHWALgR68X7UbrydN6V7DtWTaA'
)

BASE_DIR = Path(__file__).parent
MEDIA_DIR = BASE_DIR / 'media'

def upload_folder_to_cloudinary(local_folder):
    """Upload all images in local_folder to Cloudinary with public_id as relative path."""
    folder_path = MEDIA_DIR / local_folder
    if not folder_path.exists():
        print(f"Local folder {local_folder} does not exist.")
        return

    uploaded = 0
    for file_path in folder_path.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp', '.gif']:
            relative_path = os.path.relpath(file_path, MEDIA_DIR).replace('\\', '/')
            public_id = "v1/" + relative_path.rsplit('.', 1)[0]  # remove extension and add v1/
            try:
                # Upload to Cloudinary with public_id
                response = cloudinary.uploader.upload(
                    str(file_path),
                    public_id=public_id,
                    resource_type='image',
                    overwrite=True  # Overwrite if exists
                )
                print(f"Uploaded {relative_path}: {response['secure_url']}")
                uploaded += 1
            except Exception as e:
                print(f"Failed to upload {relative_path}: {e}")
    
    print(f"Uploaded {uploaded} files from {local_folder}.")

if __name__ == "__main__":
    # Upload profiles
    upload_folder_to_cloudinary('profiles')
    
    # Upload products
    upload_folder_to_cloudinary('products')
    
    print("Media upload completed.")
