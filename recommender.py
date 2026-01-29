# Simple Content-Based Recommendation System (Movies)

movies = {
    "Inception": ["sci-fi", "thriller"],
    "Interstellar": ["sci-fi", "drama"],
    "The Dark Knight": ["action", "thriller"],
    "Titanic": ["romance", "drama"],
    "Avengers": ["action", "sci-fi"],
    "Notebook": ["romance", "drama"],
    "Mad Max": ["action", "thriller"],
    "Gravity": ["sci-fi", "drama"]
}

def recommend_movies(user_preferences):
    recommendations = []

    for movie, genres in movies.items():
        score = 0
        for pref in user_preferences:
            if pref in genres:
                score += 1
        if score > 0:
            recommendations.append((movie, score))

    # Sort movies based on matching score
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations

def main():
    print("🎬 Movie Recommendation System")
    print("Available genres: action, sci-fi, drama, romance, thriller")
    
    user_input = input("Enter your preferred genres (comma separated): ")
    user_preferences = [genre.strip().lower() for genre in user_input.split(",")]

    results = recommend_movies(user_preferences)

    if results:
        print("\nRecommended Movies for You:")
        for movie, score in results:
            print(f"- {movie}")
    else:
        print("\nNo recommendations found.")

main()
