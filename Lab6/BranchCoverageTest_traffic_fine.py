"""Branch and boundary coverage: Shreya Yashodhara Singh, PES1UG24AM266."""
import pytest
from traffic_fine import speeding_fine, license_action, total_penalty


@pytest.mark.parametrize('zone,base', [('school', 2000), ('highway', 1000), ('city', 500), ('rural', 500)])
@pytest.mark.parametrize('excess,multiplier', [(-1, 0), (0, 0), (1, 1), (20, 1), (21, 2), (40, 2), (41, 3)])
def test_speed_thresholds(zone, base, excess, multiplier):
    assert speeding_fine(60 + excess, 60, zone) == base * multiplier


@pytest.mark.parametrize('commercial', [False, True])
@pytest.mark.parametrize('repeat', [False, True])
@pytest.mark.parametrize('points', [0, 3, 4, 7, 8, 11, 12, 13])
def test_license_thresholds(points, commercial, repeat):
    expected = {
        0: 'none', 3: 'none', 4: 'notice', 7: 'notice',
        8: 'suspend' if repeat else 'warning',
        11: 'suspend' if repeat else 'warning',
        12: 'revoke' if commercial else 'suspend',
        13: 'revoke' if commercial else 'suspend',
    }[points]
    assert license_action(points, commercial, repeat) == expected


@pytest.mark.parametrize('fines,expected', [
    ([], 0), ([0], 0), ([100], 100), ([1000, 2000, 500], 3500),
    ([9999], 9999), ([5000, 5000], 10000), ([10001], 10000),
    ([10000, 1], 10000),
])
def test_total_boundaries(fines, expected):
    before = fines.copy()
    assert total_penalty(fines) == expected
    assert fines == before


@pytest.mark.parametrize('fines', [[-1], [500, -1], [10001, -1]])
def test_negative_fine_rejected_even_after_cap(fines):
    before = fines.copy()
    with pytest.raises(ValueError, match='^negative fine$'):
        total_penalty(fines)
    assert fines == before
