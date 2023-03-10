from math import ceil


class PhotoAlbum():
    PAGE_LENGTH = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PAGE_LENGTH)
        return cls(pages)

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos, 1):
            if len(page) < PhotoAlbum.PAGE_LENGTH:
                page.append(label)
                return f'{label} photo added successfully on page {i} slot {len(self.photos[i-1])}'
        return f'No more free slots'

    def display(self):
        output = [f'{"-" * 11}']
        for page in self.photos:
            output.append(f'{" ".join("[]" for _ in range(len(page)))}')
            output.append(f'{"-"*11}')
        return "\n".join(output)


pa = PhotoAlbum(2)
print(pa.add_photo("tr"))
print(pa.add_photo("tr2"))
print(pa.add_photo("tr3"))
print(pa.add_photo("tr4"))
print(pa.add_photo("tr5"))
print(pa.add_photo("tr6"))
print(pa.add_photo("tr7"))
print(pa.add_photo("tr8"))
print(pa.add_photo("tr9"))
print(pa.photos)
print(pa.display())
pa.display()

# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())

# PhotoAlbum.from_photos_count(13)