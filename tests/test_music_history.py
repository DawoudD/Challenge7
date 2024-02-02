
from lib.music_history import *
import pytest

def test_music_history_empty():
    history = music_history()
    with pytest.raises(Exception) as e:
        history.add(None)
    error_messege = str(e.value)
    assert error_messege == "your history is empty!"
    # actual =history.get_history()
    # expected = []
    # assert actual == expected



def test_music_history_one_track():
    history1 = music_history()
    history1.add("a track")
    actual = history1.get_history()
    expected = ["a track"]
    assert actual == expected





def test_music_history_several_tracks():
    history2 = music_history()
    history2.add("track_1")
    history2.add("track_3")
    history2.add("track_2")
    actual = history2.get_history()
    expected = ["track_1", "track_3", "track_2"]
    assert actual == expected

