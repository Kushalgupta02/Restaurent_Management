from order import take_order, calculate_total           #it imports function from previus modules
import matplotlib.pyplot as plt
import numpy as np
def main():
    print("Welcome to our Sweet and Spicy Restaurent!")
    
    user_name=input("Enter your name:")      #user name will provide his/her name 
    print("Hello " + user_name + " Please select menu.")
    
    order = take_order()                 #to take order from user
    total = calculate_total(order)            
    print("Your order:")
    for item, quantity in order.items():
        print(f"{item}: {quantity}")
    print(f"Total amount to pay: ${total}")           #it will calculate the bill of user and provide
    review = input("Please provide a review of your experience (optional):")
    rating = input("Please rate your experience on a scale of 1-5 (optional):")
    feedback = input("Please provide any feedback or suggestions (optional):")
    with open('reviews.txt', 'a') as f:
        f.write(f"Name: {user_name}\n")
        f.write(f"Review: {review}\n")
        f.write(f"Rating: {rating}\n")
        f.write(f"Feedback: {feedback}\n")
        f.write("\n")
    ratings = [4, 5, 3, 5, 4, 5, 4, 5, 3, 4, 4, 5, 3]
    ratings.append(int(rating))
    
    x = np.arange(len(ratings))             # Create a curve graph of the ratings
    y = ratings
    plt.plot(x, y)
    
    plt.title('Ratings')                 # Set the title and labels of the chart
    plt.xlabel('Review Number')      # Set the title and labels of the chart
    plt.ylabel('Rating')            # Set the title and labels of the chart 
   
    plt.show()                    # Show the chart
    
    # print a confirmation message with the user's review, rating, and feedback
    print(f"Thank you for your review, {user_name}! Your rating was {rating} and your feedback was: {feedback}")
    
if __name__ == "__main__":           
    main()
    
#here we are asking name from user
#then we asking for their order
#Takes user orders
#Calculates the total amount to pay
#Collects user reviews and ratings
#Displays a curve graph of ratings
#take_order(): Takes user orders
#calculate_total(order): Calculates the total amount to pay
#main(): The main function that runs the application