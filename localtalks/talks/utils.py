import cloudinary.uploader


def upload_image_to_cloudinary(file, default_url):
    if file:
        upload_result = cloudinary.uploader.upload(file)
        return upload_result['url'], False
    else:
        return default_url, True
