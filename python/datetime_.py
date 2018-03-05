from datetime import datetime
from pytz import timezone
from datetime import timedelta


dates_list = ['11/20/2015', '01/09/2016', '02/28/2016', '04/18/2016', '06/07/2016', '07/27/2016', '09/15/2016']
datetimes_list = [datetime(2015, 11, 20), datetime(2016, 1, 9), datetime(2016, 2, 28), datetime(2016, 4, 18)]


# Strings to DateTimes
# Iterate over the dates_list
for date_str in dates_list:
    # Convert each date to a datetime object
    date_dt = datetime.strptime(date_str, '%m/%d/%Y')

    # Print each date_dt
    print(date_dt)


# Converting to a String
for item in datetimes_list:
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(datetime.strftime(item, '%m/%d/%Y'))

    # Print out the record as an ISO standard string
    print(datetime.isoformat(item))

    # Pieces of time
    print(item.day, item.month, item.year)


# Creating DateTime Objects... Now
# Compute the local datetime: local_dt
local_dt = datetime.now()

# Print the local datetime
print(local_dt)

# Compute and print the UTC datetime: utc_dt
print(datetime.utcnow())


# Timezones
# Create a Timezone object for Chicago and New York
chicago_usa_tz = timezone('US/Central')
ny_usa_tz = timezone('US/Eastern')

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
print(datetimes_list[1] - datetimes_list[0])
