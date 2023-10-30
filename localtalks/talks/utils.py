import cloudinary.uploader


def upload_image_to_cloudinary(file, default_url):
    if file:
        upload_result = cloudinary.uploader.upload(file)
        secure_url = upload_result['url'].replace("http://", "https://")
        return secure_url, False
    else:
        return default_url, True
