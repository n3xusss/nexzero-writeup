import subprocess

questions_and_answers = [
    ("Q1: What is the sha1 hash of the Disk image (Google, don't hurry) ?", "312fcd401047b7767a7410ce2464ad5a8af346b2"),
    ("Q2: What is the user's computer name ?", "manini-desktop"),
    ("Q3: What is the login password of this user ?", "2024"),
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
    print("nexus{w0w_1337_Certified_L1nuX_4n6_Pr4cti710n3r$$$}")

if __name__ == "__main__":
    print("\n------------------------------------------------welcome to Manini-Case 1-----------------------------------------------------------\n\n *** NOTE: You have to answer all the questions with the specified format if required to get the flag at the end. ***\n\n")
    run_netcat_session()

