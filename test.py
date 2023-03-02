from whiteboard import solution
from unittest import TestCase


class TestWhiteboard(TestCase):

    def test_anagrams1(self):
        s, t = "anagram", "nagaram"
        self.assertTrue(solution(s, t))

    def test_not_anagrams1(self):
        s, t = "stops", "pots"
        self.assertFalse(solution(s, t))

    def test_not_anagrams2(self):
        s, t = "rat", "car"
        self.assertFalse(solution(s, t))

    def test_not_anagrams2(self):
        s, t = "hello", "world"
        self.assertFalse(solution(s, t))

    def test_different_lengths(self):
        s, t = "abcd", "abc"
        self.assertFalse(solution(s, t))
