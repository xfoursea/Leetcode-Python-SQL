import pytest
from solution import solution
# test single entry
def test_calBrowsingTime_2_entries():
    solution1 = solution()
    e1= solution1.user_visit(34.05194, -118.25812, '10/07/2020 10:12:35', '10/07/2020 18:12:35')
    x = solution1.calBrowsingTime([e1])
    assert x['34.05194,-118.25812'] == 480
# test 2 entries with different lat/lon, expect 2 dictionary entries since group by location
def test_calBrowsingTime_entries_diffLocations():
    solution1 = solution()
    e1= solution1.user_visit(34.05194, -118.25812, '10/07/2020 10:12:35', '10/07/2020 18:12:35')
    e2= solution1.user_visit(35.05194, -118.25812, '10/07/2020 10:13:35', '10/07/2020 10:14:35')
    x = solution1.calBrowsingTime([e1, e2])
    assert len(x) == 2 and x['34.05194,-118.25812'] == 480 and x['35.05194,-118.25812'] == 1
# test starttime earlier than 8 am, endtime later than 8 pm, expect only count for 8am-8pm
def test_calBrowsingTime_entries_beyondTimeWindow():
    solution1 = solution()
    e1= solution1.user_visit(34.05194, -118.25812, '10/07/2020 07:12:35', '10/07/2020 20:12:35')
    e2= solution1.user_visit(35.05194, -118.25812, '10/07/2020 12:13:35', '10/07/2020 20:14:35')
    x = solution1.calBrowsingTime([e1, e2])
    assert len(x) == 2 and x['34.05194,-118.25812'] == 720 and x['35.05194,-118.25812'] == 466

# test starttime and endtime are in different days
def test_calBrowsingTime_entries_differentDays():
    solution1 = solution()
    e1= solution1.user_visit(34.05194, -118.25812, '10/07/2020 10:12:35', '11/07/2020 07:12:35')
    x = solution1.calBrowsingTime([e1])
    assert x['34.05194,-118.25812'] == 587

# test starttime is after 8 pm and endtime is before 8 am the next day
def test_calBrowsingTime_entries_differentDaysWindows():
    solution1 = solution()
    e1 = solution1.user_visit(34.05194, -118.25812, '10/07/2020 21:12:35', '11/07/2020 07:12:35')
    x = solution1.calBrowsingTime([e1])
    assert x['34.05194,-118.25812'] == 0


