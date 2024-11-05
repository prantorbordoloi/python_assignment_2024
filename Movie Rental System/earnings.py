
def rentalEaring(rented_movie_list):
    total_earning = 0
    for movies in rented_movie_list.values():
        for mov in movies:
            total_earning += mov[2]
    print(f"total_earning : {total_earning}")
    