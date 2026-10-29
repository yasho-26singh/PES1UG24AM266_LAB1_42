"""Line coverage: Shreya Yashodhara Singh, PES1UG24AM266."""
import pytest
from traffic_fine import speeding_fine, license_action, total_penalty


@pytest.mark.parametrize('speed,limit,zone,expected', [
    (50, 60, 'city', 0),
    (65, 60, 'school', 2000),
    (85, 60, 'highway', 2000),
    (101, 60, 'city', 1500),
])
def test_speeding_statements(speed, limit, zone, expected):
    assert speeding_fine(speed, limit, zone) == expected


@pytest.mark.parametrize('points,commercial,repeat,expected', [
    (12, True, False, 'revoke'), (12, False, False, 'suspend'),
    (8, False, True, 'suspend'), (8, False, False, 'warning'),
    (4, False, False, 'notice'), (0, False, False, 'none'),
])
def test_license_statements(points, commercial, repeat, expected):
    assert license_action(points, commercial, repeat) == expected


@pytest.mark.parametrize('fines,expected', [([], 0), ([0, 2000, 500], 2500), ([6000, 5000], 10000)])
def test_total_statements(fines, expected):
    before = fines.copy()
    assert total_penalty(fines) == expected
    assert fines == before


def test_negative_fine():
    with pytest.raises(ValueError, match='^negative fine$'):
        total_penalty([500, -1])
