import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('airbnb_listings.csv')

def top_rated_airbnbs(num=10, min_nights=8, instant_bookable=True):
    
    
    filtered_data = data[(data['minimum_nights'] >= min_nights) & (data['instant_bookable'] == instant_bookable)]

   
    top_listings = filtered_data.nlargest(num, 'review_scores_rating')

    return top_listings

def plot_response_rate_vs_time():
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='host_response_time', y='host_response_rate', data=data)
    plt.title('Host Response Rate vs. Response Time')
    plt.xlabel('Host Response Time')
    plt.ylabel('Host Response Rate')
    plt.show()

def airbnbs_in_dublin(cleanliness_threshold=4.0):
    
    dublin_listings = data[data['neighbourhood'] == 'Dublin']
    high_cleanliness_listings = dublin_listings[dublin_listings['review_scores_cleanliness'] > cleanliness_threshold]
    return len(high_cleanliness_listings)

def cleanliness_scores_for_listings(start, end):
    
    selected_listings = data.iloc[start-1:end]
    return selected_listings[['id', 'review_scores_cleanliness']]

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Top Rated Airbnbs")
        print("2. Plot Response Rate vs. Time")
        print("3. Airbnbs in Dublin with High Cleanliness Rating")
        print("4. Cleanliness Scores for Listings 12-15")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            top_listings = top_rated_airbnbs()
            print(top_listings)

        elif choice == '2':
            plot_response_rate_vs_time()

        elif choice == '3':
            cleanliness_threshold = float(input("Enter the cleanliness threshold: "))
            count = airbnbs_in_dublin(cleanliness_threshold)
            print(f"Number of Airbnbs in Dublin with cleanliness > {cleanliness_threshold}: {count}")

        elif choice == '4':
            cleanliness_scores = cleanliness_scores_for_listings(12, 15)
            print(cleanliness_scores)

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")