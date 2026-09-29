import random

questions = [
    {
        "question": "What is the capital of Nigeria?", 
        "options": ["Lagos", "Abuja", "Kano", "Port Harcourt"],
        "answer": "Abuja"   
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Saturn", "Mars"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "O2", "CO2", "NaCl"],
        "answer": "H2O"
    },
    {
        "question": "Who was the first person to walk on the moon?",
        "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"],
        "answer": "Neil Armstrong"  
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yen", "Dollar", "Euro", "Pound"],
        "answer": "Yen"
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["Sahara Desert", "Gobi Desert", "Kalahari Desert", "Antarctic Desert"],
        "answer": "Antarctic Desert"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
        "answer": "Mount Everest"
    },
    {
        "question": "What is the largest country in the world by land area?",
        "options": ["Russia", "Canada", "China", "United States"],
        "answer": "Russia"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": "Blue Whale"
    },
    {
        "question": "what is the country with the largest population in Africa?",
        "options": ["Nigeria", "Egypt", "South Africa", "Ethiopia"],
        "answer": "Nigeria"
    },
    {
        "question": "What is the largest island in the world?",
        "options": ["Greenland", "Australia", "New Guinea", "Borneo"],
        "answer": "Greenland"
    },
    {
        "question": "What is the largest continent in the world?",
        "options": ["Asia", "Africa", "North America", "Europe"],
        "answer": "Asia"
    },
    {
        "question": "What is the largest river in the world by volume?",
        "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
        "answer": "Amazon River"
    },
    {
        "question": "What is the largest volcano in the world?",
        "options": ["Mauna Loa", "Mount St. Helens", "Mount Vesuvius", "Mount Fuji"],
        "answer": "Mauna Loa"
    },
    {
        "question": "What is the largest lake in the world by surface area?",
        "options": ["Caspian Sea", "Lake Superior", "Lake Victoria", "Lake Huron"],
        "answer": "Caspian Sea"
    },
    {
        "question": "What is the largest city in the world by population?",
        "options": ["Tokyo", "Shanghai", "Delhi", "New York City"],
        "answer": "Tokyo"
    },
    {
        "question": "What is the largest desert in Africa?",
        "options": ["Sahara Desert", "Kalahari Desert", "Namib Desert", "Gobi Desert"],
        "answer": "Sahara Desert"   
    },
    {
        "question": "What is the largest waterfall in the world?", 
        "options": ["Victoria Falls", "Niagara Falls", "Angel Falls", "Iguazu Falls"],
        "answer": "Angel Falls"
    }

]

letters = ["A", "B", "C", "D"]

def ask_question(question):
    print(question["question"])
    

    for index, option in enumerate(question["options"]):
        letter = letters[index]
        print(f"{letter}. {option}")

    while True:
        answer = input("Your answer: ").upper().strip()
        # print(f"DEBUG: {answer}")

        if answer not in letters:
            print("Invalid answer. please choose A, B, C, D.")
            continue

        selected_option = question["options"][letters.index(answer)]
    
        if selected_option == question["answer"]:
            print("Correct!")
            return True
        else:
            print("Incorrect!") 
            print(f"Correct answer: {question['answer']}")
            return False    



def play_game(questions, questions_per_game):
    selected_questions = random.sample(questions, questions_per_game)  # Select the specified number of random questions from the list  

    score = 0
    total_questions = len(selected_questions)

    print("-----------------------------")

    for question in selected_questions:
        random.shuffle(question["options"])
        result = ask_question(question)
        print("-----------------------------")    
    
        if result:
            score += 1
    
    percentage = (score / total_questions) * 100
            
    
    
    # print("-----------------------------")
    print(f"Your final score: {score}/{total_questions}")

    print(f"Percentage: {percentage}%")
    print("-----------------------------")
    return score, percentage

def main():
    while True:

        while True:
            try:
                questions_per_game = int(input(f"Enter the number of questions you want to answer (1-{len(questions)}): "))
            
                if questions_per_game < 1 or questions_per_game > len(questions):
                    print(f"Please enter a number between 1 and {len(questions)}.")
                    continue
            
                break
            except ValueError:
                print("Please enter a number.")
            
        score, percentage = play_game(questions, questions_per_game)

        while True:

            play_again = input("Play again? (Y/N): ").upper()

            if play_again not in ["Y", "N"]:
                print("Please enter Y or N.")
                continue

            break

        if play_again == "N":
            break 

    print("Thank you for playing!")

main()              






    
        
