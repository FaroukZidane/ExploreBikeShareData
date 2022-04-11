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
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    
    # Empty variable to store city name
    city = ''
    
    while city not in CITY_DATA.keys():
        print("\nPlease enter the city.")
        print("\nAvailable options are: ")
        print("1. Chicago   2. New York City    3. Waghington DC")
        print("\n(Type the city however you want, CAPS or lowercase)")
        
        city = input()
        city = city.lower()
        
        if city not in CITY_DATA.keys():
            print("\nInvalid input, please enter the city in a correct format.")
            print("\nRestarting...")
    
    # months data dictionary
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    # Empty variable to store month name
    month = ''
    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in MONTH_DATA.keys():
        print("\nPlease enter a specific month or enter \'all\' for all months.")
        print("\nAvailable options are: ")
        print('1. january, 2. february, 3. march, 4. april, 5. may, 6. june, 7. all')
        print('\n(Type the month however you want, CAPS or lowercase)')
                  
        month = input()
        month = month.lower()
                  
        if month not in MONTH_DATA.keys():
            print('\nInvalid input, please enter the month in a correct format.')
            print('\nRestarting...')
                  
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # day data dictionary
    DAY_DATA = {'monday': 1, 'teusday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7, 'all': 8}
    # Empty variable to store day name
    day = ''
    # TO DO: get user input for day (all, monday, teusday, ... , sunday)
    while day not in DAY_DATA.keys():
        print("\nPlease enter a specific day or enter \'all\' for all days.")
        print("\nAvailable options are: ")
        print('1. monday, 2. teusday, 3. wednesday, 4. thursday, 5. friday, 6. saturday, 7. sunday, 8. all')
        print("\n(Type the day however you want, CAPS or lowercase)")
                  
        day = input()
        day = day.lower()
                  
        if day not in DAY_DATA.keys():
            print("\nInvalid input, please enter the day in a correct format.")
            print("\nRestarting...")
                  
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
    
    # load csv file into the dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

        
    return df

                  
def time_stats(df):
    """
    Displays statistics on the most frequent time of travel.

    Args:
        (str) df - the required dataframe from which we need to display statistics.
        
    """
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("\nThe most common month is: ")
    print(df['month'].mode()[0])


    # TO DO: display the most common day of week
    print("\nThe most common day is: ")
    print(df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("\nThe most common start hour is: ")
    print(df['hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

                  
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nThe most commonly used start station is: ")
    print(df['Start Station'].mode()[0]) 

    # TO DO: display most commonly used end station
    print("\nThe most commonly used end station is: ")
    print(df['End Station'].mode()[0]) 
    
    # TO DO: display most frequent combination of start station and end station trip
    # Create a new column "Start to End" to combine start and end station
    # and perform the mode function on it to extract most frequent combination
    # of start station and end station trip
    df['Start to End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    
    print("\nThe most frequent combination of start station and end station trip is: ")
    print(df['Start to End'].mode()[0]) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

                  
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # trip duration in seconds
    trip_duration = df['Trip Duration'].sum()
    minutes, seconds = divmod(trip_duration, 60)
    hours, minutes = divmod(minutes, 60)
    print(f'\nTotal trip duration = {hours} hours, {minutes} minutes and {seconds} seconds')

    # TO DO: display mean travel time
    avg_trip_duration = df['Trip Duration'].mean()
    avg_minutes, avg_seconds = divmod(avg_trip_duration, 60)
    avg_hours, avg_minutes = divmod(avg_minutes, 60)
    print(f'\nAvreage trip duration = {avg_hours} hours, {avg_minutes} minutes and {avg_seconds} seconds')    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('\nThe user types for this city is the following: ')
    print(user_types)

    try:
        gender = df['Gender'].value_counts()
        print('\nThe gender types for this city is the following: ')
        print(gender)
    except:
        print('\nSorry, there is no gender information for this file.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f'\nThe earliest birth year is {earliest_year}, the most recent year is {most_recent_year} and the most common year is {most_common_year}.')
    except:
        print('\nSorry, no birth year information for this file.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    """
        Display first 5 rows of raw data after prompting the user.
        
        Args:
            df -- dataframe to display the rows from
        
        Returns:
            No returns
    """
    prompt_opts = ['yes', 'no']
    prompt = ''
    
    while prompt not in prompt_opts:
        print("\nWould you like to see 5 rows of raw data? 1. Yes   2. No")
        prompt = input()
        prompt = prompt.lower()
        
        if prompt not in prompt_opts:
            print('\nInvalid input format, please try again.')
            print('\nRestarting...')
    
    
    start_loc = 0
    while prompt != 'No'.lower():
        
        print(df.iloc[start_loc:start_loc+5])
        start_loc = start_loc + 5
        
        prompt = ''
        while prompt not in prompt_opts:
            print("\nWould you like to continue showing 5 rows of raw data? 1. Yes   2. No")
            prompt = input()
            prompt = prompt.lower()
            
            if prompt not in prompt_opts:
                print('\nInvalid input format, please try again.')
                print('\nRestarting...')
                
        
                
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart the program? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    