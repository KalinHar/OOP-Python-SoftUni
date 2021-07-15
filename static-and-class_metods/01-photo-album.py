import math


class PhotoAlbum:
    PAGE_PHOTOS = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(math.ceil(photos_count / cls.PAGE_PHOTOS))

    def add_photo(self, label):
        for page in self.photos:
            if len(page) < self.PAGE_PHOTOS:
                page.append(label)
                return f"{label} photo added successfully " \
                       f"on page {self.photos.index(page) + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        result = ["-----------"]
        for page in self.photos:
            result.append(" ".join(["[]" for _ in page]))
            result.append("-----------")
        return "\n".join(result)


album = PhotoAlbum(2)
album2 = PhotoAlbum.from_photos_count(8)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
print(album2.display())
