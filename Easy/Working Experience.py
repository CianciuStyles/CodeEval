import sys

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == '':
            continue

        years = {i: [False for _ in range(12)] for i in range(1990, 2021)}
        dates = test.strip().split('; ')
        for date in dates:
            start, end = list(map(lambda d: d.split(' '), date.split('-')))
            start[1], end[1] = int(start[1]), int(end[1])

            for year in range(start[1], end[1]+1):
                start_month = months.index(start[0]) if year == start[1] else 0
                end_month = months.index(end[0]) + 1 if year == end[1] else 12
                for month in range(start_month, end_month):
                    years[year][month] = True

        months_of_experience = sum(sum(1 for month in years[year] if month) for year in years.keys())
        print(months_of_experience // 12)