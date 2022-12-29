import time
import pandas as pd
import numpy as np
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle inonvalid inputs
    Cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input(
            'choose the city you would like to see the data \n').lower()
        if city not in Cities:
            print(
                "No Data for the selected city. Choose between chicago,new york city or washington.")
        else:
            print('Available city')
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input(
            'choose the month you want to display the data \n').lower()
        if month not in months:
            print("Please select available months between january to junle or all")
        else:
            print("Available month")
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input(
            'choose the Day of the week you want to display the data \n').lower()
        if day not in days:
            print(
                "Please select the correct day of the week between monday to sunday or all")
        else:
            break
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into data frame
    df = pd.read_csv(CITY_DATA[city])
    # convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of the week from start time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month
    if month != 'all':
        # use the index of the month list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('most common month is:', common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('most common day of the week is:', common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('most common start hour:', common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
   # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('most common start station is:', common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('most common used end station is:', common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station'] + ' - ' +
                        df['End Station']).mode()[0]
    print('Most Frequent Combination of Start and End Station:', common_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time is:', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time is:', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    except:
        print('Gender is not available')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        display_earliest = df['Birth Year'].min()
        print('earliest birth year:', display_earliest)
    except:
        print('Earliest Birth Year is not available for this city')
    try:
        recent_year = df['Birth Year'].max()
        print('most recent year:', recent_year)
    except:
        print('Most recent year is not available for this city')
    try:
        common_year = df['Birth Year'].mode()[0]
        print('most common year of birth:', common_year)
    except:
        print('Most common year is not available for this city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_row_count(df):
    raw_data = input(
        'Would you like to see first 5 rows of the raw data file? Yes or No\n').lower()
    counter = 0
    while (raw_data.lower() != 'no'):
        counter = counter + 5
        print(df.head(counter))
        raw_data = input(
            'Would you like to see more 5 more rows of the raw file? Yes or No\n').lower()
        print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_row_count(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
