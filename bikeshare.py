import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')

    print("Type C for Chicago, N for New York or W for Washington")
    while True :

        city_name = input("Please Enter The City Name You Want To Analyze: ").lower() 


        if city_name != "n" and city_name != "c" and city_name!= "w" : 

            print ("Wrong Input! Type C for Chicago, N for New York or W for Washington ")
            continue  
        
        if city_name == "c" : 
            city = CITY_DATA["chicago"] 
            break
        elif city_name == "n" : 
            city = CITY_DATA["new york city"]
            break
        elif city_name == "w" : 
            city = CITY_DATA["washington"]
            break 

    print("Type 1 to 12 to choose months where January is 1 and December is 12 or Type ALL to display for all months ")
    while True : 

        month_name = input("Which month do you want to see the data for : ").lower()

        if month_name !="1" and month_name!="2" and month_name!="3" and month_name!="4" and month_name!="5" and month_name!="6" and month_name!="7" and month_name!="8" and month_name!="9" and month_name!="10" and month_name!="11" and month_name!="12"  and month_name != "all": 
            print ("Wrong Input! Type 1 to 12 to choose months where January is 1 and December is 12 or Type ALL to display for all months")
            continue

        months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

        if month_name == "all" : 

            print ("No Filters Will Be Applied")
            month = "all"
            break

        else : 

            month = months[int(month_name)-1]
            break 

    print ("Type 1 to 7 to choose days where Monday is 1 and Sunday is 7 or Type ALL to display for all days")
    while True : 
        
        day_name = input("Which day do you want the data for : ").lower()

        if day_name !="1" and day_name!="2" and day_name!="3" and day_name!="4" and day_name!="5" and day_name!="6" and day_name!="7" and day_name!="all": 

            print ("Wrong Input! Type 1 to 7 to choose days where Sunday is 1 and Saturday is 7 or Type ALL to display for all days ")
            continue

        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

        if day_name!= "all" :
            day = days[int(day_name)-1]
            break

        elif day_name == "all" : 
            print("No Filters Will Be Applied")
            day = "all"
            break

    print('-'*40)    
    return (city,month,day)


def load_data(city, month, day):
    
    df = pd.read_csv(city)

    if month == "all" and day == "all" : 
        return df

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_the_week"] = df["Start Time"].dt.weekday
    
    if month!='all' :

        months = ["January","February","March","April","May",
        "June","July","August","September","October","November","December"]
        month= months.index(month) + 1 

        new_df = df[df["month"]==month]
    else : 
        new_df = df

    if day!="all" : 
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        day = days.index(day)+1
        new_df = new_df[df["day_of_the_week"]==day]


    return new_df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("Displaying the most popular month if you have chosen 'ALL' option for months : ")
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_the_week"] = df["Start Time"].dt.weekday

    if len(df["month"].unique()) < 2 : 
        print ("*"*40)
        print("Since you have filtered using one month,this does not apply")
        print ("*"*40)
    else : 
        popular_month = df["month"].mode()[0]
        months = ["January","February","March","April","May",
        "June","July","August","September","October","November","December"]
        popular_month= months[popular_month-1]
        print ("The most popular month is : ",popular_month)
     
    print("Displaying the most popular day of the week if you have chosen 'ALL' option for day  : ")   
    if len(df["day_of_the_week"].unique()) < 2 : 
        print ("*"*40)
        print("Since you have filtered using one week,this does not apply")
        print ("*"*40)

    else : 
        popular_day= df["day_of_the_week"].mode()[0]
        day= ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        popular_day= day[popular_day]
        print ("The most popular day of the week is :",popular_day)

    print("Displaying the most common hour : ")  
    extract_hours = df["Start Time"].dt.hour

    print ("Most common start hour is:",extract_hours.mode()[0],"o'clock")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used Start Station is :" ,df["Start Station"].mode()[0])

    # TO DO: display most commonly used end station
    print ("The most commonly used End Station is :",df["End Station"].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df["combination_of_start_and_end_stations"] = df["Start Station"] + " " + df["End Station"]
    print ("The most frquent combination of start station and end station:",df["combination_of_start_and_end_stations"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_travel= np.sum(df["Trip Duration"])
    print("The total travel time is :" , total_time_travel)

    # TO DO: display mean travel time
    mean_travel_time = np.mean(df["Trip Duration"])
    print("The mean travel time is:" , mean_travel_time) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of Subscribers : " , df["User Type"].value_counts()[0])
    print("Counts of Customers : " , df["User Type"].value_counts()[1])
    # TO DO: Display counts of gender
    if "Gender" in df.columns :

        print ("Counts of Men :", df["Gender"].value_counts()[0])
        print ("Counts of Woman :", df["Gender"].value_counts()[1])
    else : 
        print ("No information about Gender is found in this dataset")

    if "Birth Year" in df.columns: 

        print("Most common year of birth : " , df["Birth Year"].mode()[0])
        print("Earliest year of birth :" , df["Birth Year"].min())
        print("Most Recent year of birth:" , df["Birth Year"].max())
      # TO DO: Display earliest, most recent, and most common year of birth
    else : 

        print("No information about Birth Year is found in this dataset")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def do_you_want_to_see_raw_data():
    print('helloworld')

    print("Are you interested into looking at raw data") 
    while True : 
        answer = input("Please type Y for Yes and N for No").lower()

        if answer!="y" and answer!="n" :

            print("Wrong Input! Please type Y for Yes and N for No") 
            continue

        if answer == "y" :

            while True :

                print("Type C for Chicago, N for New York or W for Washington")

                city_name = input("Please Enter The City Name You Want To Analyze: ").lower() 


                if city_name != "n" and city_name != "c" and city_name!= "w" : 

                    print ("Wrong Input! Type C for Chicago, N for New York or W for Washington ")
                    continue  
        
                if city_name == "c" : 
                    city = CITY_DATA["chicago"]
                    for i in range(0,len(city),5) :
                        #yield (i)  
                        print(pd.read_csv(city).head(i))
                        print("Do you want more ?")
                        your_input = input("Yes or No").lower()

                        if your_input == "yes" :
                            continue 
                        elif your_input == "no" : 
                            break


            #elif city_name == "n" : 
             #   city = CITY_DATA["new york city"]
             #   print(pd.DataFrame.(city))
            #elif city_name == "w" : 
            #    city = CITY_DATA["washington"] 
             #   print(pd.DataFrame.(city))

    return 1

def main():
    while True:
        see_data = do_you_want_to_see_raw_data()
        break
        # print(see_data)

        # city, month, day = get_filters()
        # df = load_data(city, month, day)

        # print (df)
        # time_stats(df)
        # station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)

        # restart = input('\nWould you like to restart? Enter yes or no.\n')
        # if restart.lower() != 'yes':
        #     break
        
if __name__ == "__main__":
	main()
