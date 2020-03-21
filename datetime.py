In [1]: from datetime import datetime

In [2]: birthday = datetime(1984, 4, 15)

In [3]: birthday.day
Out[3]: 15

In [4]: birthday.year
Out[4]: 1984

In [5]: birthday.month
Out[5]: 4

In [6]: birthday.weekday()
Out[6]: 6

In [7]: datetime.now()
Out[7]: datetime.datetime(2020, 2, 23, 19, 48, 43, 594819)

In [8]: datetime.now()
Out[8]: datetime.datetime(2020, 2, 23, 19, 48, 47, 581749)

In [9]: datetime.now()
Out[9]: datetime.datetime(2020, 2, 23, 19, 48, 51, 13051)

In [10]: datetime.now() - birthday
Out[10]: datetime.timedelta(days=13097, seconds=71448, microseconds=953868)

In [11]: parsed_date = datetime.strptime('Jan 15, 2019', '%b %d, %Y')

In [12]: parsed_date
Out[12]: datetime.datetime(2019, 1, 15, 0, 0)

In [13]: date_string = datetime.strftime(datetime.now(), '%b %d, %Y')

In [14]: date_string
Out[14]: 'Feb 23, 2020'