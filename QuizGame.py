import csv
import random
import sys

def quiz_game():
    correct_ans = 0
    que = 10
    
    class quiz:
        questions = []
        
        def __init__(self, question, option1, option2, option3, option4, cor_option):
            self.que = question
            self.opt1 = option1
            self.opt2 = option2
            self.opt3 = option3
            self.opt4 = option4
            self.corr = cor_option
        
        def rules(self):
            print("\nHello! Welcome to the quiz game!\n\nRules:")
            print("\n1. You\'ll be given questions with four options: 1,2,3,4\n2. You need to select the correct option.\n3. If your answer is correct, you\'ll get one point, otherwise, the correct answer will be displayed.\n4. There will be exactly 10 questions.\n5. Choose 'q' as a choice if you want to quit in the middle.")
        
        @classmethod
        def instantiate_from_csv(cls):
            with open('QuizGamecsv.csv', 'r') as f:
                reader = csv.DictReader(f)
                tot_que = list(reader)
            for ques in tot_que:
                cls.questions.append(quiz(
                    question=ques.get('Question'),
                    option1=ques.get('Option1'),
                    option2=ques.get('Option2'),
                    option3=ques.get('Option3'),
                    option4=ques.get('Option4'),
                    cor_option=int(ques.get('Correct_Ans'))
                )) 
            return tot_que
        
        def main_quiz(self, tot_que):
            nonlocal correct_ans
            nonlocal que
            i = 1
            j = 0
            que_asked = [False] * len(tot_que)
            while i <= que:
                j = random.randrange(0, len(tot_que))
                if que_asked[j]:
                    continue
                else: 
                    i += 1 
                    que_asked[j] = True
                    print(f"\nYour question is: \n{tot_que[j].get('Question')} \nOption1: {tot_que[j].get('Option1')} \nOption2: {tot_que[j].get('Option2')} \nOption3: {tot_que[j].get('Option3')} \nOption4: {tot_que[j].get('Option4')}\n")
                    
                    choice = 0
                    while choice not in [1, 2, 3, 4, "q", "Q"]:
                        try: 
                            choice = input("What is your choice?\n")
                            if choice in ["q", "Q"]:
                                print("You Quit. \nThank you for playing.")
                                return self.results()
                            choice = int(choice)
                            if choice not in [1, 2, 3, 4]:
                                print("Invalid choice")
                            elif choice == int(tot_que[j].get('Correct_Ans')):
                                print("🎉 Correct answer!")
                                correct_ans += 1
                                break
                            else:
                                print(f"❌ Wrong! The correct answer is option: {tot_que[j].get('Correct_Ans')}") 
                                break
                        except: 
                            print("⚠️ Enter a number only!")
        
        def results(self):
            print(f"Your final score is {correct_ans} out of {que} 📝")
            return correct_ans
    
    tot_que = quiz.instantiate_from_csv()
    q_instance = quiz("", "", "", "", "", 0)
    q_instance.rules()
    q_instance.main_quiz(tot_que)
    return q_instance.results()

if __name__ == "__main__":
    score = quiz_game()
