from datetime import datetime, date, timedelta
from datetime import timezone as datetime_timezone
from pytz import timezone as pytz_timezone
from dateutil import tz as dateutil_timezone
from zoneinfo import ZoneInfo  # Python 3.9


print('Strings to Dates')
dates_str_list = ['11/20/2015', '01/09/2016', '02/28/2016', '04/18/2016', '06/07/2016', '07/27/2016', '09/15/2016']

# Iterate over the dates_str_list
for date_str in dates_str_list:
    # Convert each date to a datetime object
    date_dt = datetime.strptime(date_str, '%m/%d/%Y')

    # Print each date_dt
    print(date_dt)


print('Strings to DateTimes')
datetimes_str_list = ['11/20/2015 00:00:01', '01/09/2016 13:14:15', '02/28/2016 08:00:00']

# Iterate over the dates_str_list
for date_str in datetimes_str_list:
    # Convert each date to a datetime object
    date_dt = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')

    # Print each date_dt
    print(date_dt)


print('Dates to Strings')
dates_list = [date(2015, 11, 20), date(2016, 1, 9), date(2016, 2, 28), date(2016, 4, 18)]

# Converting to a String
for item in dates_list:
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(date.strftime(item, '%m/%d/%Y'))

    # Print the date in the format 'YYYY-MM'
    print(item.strftime('%Y-%m'))

    # Print the date in the format 'MONTH (YYYY)'
    print(item.strftime('%B (%Y)'))

    # Print the date in the format 'YYYY-DDD'
    print(item.strftime('%Y-%j'))

    # Print out the record as an ISO standard string
    print(date.isoformat(item))

    # Pieces of time
    print(item.day, item.month, item.year)


print('DateTimes to Strings')
datetimes_list = [datetime(2015, 11, 20), datetime(2016, 1, 9, 11, 22, 33), datetime(2016, 2, 28, 21, 12, 0, 500000),
                  datetime(2016, 4, 18)]

# Converting to a String
for item in datetimes_list:
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(datetime.strftime(item, '%m/%d/%Y'))

    # Print out the record as an ISO standard string
    print(datetime.isoformat(item))

    # Pieces of time
    print(item.day, item.month, item.year, item.hour, item.minute, item.second, item.microsecond)


print('Putting a list of dates in order')
# Put the dates in order
dates_list_ordered = sorted(dates_list)

# Print the first and last ordered dates
print(dates_list_ordered[0])
print(dates_list_ordered[-1])


print('Change dates')
print(dates_list_ordered[1])
# Replace the year with 1916
print(dates_list_ordered[1].replace(year=1916))


print('Unix timestamps')
# Starting timestamps
timestamps = [1514665153, 1514664543]

# Datetime objects
dts = [datetime.fromtimestamp(ts) for ts in timestamps]

# Print results
print(dts)


# Creating DateTime Objects... Now
# Compute the local datetime: local_dt
print(datetime.now())

# Compute and print the UTC datetime: utc_dt
print(datetime.utcnow())


print('Timezones')
# October 1, 2017 at 15:26:26, UTC
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=datetime_timezone.utc)

# Print results
print(dt.isoformat())


# Create a timezone for Pacific Standard Time, or UTC-8
pst = datetime_timezone(timedelta(hours=-8))

# October 1, 2017 at 15:26:26, UTC-8
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)

# Print results
print(dt.isoformat())


# October 1, 2017 at 15:26:26, timezone for London
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=dateutil_timezone.gettz('Europe/London'))

# Print results
print(dt.isoformat())


# Create a Timezone object for Chicago and New York
chicago_usa_tz = pytz_timezone('US/Central')
# chicago_usa_tz = dateutil_timezone.gettz('US/Central')
# chicago_usa_tz = ZoneInfo("US/Central")

ny_usa_tz = pytz_timezone('US/Eastern')
# ny_usa_tz = dateutil_timezone.gettz('US/Eastern')
# ny_usa_tz = ZoneInfo("US/Eastern")

# Iterate over the datetimes list
for orig_dt in datetimes_list:
    # Make the orig_dt timezone "aware" for Chicago
    chicago_dt = orig_dt.replace(tzinfo=chicago_usa_tz)

    # Convert chicago_dt to the New York Timezone
    ny_dt = chicago_dt.astimezone(ny_usa_tz)

    # Print the chicago_dt, ny_dt, and ridership
    print('Chicago: %s, NY: %s' % (chicago_dt, ny_dt))


# Time in the future and from the past
# Build a timedelta of 30 days
glanceback = timedelta(days=30)

# Iterate over the datetimes_list as date
for date in datetimes_list:
    # Calculate the date 30 days back: prior_period_dt
    prior_period_dt = date - glanceback

    # Print dates
    print(date, prior_period_dt)


# Finding differences in DateTimes
datetimes_sub = datetimes_list[1] - datetimes_list[0]
print(datetimes_sub)
print(datetimes_sub.days)
print(datetimes_sub.total_seconds())


print('How many hours elapsed around daylight saving?')
# Start on March 28, 2021, midnight, then add 6 hours
start = datetime(2021, 3, 28, tzinfo=dateutil_timezone.gettz('Europe/Warsaw'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())

# How many hours have elapsed?
print((end - start).total_seconds()/(60*60))

# What if we move to UTC?
print((end.astimezone(datetime_timezone.utc) - start.astimezone(datetime_timezone.utc)).total_seconds()/(60*60))


start = datetime(2021, 10, 31, tzinfo=dateutil_timezone.gettz('Europe/Warsaw'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())
print((end - start).total_seconds()/(60*60))
print((end.astimezone(datetime_timezone.utc) - start.astimezone(datetime_timezone.utc)).total_seconds()/(60*60))


print('March 29, throughout a decade')
# Create starting date
dt = datetime(2000, 3, 29, tzinfo=dateutil_timezone.gettz('Europe/London'))

# Loop over the dates, replacing the year, and print the ISO timestamp
for y in range(2000, 2011):
    print(dt.replace(year=y).isoformat())


dts = [datetime(2021, 10, 30, 23, 30, 0, tzinfo=datetime_timezone.utc),
       datetime(2021, 10, 31, 0, 0, 0, tzinfo=datetime_timezone.utc),
       datetime(2021, 10, 31, 0, 30, 0, tzinfo=datetime_timezone.utc),
       datetime(2021, 10, 31, 1, 0, 0, tzinfo=datetime_timezone.utc),
       datetime(2021, 10, 31, 1, 30, 0, tzinfo=datetime_timezone.utc),
       datetime(2021, 10, 31, 2, 1, 1, tzinfo=datetime_timezone.utc)]

dts = [dt.astimezone(dateutil_timezone.gettz('Europe/Warsaw')) for dt in dts]

print('Finding ambiguous datetimes')
for dt in dts:
    if dateutil_timezone.datetime_ambiguous(dt):
        print(f"Date {dt} fold={dt.fold} is ambiguous")
    else:
        print(f"Date {dt} fold={dt.fold}")


print('Sorting with timezone')
for dt in sorted(dts):
    print(dt)

print('Sorting with timezone as utc')
dts_sorted = sorted([dt.astimezone(datetime_timezone.utc) for dt in dts])
dts_sorted = [dt.astimezone(dateutil_timezone.gettz('Europe/Warsaw')) for dt in dts_sorted]
for dt in dts_sorted:
    print(dt)
