from .constant import CHO_NX, JUNG_NX, JONG_NX
from jamo import j2hcj, h2j, j2h
import math

def shift(source: str, target: str) -> list[str]:
    assert len(source) == 1
    assert len(target) == 1

    source = list(j2hcj(h2j(source)))
    target = list(j2hcj(h2j(target)))

    while len(source) != 3:
        source.append(' ')
    while len(target) != 3:
        source.append(' ')

    cho_path = CHO_NX.shortest_path(source[0], target[0])
    jung_path = JUNG_NX.shortest_path(source[1], target[1])
    jong_path = JONG_NX.shortest_path(source[2], target[2])

    lcm = math.lcm(len(cho_path), len(jung_path), len(jong_path))

    cho_keyframe = [item for item in cho_path for _ in range( lcm // len(cho_path) )]
    jung_keyframe = [item for item in jung_path for _ in range( lcm // len(jung_path) )]
    jong_keyframe = [item for item in jong_path for _ in range( lcm // len(jong_path) )]


    keyframe = []
    for i in range(lcm):
        if jong_keyframe[i] == ' ':
            ch = j2h(cho_keyframe[i], jung_keyframe[i])
        else:
            ch = j2h(cho_keyframe[i], jung_keyframe[i], jong_keyframe[i])

        try:
            if keyframe[-1] != ch:
                keyframe.append(ch)
        except IndexError:
            keyframe.append(ch)

    return keyframe

__all__ = ["shift"]