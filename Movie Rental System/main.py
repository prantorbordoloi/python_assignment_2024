import catalog
import rentals 
import earnings


while True:
    print("1.add a movie ")
    print("2.Rent a movie ")
    print("3.display available movies ")
    print("4.display rented movies ")
    print("5.display earnings")
    print("6.exit")
    choice = int(input("enter your choice : "))

    if choice ==1:
        title = input("enter the title of the movie : ")
        genre = input("enter the genre of the movie : ")
        price = float(input("enter the price of the movie : "))
        catalog.addMovie(title,genre,price)
    
    elif choice ==2:
        customer = input("name of the customer :")
        title = input("enter the movie title :")
        rentals.rentMovie(catalog.m_list,title,customer)
    
    elif choice ==3:
        print("displaying the available movies : ")
        catalog.availableMovies()
    
    elif choice == 4 :
        print("displaying the rented movies : ")
        rentals.displayRentedMovies()
    
    elif choice ==5:
        print("displaying the total earinings : ")
        earnings.rentalEaring(rentals.rented_movie_list)
    elif choice ==6:
        print("Exit...")
        break
    else:
        print("invalid input .....")
 
# catalog.addMovie("avatar","action",120)
# catalog.addMovie("uri","action",120)
# catalog.availableMovies()
# # addUser(u_details,"Prantor")
# # addUser(u_details,"John")
# rentals.rentMovie(catalog.m_list,"avatar","Prantor")
# rentals.rentMovie(catalog.m_list,"uri","Prantor")
# rentals.displayRentedMovies()
# earnings.rentalEaring(rentals.rented_movie_list)