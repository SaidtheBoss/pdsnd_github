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
    while True:
        city = input('please enter the city:')
        city = city.lower()
        if city in CITY_DATA:
            break
        else: 
            print('sorry the city is not available or the input is invalid')
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        int_month = input('please enter the month or enter zero for all:')
        try:
            month = int(int_month)
            if month <= 12 and month > -1:
                break
            else:
                print('please enter a valid month')
        except:
            print("please enter the month as a number EX jan = 1;")              
     
    while True:
        int_day = input('please enter the day or enter zero for all:')
        try:
            day = int(int_day)
            if day <= 7 :
                break
            else:
                print('please enter a valid day')
        except:
            print("please enter the day as a number EX sun = 1;") 
    print('thanks')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
     ask = ''
     df = pd.read_csv(CITY_DATA[city])
     df['Start Time'] = pd.to_datetime(df['Start Time'])
     if month != 0:
        df = df[df['Start Time'].dt.month == month]
     if day != 0:
        df = df[df['Start Time'].dt.day == day]  
     while True:
         ask = input('do you want to see the data in rows of 5 ? \n yes/no ?:')
         ask = ask.lower()
         if(ask == 'yes' or ask == 'no'):
             break
         else:
             print('please state in \'yes\' or \'no\'')
     
    
     if(ask == 'yes'):
         dfview = pd.DataFrame(df)
         while True:
                print(dfview.head(5))
                dfview = dfview.tail(len(dfview) - 5)
                ask =''
                while True:
                     ask = input('would you like to continue to see row data? \n state in \'yes\' or \'no\':')
                     ask = ask.lower()
                     if(ask == 'yes' or ask == 'no'):
                         if(ask == 'yes'):
                            break
                         else:
                            return df
                     else:
                         print('please state in \'yes\' or \'no\'')
     else:
        print(df)

               
     return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month:',(df['Start Time'].dt.month).mode()[0])

    # TO DO: display the most common day of week
    print('the most common day:',(df['Start Time'].dt.day).mode()[0])

    # TO DO: display the most common start hour
    print('the most common hour:',(df['Start Time'].dt.hour).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('most common start' ,df['Start Station'].mode()[0])
    
     

    # TO DO: display most commonly used end station
    print('most common end' ,df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = 'start: ' + df['Start Station'] + ' end: '  + df['End Station']
    print(df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean of travel times',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('the counts of user types')
    print(df['User Type'].value_counts())

    
    # TO DO: Display counts of gender
    if 'Gender' in df:
    # TO DO: Display counts of gender
        print('the counts of gender')
        print(df['Gender'].value_counts())
    else:
        print('sorry the coloumn \'Gender\' does not exist to calculate')
    # TO DO: Display earliest, most recent, and most common year of birth
   
    if 'Birth Year' in df:
        print("earliest birth", df['Birth Year'].min())      
        print("latest birth", df['Birth Year'].max())
        print('most common birth year' ,df['Birth Year'].mode()[0])
    else:
        print('sorry the coloumn \'Birth Year\' does not exist to calculate')    
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
