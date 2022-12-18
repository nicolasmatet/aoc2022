import re

import numpy as np

from utils import count_items

pattern = re.compile("Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)")


def spheres():
    for line in open("input.txt"):
        res = [int(v) for v in re.match(pattern, line).groups()]
        center = (res[0], res[1])
        radius = abs(res[0] - res[2]) + abs(res[1] - res[3])
        yield Sphere(center, radius)


def beacons():
    for line in open("input.txt"):
        res = [int(v) for v in re.match(pattern, line).groups()]
        yield res[2], res[3]


class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def x_intersection(self, y):
        delta_y = abs(self.center[1] - y)
        intersection_radius = self.radius - delta_y
        if intersection_radius < 0:
            return None
        return self.center[0] - intersection_radius, self.center[0] + intersection_radius + 1

    def has_intersection(self, y):
        delta_y = abs(self.center[1] - y)
        return self.radius - delta_y >= 0


def remove_intersection(ref_segment, segments):
    start, end = ref_segment
    truncated_segments = []
    min_intersection = np.inf
    for seg in segments:
        if (new_end := max(end, seg[0])) < seg[1]:
            if new_end != seg[0]:
                min_intersection = min(min_intersection, new_end - seg[0])
            truncated_segments.append((new_end, seg[1]))
    return truncated_segments, min_intersection


def join_sorted_segments(segments):
    joined = [segments[0]]
    for seg in segments[1:]:
        if seg[0] == joined[-1][1]:
            joined[-1] = (joined[-1][0], seg[1])
        else:
            joined.append(seg)
    return joined


def remove_all_intersections(segments):
    segment_to_truncate = sorted([*segments], key=lambda seg: seg[0])
    truncated_segments = []
    min_intersection = np.inf

    while segment_to_truncate:
        truncated_segments.append(segment_to_truncate.pop(0))
        segment_to_truncate, _min_intersection = remove_intersection(truncated_segments[-1], segment_to_truncate)
        min_intersection = min(min_intersection, _min_intersection)
    return truncated_segments, min_intersection


def reduce_search_space(segments, search_max):
    while segments[0][0] < 0 and segments[0][1] < 0:
        segments.pop(0)
    if segments[0][1] >= 0:
        segments[0] = (0, segments[0][1])

    while segments[-1][0] > search_max and segments[-1][1] > search_max:
        segments.pop()
    if segments[-1][0] < search_max:
        segments[-1] = (segments[-1][0], search_max)
    return segments


def solve1(y=10):
    segments = [s.x_intersection(y) for s in spheres() if s.has_intersection(y)]
    segments, _ = remove_all_intersections(segments)
    len_segments = sum(seg[1] - seg[0] for seg in segments)
    n_beacons = count_items(set(beacons()), where=lambda b: b[1] == y)
    return len_segments - n_beacons


def solve2(search_max=20):
    found = []
    y = 0
    loops = 0
    while y < search_max:
        if loops % 1000 == 0:
            print("y=", y)
        segments = [s.x_intersection(y) for s in spheres() if s.has_intersection(y)]
        segments, min_intersection = remove_all_intersections(segments)
        segments = join_sorted_segments(segments)
        if len(segments) == 1:
            loops += 1
            y += min_intersection
            continue
        segments = reduce_search_space(segments, search_max)
        print("segments", segments, y)
        found.append((segments[0][1], y))
        break
    if not found:
        return None
    return found[0][0] * 4000000 + found[0][1]


if __name__ == "__main__":
    # print(solve1(y=2000000))
    print(solve2(search_max=4000000))
