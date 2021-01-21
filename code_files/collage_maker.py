from PIL import Image
import os


def collage(folder_with_photos,
            name_for_collage,
            no_of_rows=1,
            no_of_pics_per_row=[]):
    """Create a collage out of given photos.
    Keyword arguments:
    folder_with_photos -- path to a folder with photos inside of it
    name_for_collage -- the created collage will be saved under that variable's name
    no_of_rows -- number of rows that the collage shall have (default 1)
    no_of_pics_per_row -- a list of integers indicating how many pictures will be in each of the rows (default [])
    """
    list_of_all_photos = [Image.open(f"{folder_with_photos}/{photo}") for photo
                          in os.listdir(folder_with_photos)]
    max_height = max(photo.size[1] for photo in list_of_all_photos)
    image_width = 1080
    list_with_grouped_rows = []
    for row in range(no_of_rows):
        list_one_row = []
        for _ in range(no_of_pics_per_row[row]):
            list_one_row.append(list_of_all_photos[0])
            list_of_all_photos.pop(0)
        list_with_grouped_rows.append(list_one_row)

    collage_background = Image.new("RGB",
                                   (max(no_of_pics_per_row)*image_width,
                                    max_height*no_of_rows))
    for row in enumerate(list_with_grouped_rows):
        photo_counter = 0
        for pic in range(no_of_pics_per_row[row[0]]):
            photo = row[1][photo_counter]
            collage_background.paste(photo,
                                     (pic*image_width, row[0]*max_height))
            photo_counter += 1
    collage_background.show()
    collage_background.save(f"{name_for_collage}.jpg", "JPEG")
