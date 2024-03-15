import subprocess

questions_and_answers = [
    ("Q7: Which interesting website does he usually visit ?", "freepalestine-foundation.dz"),
    ("Q8: What is the UUID of the main root volume ?", "a3389150-6669-478a-8bfb-059dd1718175"),
    ("Q9: The user is suspected that he was hiding a secret in a non-casual place, can you recover his ultimate secret ?", "FreePalestine")
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
    print("nexus{w0w_1337_Certified_L1nuX_4n6_ExP3r7!!!}")

if __name__ == "__main__":
    print("\n------------------------------------------------welcome to Manini-Case 3-----------------------------------------------------------\n\n *** NOTE: You have to answer all the questions with the specified format if required to get the flag at the end. ***\n\n")
    run_netcat_session()

