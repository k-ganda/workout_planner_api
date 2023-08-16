import requests


def get_valid_input(prompt, options):
    while True:
        choice = input(f"{prompt} ({'/'.join(options)}): ").lower()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please choose a valid option.")


def main():
    url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"

    time = input("Enter duration of workout (in minutes): ")

    equipment_options = ["yes", "no"]
    equipment = get_valid_input("Do you have any equipment?", equipment_options)

    muscle_options = ["legs", "chest", "back", "none"]
    muscle = get_valid_input(
        "Which muscle group would you like to focus on?", muscle_options
    )

    fitness_level_options = ["beginner", "intermediate", "advanced"]
    fitness_level = get_valid_input("Choose your fitness level", fitness_level_options)

    fitness_goals_options = [
        "weight_loss",
        "muscle_gain",
        "strength_training",
        "cardiovascular_endurance",
        "flexibility",
        "general_fitness",
    ]
    fitness_goals = get_valid_input(
        "What are your fitness goals?", fitness_goals_options
    )

    querystring = {
        "time": time,
        "equipment": equipment,
        "muscle": muscle,
        "fitness_level": fitness_level,
        "fitness_goals": fitness_goals,
    }

    headers = {
        "X-RapidAPI-Key": "c2e3fe64a2msh77c749c5e8811acp1df9c3jsn291fdd37d9df",
        "X-RapidAPI-Host": "workout-planner1.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    print(data)


if __name__ == "__main__":
    main()
