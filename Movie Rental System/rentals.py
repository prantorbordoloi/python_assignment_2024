rented_movie_list = {}

def rentMovie(m_list,m_name,cus):
    for mov in m_list:
        if mov[0] == m_name:
            if cus not in rented_movie_list:
                rented_movie_list[cus] = []
            rented_movie_list[cus].append(mov)
            print(f"{cus} rented the movie {m_name}")
        else:
            print(f"movie : {m_name} is not available for rent ...")


def displayRentedMovies():
    if rented_movie_list:
        print("displaying rented movies ....")
        for cus , movies in rented_movie_list.items():
            print(f"customers : {cus}")
            for mov in movies:
                print(f"title : {mov[0]} , genre : {mov[1]} , rent_price : {mov[2]}")
        # print(rented_movie_list)
    else:
        print("no movie rented...")