from basic_word import BasicWord
from player import Player
from utils import load_random_word


def main():

    print(f"Ввведите имя игрока")
    user_input = input()

    player = Player(user_input)
    print(f"Привет {user_input}")

    word, subwords = load_random_word()
    basic_word = BasicWord(word, subwords)
    word_count = basic_word.get_word_count()

    print(f"Составьте {word_count} слов из слова ПИТОН")
    print(f"Слова должны быть не короче 3 букв")

    print(f"Чтобы закончить игру, угадайте все слова или напишите stop")
    print(f"Поехали, ваше первое слово?")

    for i in range(word_count):

        user_input = input()

        if user_input in ["stop", "стоп"]:
            break

        is_used = player.was_used(user_input)
        is_subword = basic_word.has_subword(user_input)

        if not is_used and is_subword:
            print(f"верно")
            player.add_word(user_input)
        else:
            print(f"неверно")

    words_ok = player.get_word_count()

    print(f"слова закончились, игра завершена!")
    print(f"вы угадали {words_ok} слов")

main()
