import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_city = False
    while not valid_city:
        city = input('Please choose between one of the following cities: new york city, chicago and washington.\n')
        city_lower = city.lower()
        if city_lower in CITY_DATA:
            valid_city = True
        else:
            print('Oops, this is not a valid input. Please try again with one of the cities listed.\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    valid_month = False
    while not valid_month:
        month = input('For which of the months from January to June would you like to see data? If you would like to see data for all months, enter "all".\n')
        months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
        month_lower = month.lower()
        if month_lower in months:
            valid_month = True
        else:
            print('Oops, this is not a valid input. Please try again by entering one of the months listed above or "all".\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_day = False
    while not valid_day:
        day = input('For which weekday would you like to see data? If you would like to see data for all days, enter "all".\n')
        days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all')
        day_lower = day.lower()
        if day_lower in days:
            valid_day = True
        else:
            print('Oops, this is not a valid input. Please try again by entering a weekday or "all".\n')

    print('-'*40)
    return city_lower, month_lower, day_lower


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
    
    filename = CITY_DATA.get(city)
    df = pd.read_csv(filename)
    
    # get month and weekday data
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    
    #filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    # filter by weekday
    if day!= 'all':
        df = df[df['weekday'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month_name()
    #print(df['month'].unique())
    popular_month = df['month'].mode()[0]
    print('Most common month of travel is: ', popular_month)


    # TO DO: display the most common day of week
    df['weekday'] = df['Start Time'].dt.weekday_name
    popular_weekday = df['weekday'].mode()[0]
    print('Most common weekday of travel is: ', popular_weekday)

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['start_hour'].mode()[0]
    print('Most common hour to start travel is: ', popular_start_hour)
    print('\n')     
    
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most common station to start travel: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most common station to end travel: ', popular_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df_stations = pd.DataFrame(df, columns = ['Start Station', 'End Station'])
    stations_variable = df_stations.groupby('Start Station')['End Station'].value_counts().idxmax()
    print(f"The most common start station is {stations_variable[0]} and the most common end station is {stations_variable[1]}.")
    print('\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Trip Duration is measured in seconds (from diff(Start, End))
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time in seconds is: ', total_travel_time.astype(int))
    print('The total travel time in minutes is: ', int(total_travel_time//60))
    print('The total travel time in hours is: ', int(total_travel_time//3600))
    print('The total travel time in days is: ', int(total_travel_time//86400))
    print('\n')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time in minutes is: ', int(mean_travel_time//60))
    print('\n')
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    user_types_percentage = df['User Type'].value_counts(normalize = True).round(decimals = 5)
    user_types_percentage *= 100
    print('The count of users by type is:\n', user_types)
    print('The user type percentage of the total is:\n', user_types_percentage)
    print('\n')   
    
    try:
        # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        gender_count_percentage = df['Gender'].value_counts(normalize = True).round(decimals = 5)
        gender_count_percentage *= 100
        print('The count of each gender is:\n', gender_count)
        print('The percentage of each gender is:\n', gender_count_percentage)
        print('\n')

        # TO DO: Display earliest, most recent, and most common year of birth
        min_birth_year = df['Birth Year'].min().astype(int)
        print('The earliest birth year is: ', min_birth_year)

        max_birth_year = df['Birth Year'].max().astype(int)
        print('The most recent birth year is: ', max_birth_year)

        common_birth_year = df['Birth Year'].mode()[0].astype(int)
        print('The most common birth year is: ', common_birth_year)
        
    except Exception as e:
        print('Sorry, birth year and gender data is not available for the city you\'ve selected.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(df):
    raw_data_prompt = input('Would you like to see the first 5 rows of raw data for the city you\'ve selected? Enter "yes" or "no".\n')
    start_row = 0
    end_row = start_row + 5
    #Enter or exit raw data dispaly
    while raw_data_prompt.lower() == 'yes':
        raw_data = df.iloc[start_row:end_row]
        print(raw_data)
        start_row += 5
        end_row += 5
        raw_data_prompt = input('Would you like to see the next 5 rows of raw data?\n')

        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


    #Adding line for Section IV refactoring