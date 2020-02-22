import d3dshot
import time
from PIL import Image
import numpy as np


class Camera:
    def __init__(self):
        self.grabber = d3dshot.create('numpy')

    def __enter__(self):
        self.__init__()
        return self.grabber

    def __exit__(self, exc_type, exc_val, exc_tb):
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
    now = time.time()
    d = d3dshot.create(capture_output='numpy')
    num_test = 1
    for a in range(num_test):
        # print(a)
        # a += 1
        d.screenshot()
    print(num_test / (time.time() - now), 'fps')


def shot_part_to_numpy(left, top, right, bottom):
    d = d3dshot.create(capture_output='numpy')
    data = d.screenshot()
    del d
    print(data)
    Image.fromarray(data).save('converted.png')
    pass


def main():
    time.sleep(1)
    pic = Camera()
    data = pic.grab_to_numpy((0, 0, 1500, 800))
    print(data)
    pic.save_numpy_img(data, name='captured.png')
    smaller = pic.grab_vital_pixels(data, (150, 80))
    print('smalled')
    pic.save_numpy_img(smaller, name='smaller.png')
    exit()
    test_image()


if __name__ == '__main__':
    main()
