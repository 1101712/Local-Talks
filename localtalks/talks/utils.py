import cloudinary
import cloudinary.uploader


def upload_image_to_cloudinary(file, default_url):
    try:
        if file:
            upload_result = cloudinary.uploader.upload(file)
            secure_url = upload_result['url'].replace("http://", "https://")
            return secure_url, False
        else:
            return default_url, True
    except cloudinary.exceptions.Error as e:
        print(f"An error occurred while uploading to Cloudinary: {e}")
        return default_url, True
