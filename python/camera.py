from picamzero import Camera


class BenderCamera:
    def __init__(self):
        self.camera = Camera()

    def take_picture(self, filename="image.jpg"):
        self.camera.take_photo(filename)
