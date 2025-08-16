import os
from dotenv import load_dotenv
from openai import OpenAI

def get_personal_plan():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Error: API key not found. Check your .env file!")
        return

    client = OpenAI(api_key=api_key)

    # This is prompt but it prob can be a lot better not sure
    system_message = {
        "role": "system",
        "content": (
            "You are a Professional Personal Trainer AI. "
            "Your task is to design a comprehensive monthly fitness plan based on the user's input. "
            "The plan must include:\n"
            "- 8–10 varied exercises for each workout day\n"
            "- A progressive overload strategy, specifying sets and reps for each week\n"
            "- Cardio recommendations integrated into workout days\n"
            "- A concise monthly overview summarizing the workout schedule\n"
            "- A diet plan tailored to the user's fitness goals, including meal suggestions and macronutrient breakdown\n\n"
            "Ensure that each week increases in difficulty according to the user’s experience level, "
            "preferences, and available equipment, while also being mindful of any existing medical conditions or injuries. "
            "The plan must be comprehensive and user-friendly."
        )
    }

    # I found that this are the best questions to be asked and to use
    questions = [
        "Age",
        "Gender",
        "Weight",
        "Height",
        "Body Mass Index (BMI) (if available)",
        "Fitness Goal",
        "Workout Setting Preference (home, street, gym)",
        "Weekly Workout Days/Availability (name all days)",
        "Desired Duration of the Plan (weeks)",
        "Time of Day Preference",
        "Experience Level (1-10)",
        "Equipment Available",
        "Available Space",
        "Specific Areas to Focus On",
        "Preferred Workout Duration",
        "Intensity Level (for start)",
        "Preferred Exercise Types",
        "Exercises Enjoyed",
        "Exercises Disliked",
        "Previous Workout Programs",
        "Existing Medical Conditions or Injuries",
        "Current Medications Impacting Workouts",
        "Stress Levels (1-10)",
        "Sleep Duration and Quality",
        "Occupation or Daily Activities Impacting Workouts",
        "Current Diet Style",
        "Daily Caloric Intake Goal",
        "Macronutrient Distribution Preferences",
        "Dietary Restrictions or Preferences",
        "Cardio Preferences",
        "Desired Weekly Running Duration",
        "Any Upcoming Events Affecting Routine",
    ]

    conversation = [system_message]

    #This is to that user can respond then reapets but it is kinda taking to long need maybe to change it
    for question in questions:
        user_response = input(f"{question}? ")
        conversation.append({"role": "user", "content": f"{question}: {user_response}"})

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  #If you have better version then gg but if not its this and only this
        messages=conversation
    )
    # I didnt get to this part my api is shit for some reason
    ai_response = completion.choices[0].message.content
    print("\n===== Your Personalised Fitness Plan =====\n")
    print(ai_response)
    input("\nPress enter to close...")

if __name__ == "__main__":
    get_personal_plan()
