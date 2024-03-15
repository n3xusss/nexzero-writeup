import subprocess

questions_and_answers = [
    ("Q4: What is the ID of the last boot ?", "62c2a4fe86254123a4a73629ea60fee0"),
    ("Q5: How did he install google-chrome (full command) ?", "sudo dpkg -i google-chrome-stable_current_amd64.deb"),
    ("Q6: When exactly did he install google-chrome (YYYY-MM-DD_HH:MM:SS) ?", "2024-01-16_21:01:36"),
]

def run_netcat_session():
    for question, correct_answer in questions_and_answers:
        user_answer = input(f"{question}\n>> ").strip()
        if user_answer == correct_answer:
            print("Correct! Moving to the next question.\n")
        else:
            print("Incorrect. Exiting ...")
            return
    print("You have succefully answered all the questions. Here is your flag: \n\n")        
    print("nexus{w0w_1337_Certified_L1nuX_4n6_Ex4min3r###}")

if __name__ == "__main__":
    print("\n------------------------------------------------welcome to Manini-Case 2-----------------------------------------------------------\n\n *** NOTE: You have to answer all the questions with the specified format if required to get the flag at the end. ***\n\n")
    run_netcat_session()

