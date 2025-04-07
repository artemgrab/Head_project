from picamzero import Camera
from integration import on_camera_image


class BenderCamera:
    def __init__(self):
        self.camera = Camera()

    def take_picture(self, filename="image.jpg"):
        self.camera.take_photo(filename)
        on_camera_image(filename)
