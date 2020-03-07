Idea:
make d3dshot easier to use and add some utilities.

Has a Camera class which:
	works with 'with Camera() as cam:'
	grab_regions_to_numpy()
        	Converts a list of coordinate groups to separate images from full screenshot
        	:param regions: [(r1, t1, l1, b1}, (r2, t2, l2, b2), ...]
        	:return: all images in order
        	:rtype: list
	save_numpy_img(data, name=None):
		name then defaults to the time
	grab_vital_pixels(data, new_dimensions: tuple):
		turns numpy image and rescales it new dimensions.
		new_dimensions is (x_wide, y_wide)

I am still working on improving my documentation.