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
    city= ['chicago', 'new york city', 'washington']
    name = input('what city would you like to dive into?:\n').lower()
    while True:
        if name in city:
            break
        else:
            input('please try again bud: \n')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    mont= input('specify a month between january and june or type all to apply no filter?:\n').lower()
    if mont not in month:
        print("you need to choose month between january and june")
    else:
        print('thanks!')

    # TO DO get user input for day of week (all, monday, tuesday, ... sunday)
    day = ['all','monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    weekday = input('please input day of the week or type all to apply no day filter:\n').lower()

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


    return df
df= pd.read_csv('washington.csv')

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df.loc[:,"month"].mode()[0]
    print("the most common month of travel is:", common_month)


    # TO DO: display the most common day of week
    df['day_of_week']=df['Start Time'].dt.weekday
    common_day= df.loc[:,"day_of_week"].mode()[0]
    print("the day on which trips were most frequently made:", common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df.loc[:,"hour"].mode()[0]
    print("the most frequent hour of travel was:", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    busiest_start_station = df['Start Station'].value_counts().idxmax()
    print('the busiest Start Station was:', busiest_start_station)


    # TO DO: display most commonly used end station
    busiest_end_station = df['End Station'].value_counts().idxmax()
    print('the busiest End Station was:', busiest_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combo_station =df[['Start Station', 'End Station']].mode().loc[0]
    print("the most frequent combo of two stations was: {} start, {} end".format(most_frequent_combo_station[0], most_frequent_combo_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("the total time travelled was:", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration'].sum()/df['Trip Duration'].count())
    print("Mean travel time was:", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types =df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)


    else:
        print('Gender column not included in this Data Base')


    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' not in df.columns:
        print('Birth Year not included in this Data base')
    else:
        earliest_birth = df['Birth Year'].min()
        latest_birth = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('The earliest birth year was:', earliest_birth)
        print('The most recent Birth Year was:', latest_birth)
        print('The most common year of birth was:',most_common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    row_num = 0
    raw_data = input('Would you like to view the raw data ? Enter yes or no.\n')
    while True:
        if raw_data.lower() =='yes':
            raw_data_splice = df.iloc[row_num : row_num + 5]
            print(raw_data_splice)
            row_num += 5
            raw_data = input('Would you like to see more data? Enter yes or no.\n')
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



# Note that i consulted the Pandas library: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html for concepts which were unclear
