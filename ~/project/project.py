import random
from colorama import Fore

def main():

    words_list=load_words_list("wordle_words.txt")
    selected=random.choice(words_list).strip()
    typed_words=["- - - - - ","- - - - - ","- - - - - ","- - - - - ","- - - - - ","- - - - - "]
    win=False
    i=0
    print(selected)
    while(i<6):
        check=False

        while(check==False):
            draw_border(typed_words)
            word=str(input("Type: ")).lower().strip()
            if len(word)==5:
                if word in words_list:
                    check=True
                else: print("Invalid word") 
            else: print("Typed word should have 5 letters")

        typed_words=adding_word(typed_words,word,selected,i)

        if word==selected:
            win=True
            draw_border(typed_words)
            print(Fore.GREEN+"CONGRATULATION YOU WIN!!!"+Fore.RESET)
            break

        i+=1
    
    if not win:
        draw_border(typed_words)
        print(Fore.RED+f"You lose!"+Fore.RESET)
        print(f"The selected word was: {selected}")
        
def load_words_list(words):

    words_list=[]
    with open(words) as file:
        for word in file:
            words_list.append(word.strip())
    return words_list


def draw_border(typed_words):

    top_border = "┌" + "─" * 11 + "┐"
    bottom_border = "└" + "─" * 11 + "┘"
    print(top_border)

    for word in typed_words:
        print("| "+ word +"|")
    
    print(bottom_border)


def adding_word(typed_words,word,selected,i):
    current_word=""

    for j in range(len(word)):
        if word[j] in selected:
            if word[j]==selected[j]: 
                current_word+=Fore.GREEN+word[j].upper()+" "+Fore.RESET
            else: 
                current_word+=Fore.YELLOW+word[j].upper()+" "+Fore.RESET
        else: 
            current_word+=word[j].upper()+" "
    
    typed_words[i] = current_word
    return typed_words

if __name__=="__main__":
    main()