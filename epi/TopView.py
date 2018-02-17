class Segment:
    def __init__(self, left, right, height, name):
        self.height = height
        self.right = right
        self.left = left
        self.name = name

    def __eq__(self, other):
        return (self.left, self.right, self.name) == (other.s, other.e, other.n)

    def __str__(self):
        return self.__repr__(self)

    def __repr__(self):
        return "({0}-{1}@{2},{3})".format(self.name, self.height, self.left, self.right)


class Endpoint:
    def __init__(self, is_left, segment):
        self.is_left = is_left
        self.segment = segment

    def value(self):
        return self.segment.left if self.is_left else self.segment.right

    def __repr__(self):
        return "({0}{1})".format(self.segment.name, self.value())


class Structure:
    def __init__(self, _segments):
        self.segments = _segments
        print("passed segments ")
        print(_segments)

    def top_view(self):
        sorted_endpoints = []
        for segment_ in self.segments:
            sorted_endpoints.append(Endpoint(True, segment_))
            sorted_endpoints.append(Endpoint(False, segment_))
        sorted_endpoints.sort(key=lambda end_point: end_point.value()) # O n(log n)
        return sorted_endpoints

    @staticmethod
    def sort_endpoints(end_points):
        return


segments = [Segment(0, 4, 1, 'A'),
            Segment(5, 7, 1, 'E'),
            Segment(9, 18, 1, 'H'),
            Segment(8, 9, 2, 'G'),
            Segment(2, 7, 2, 'C'),
            Segment(12, 15, 2, 'J'),
            Segment(1, 3, 3, 'B'),
            Segment(6, 10, 3, 'F'),
            Segment(11, 13, 3, 'I'),
            Segment(14, 15, 3, 'K'),
            Segment(16, 17, 3, 'L'),
            Segment(4, 5, 4, 'D')
            ]
if __name__ == '__main__':
    structure = Structure(segments)
    view = structure.top_view()
    print("top view ")
    print(view)

    expectedView = [
        Segment(0, 1, 5, 'A'),
        Segment(1, 3, 5, 'B'),
        Segment(3, 4, 5, 'C'),
        Segment(4, 5, 5, 'D'),
        Segment(5, 6, 5, 'C'),
        Segment(6, 10, 5, 'F'),
        Segment(10, 11, 5, 'H'),
        Segment(11, 13, 5, 'I'),
        Segment(13, 14, 5, 'J'),
        Segment(14, 15, 5, 'K'),
        Segment(15, 16, 5, 'H'),
        Segment(16, 17, 5, 'L'),
        Segment(17, 18, 5, 'H'),
    ]
    # print("found " + view == expectedView)
