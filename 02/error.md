gitpod /workspace/boilerplate-demographic-data-analyzer (main) $ /home/gitpod/.pyenv/shims/python /workspace/boilerplate-demographic-data-analyzer/main.py
Number of each race:
 White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
Name: race, dtype: int64
Average age of men: nan
Percentage with Bachelors degrees: 16.44605509658794%
Percentage with higher education that earn >50K: Bachelors    16.446055
Masters       5.291607
Doctorate     1.268389
Name: education, dtype: float64%
Percentage without higher education that earn >50K: Bachelors     7.634901
Masters      18.789349
Doctorate    22.812567
Name: education, dtype: float64%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 0.006142317496391388%
Country with highest percentage of rich: United-States
Highest percentage of rich people in country: 22.023279383311323%
Top occupations in India: Prof-specialty
FEFFE.F.F.
======================================================================
ERROR: test_higher_education_rich (test_module.DemographicAnalyzerTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/boilerplate-demographic-data-analyzer/test_module.py", line 27, in test_higher_education_rich
    self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage with higher education that earn >50K.")
  File "/home/gitpod/.pyenv/versions/3.8.20/lib/python3.8/unittest/case.py", line 937, in assertAlmostEqual
    if first == second:
  File "/workspace/.pyenv_mirror/user/current/lib/python3.8/site-packages/pandas/core/generic.py", line 1527, in __nonzero__
    raise ValueError(
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

======================================================================
ERROR: test_lower_education_rich (test_module.DemographicAnalyzerTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/boilerplate-demographic-data-analyzer/test_module.py", line 32, in test_lower_education_rich
    self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage without higher education that earn >50K.")
  File "/home/gitpod/.pyenv/versions/3.8.20/lib/python3.8/unittest/case.py", line 937, in assertAlmostEqual
    if first == second:
  File "/workspace/.pyenv_mirror/user/current/lib/python3.8/site-packages/pandas/core/generic.py", line 1527, in __nonzero__
    raise ValueError(
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

======================================================================
FAIL: test_average_age_men (test_module.DemographicAnalyzerTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/boilerplate-demographic-data-analyzer/test_module.py", line 17, in test_average_age_men
    self.assertAlmostEqual(actual, expected, msg="Expected different value for average age of men.")
AssertionError: nan != 39.4 within 7 places (nan difference) : Expected different value for average age of men.

======================================================================
FAIL: test_highest_earning_country (test_module.DemographicAnalyzerTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/boilerplate-demographic-data-analyzer/test_module.py", line 47, in test_highest_earning_country
    self.assertEqual(actual, expected, "Expected different value for highest earning country.")
AssertionError: 'United-States' != 'Iran'
- United-States
+ Iran
 : Expected different value for highest earning country.

======================================================================
FAIL: test_highest_earning_country_percentage (test_module.DemographicAnalyzerTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/boilerplate-demographic-data-analyzer/test_module.py", line 52, in test_highest_earning_country_percentage
    self.assertAlmostEqual(actual, expected, msg="Expected different value for highest earning country percentage.")
AssertionError: 22.023279383311323 != 41.9 within 7 places (19.876720616688676 difference) : Expected different value for highest earning country percentage.

======================================================================
FAIL: test_percentage_bachelors (test_module.DemographicAnalyzerTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/boilerplate-demographic-data-analyzer/test_module.py", line 22, in test_percentage_bachelors
    self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage with Bachelors degrees.")
AssertionError: 16.44605509658794 != 16.4 within 7 places (0.046055096587942046 difference) : Expected different value for percentage with Bachelors degrees.

======================================================================
FAIL: test_rich_percentage (test_module.DemographicAnalyzerTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/boilerplate-demographic-data-analyzer/test_module.py", line 42, in test_rich_percentage
    self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage of rich among those who work fewest hours.")
AssertionError: 0.006142317496391388 != 10 within 7 places (9.99385768250361 difference) : Expected different value for percentage of rich among those who work fewest hours.

----------------------------------------------------------------------
Ran 10 tests in 0.210s

FAILED (failures=5, errors=2)