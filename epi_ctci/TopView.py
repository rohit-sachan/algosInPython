# its an example of line sweep algorithm as well
from sortedcontainers import SortedDict
import unittest

class Segment:
    def __init__(self, left, right, height, name):
        self.height = height
        self.right = right
        self.left = left
        self.name = name

    def __eq__(self, other):
        return (self.left, self.right, self.name) == (other.left, other.right, other.name)

    def __str__(self):
        return self.__repr__(self)

    def __repr__(self):
        return "({0}-{1}@{2},{3})".format(self.name, self.height, self.left, self.right)

    def __hash__(self) -> int: return super().__hash__()


class Endpoint:
    def __init__(self, is_left, segment):
        self.is_left = is_left
        self.segment = segment

    def value(self):
        return self.segment.left if self.is_left else self.segment.right

    def segment(self):
        return self.segment

    def __repr__(self):
        return "({0}{1})".format(self.segment.name, self.value())

    def __lt__(self,other): return self.segment.height > other.segment.height

    def __eq__(self,other): return self.segment.height == other.segment.height

    def __hash__(self) -> int: return hash((self.is_left, self.segment))


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

        resulted_segments = []
        # sweeper = SortedDict(key=lambda ep: ep.height)
        sweeper = SortedDict()
        print(sweeper)

        for endpoint_ in sorted_endpoints:
            if sweeper.__len__() == 0:
                sweeper[endpoint_] = endpoint_.segment
            elif not endpoint_.is_left: # right of some segment
                left_ep = Endpoint(True, endpoint_.segment)
                if left_ep.__eq__(sweeper.peekitem(0)[0]): # "top most" is ending now
                    sweeper.pop(sweeper.peekitem(0)[0])
                    prev_seg = resulted_segments[resulted_segments.__len__()-1]
                    resulted_segments.append(Segment(prev_seg.right,endpoint_.segment.right,endpoint_.segment.height,endpoint_.segment.name))
                else: # some segment "not at top" needs to end now
                    sweeper.pop(left_ep)
            elif sweeper.peekitem(0)[0].segment.height < endpoint_.segment.height: # crossover, a higher segment found
                current_top = sweeper.peekitem(0)[0]
                if resulted_segments.__len__() > 0:
                    last_segment = resulted_segments[resulted_segments.__len__()-1]
                    resulted_segments.append(Segment(last_segment.right,endpoint_.segment.left,current_top.segment.height,current_top.segment.name))
                else:
                    resulted_segments.append(Segment(current_top.segment.left,endpoint_.segment.left,current_top.segment.height,current_top.segment.name))
                sweeper[endpoint_] = endpoint_.segment
            elif sweeper.peekitem(0)[0].segment.height > endpoint_.segment.height: # non contributing end found
                sweeper[endpoint_] = endpoint_.segment

        return resulted_segments


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
        Segment(0, 1, 1, 'A'),
        Segment(1, 3, 3, 'B'),
        Segment(3, 4, 2, 'C'),
        Segment(4, 5, 4, 'D'),
        Segment(5, 6, 2, 'C'),
        Segment(6, 10, 3, 'F'),
        Segment(10, 11, 1, 'H'),
        Segment(11, 13, 3, 'I'),
        Segment(13, 14, 2, 'J'),
        Segment(14, 15, 3, 'K'),
        Segment(15, 16, 1, 'H'),
        Segment(16, 17, 3, 'L'),
        Segment(17, 18, 1, 'H'),
    ]
    print("found " + str (view == expectedView))
