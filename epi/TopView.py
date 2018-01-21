from collections import OrderedDict
from functools import cmp_to_key

class Segment:
    def __init__(self, s, e, h, n):
        self.h = h
        self.e = e
        self.s = s
        self.n = n

    def __eq__(self, other):
        return (self.s, self.e, self.n) == (other.s, other.e, other.n)

    def __str__(self):
        return self.__repr__(self)

    def __repr__(self):
        return "({0}-{1}@{2},{3})".format(self.n, self.h, self.s, self.e)


def mycmp(segment_1, segment_2):
    if segment_1.h < segment_2.h:
        return -1
    elif segment_1.h > segment_2:
        return 1
    else:
        if segment_1.s < segment_2.s:
            return -1
        elif segment_1.s > segment_2.s:
            return 1
        else:
            return 0


class Blocks:
    def __init__(self, _segments):
        self.segments = _segments
        print("passed ")
        print(_segments)

    def top_view(self):
        return sorted(self.segments, key=cmp_to_key(mycmp), reverse=True)
        # return self.segments


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
    blocks = Blocks(segments)
    view = blocks.top_view()
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
    print("top view ")
    print(view)
    # print("found " + view == expectedView)
