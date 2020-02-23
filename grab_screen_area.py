import d3dshot
import time
from PIL import Image
import numpy as np


class Camera:
    def __init__(self):
        print('init')
        self.grabber = d3dshot.create('numpy')

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        del self.grabber

    def grab_to_numpy(self, corners):
        data = self.grabber.screenshot(region=corners)
        return data

    @staticmethod
    def save_numpy_img(data, name=None):
        if name is None:
            name = str(time.time()) + '.png'
        Image.fromarray(data).save(name)
        return

    @staticmethod
    def grab_vital_pixels(data, new_dimensions: tuple):
        # will grab pixels with corners being the start and end points
        # new_dimensions is (x, y)
        new_pic = []
        for y in range(new_dimensions[1]):
            y_cord = y * data.shape[0] // (new_dimensions[1] - 1)
            x_row = []
            for x in range(new_dimensions[0]):
                x_cord = x * data.shape[1] // (new_dimensions[0] - 1)
                if x_cord >= data.shape[1]:
                    x_cord = data.shape[1] - 1
                if y_cord >= data.shape[0]:
                    y_cord = data.shape[0] - 1
                x_row.append(data[y_cord][x_cord])
            new_pic.append(x_row)
        return np.asarray(new_pic)


def test_image():
    with Camera() as c:
        data = c.grab_to_numpy((500, 200, 1000, 500))
        c.save_numpy_img(c.grab_vital_pixels(data, (50, 30)), 'with_test.png')


def main():
    test_image()
    exit()
    time.sleep(1)
    pic = Camera()
    data = pic.grab_to_numpy((0, 0, 1500, 800))
    print(data)
    pic.save_numpy_img(data, name='captured.png')
    smaller = pic.grab_vital_pixels(data, (150, 80))
    print('smalled')
    pic.save_numpy_img(smaller, name='smaller.png')


if __name__ == '__main__':
    main()
