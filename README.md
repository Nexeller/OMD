## 1
1.`python -m doctest -o NORMALIZE_WHITESPACE -v test_issue-01.py`.\
2.скриншот в `issue1.png`

## 2
0.ставим пакет `pytest`\
1.`python -m pytest -v test_issue-02.py`\
2.скриншот в `issue2.png`

## 3
1.`python -m unittest test_issue-03.py`\
1.скриншот в `issue3.png`

## 4
1.`python -m pytest test_issue-04.py`\
2.скриншот в `issue4.png`

## 5
1.ставим пакет `requests`\
2.`python -m pytest -v -s test_issue-05.py`\
3.`python -m pytest -q test_issue-05.py --cov=what_is_year_now`\
4.`python -m pytest --cov . --cov-report html`\ 
5.скриншоты в  `issue5.1(5.2).png`
