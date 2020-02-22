import d3dshot
import time


def test_image():
    now = time.time()
    d = d3dshot.create(capture_output='numpy')
    num_test = 1
    for a in range(num_test):
        # print(a)
        # a += 1
        d.screenshot()
    print(num_test / (time.time() - now), 'fps')


def shot_part(left, top, right, bottom):
    d = d3dshot.create()
    data = d.screenshot

    pass


def main():
    shot_part(0, 0, 0, 0)
    exit()
    test_image()


if __name__ == '__main__':
    main()
