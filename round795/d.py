import typing
import sys
input = sys.stdin.readline


class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = self._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    @staticmethod
    def _ceil_pow2(n: int) -> int:
        x = 0
        while (1 << x) < n:
            x += 1

        return x


def next_greater():
    s = []
    ret = [N] * N
    for i in range(N):
        while s and A[s[-1]] < A[i]:
            ret[s.pop()] = i
        s.append(i)
    return ret


def prev_greater():
    s = []
    ret = [-1] * N
    for i in range(N - 1, -1, -1):
        while s and A[s[-1]] < A[i]:
            ret[s.pop()] = i
        s.append(i)
    return ret


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    prefix = [A[0]] + [0] * (N - 1)
    suffix = [0] * (N - 1) + [A[N - 1]]
    for i in range(1, N):
        prefix[i] = prefix[i - 1] + A[i]
        suffix[N - i - 1] = suffix[N - i] + A[N - i - 1]

    pt = SegTree(max, -10 ** 20, prefix)
    st = SegTree(max, -10 ** 20, suffix)

    ng = next_greater()
    pg = prev_greater()

    flg = True
    for i in range(N):
        l_max, r_max = 0, 0
        if i + 1 < ng[i]:
            r_max = pt.prod(i + 1, ng[i]) - prefix[i]
        if pg[i] + 1 < i:
            l_max = st.prod(pg[i] + 1, i) - suffix[i]
        if max(r_max, l_max) > 0:
            flg = False
    if flg:
        print('YES')
    else:
        print('NO')
