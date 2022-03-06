from PIL import Image
import os
from math import ceil


def collage_aux(list_of_all_photos,
                no_pics_per_row,
                no_of_photos,
                collage_background,
                no_of_rows):
    """Make the actual collage.
    Keyword arguments:
    list_of_all_photos - a list of photos to be included in collage
    no_pics_per_row - number of photos,
    that the collage will fit in one row
    no_of_photos - number of photos in the collage
    collage_background - a white Image object to put the photos on
    no_of_rows - number of rows in the collage
    """
    list_of_heights = []
    list_of_photos_sorted_up = sorted(list_of_all_photos,
                                      key=lambda x: x.height)
    list_of_photos_sorted_down = sorted(list_of_all_photos,
                                        key=lambda x: x.height, reverse=True)
    for _ in range(no_pics_per_row):
        list_of_heights.append(0)
    total_pics_counter = 0
    for row in range(no_of_rows):
        for pic_no in range(no_pics_per_row):
            photo = (list_of_photos_sorted_up[0] if row % 2
                     else list_of_photos_sorted_down[0])
            collage_background.paste(photo,
                                     (pic_no*photo.width,
                                      list_of_heights[pic_no]))
            list_of_heights[pic_no] += photo.height
            (list_of_photos_sorted_up.pop(0) if row % 2
             else list_of_photos_sorted_down.pop(0))
            total_pics_counter += 1
            if total_pics_counter == no_of_photos:
                break
    return collage_background, list_of_heights


def collage(folder_with_photos,
            name_for_collage,
            no_of_photos=2,
            no_pics_per_row=1):
    """Create a collage out of given photos.
    Keyword arguments:
    folder_with_photos -- path to a folder with photos inside of it
    name_for_collage -- name for the newly made collage
    no_of_photos -- number of photos in the collage (default 2)
    no_pics_per_row -- number of photos,
    that the collage will fit in one row (default 1)
    """
    list_of_all_photos = [Image.open(f"{folder_with_photos}/{photo}") for photo
                          in os.listdir(folder_with_photos)]
    max_height = max(photo.height for photo in list_of_all_photos)
    image_width = 1080
    no_of_rows = ceil(no_of_photos / no_pics_per_row)
    collage_background = Image.new("RGB",
                                   (no_pics_per_row * image_width,
                                    max_height * no_of_rows), "white")
    collage_filled = collage_aux(list_of_all_photos,
                                 no_pics_per_row,
                                 no_of_photos,
                                 collage_background,
                                 no_of_rows)
    collage_final = collage_filled[0].crop((0, 0,
                                           no_pics_per_row*image_width,
                                           max(collage_filled[1])))
    collage_final.save(f"{name_for_collage}", "JPEG")
