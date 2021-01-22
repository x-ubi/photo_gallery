from code_files.gui import (get_data_from_json_file,
                 topics_list,
                 photos_list
                 )


def test_get_data_from_file():
    data = get_data_from_json_file()
    assert data == {"topic-fetching-url": "https://api.unsplash.com/topics?"
                    "client_id=-hpd125zy8DilndMtKzI2ueQg7zpgagq4nTSbR7osUM;"
                    "per_page=100",
                    "photo-fetching-url": "https://api.unsplash.com/topics/"
                    "{given_id}/photos?client_id="
                    "-hpd125zy8DilndMtKzI2ueQg7zpgagq4nTSbR7osUM;"
                    "per_page={given_number};page={given_page}"
                    }


def test_topics_list():
    topics = topics_list()
    assert len(topics) == 25


def test_photos_list():
    photos = photos_list('wallpapers', 5, 1)
    assert len(photos) == 5

