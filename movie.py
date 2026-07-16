 #create a hangman game

import random
MOVIES = ["Avatar", "Manichitrathazhu", "Spadikam", "Kilukkam", "Inside Out","Kireedam","Devasuram","Godfather","Titanic","Barbie",
          "Spider Man","Iron Man","Jurassic Park","The Avengers","Jurassic World","Master","Ramji Rao Speaking","Amaram","Commissioner","Narasimham",
          "Chithram","Classmates","Ustad Hotel","Bangalore Days","Premam","Charlie","Kammatipaadam","Take Off","Angamaly Diaries","Ezra",
          "Parava","Sudani from Nigeria","Koode","Joseph","Varathan","Kumbalangi Nights","Virus","Uyare","Helen","Jallikattu",
          "Ayyappanum Koshiyum","The Great Indian Kitchen","Nayattu","Joji","Malik","Minnal Murali","Home","Hridayam","Bheeshma Parvam","Jana Gana Mana",
          "Nna Thaan Case Kodu","Romancham","2018","Kannur Squad","Neru","Aavesham","Bramayugam","Manjummel Boys","Premalu","Aadu",
          "Lucifer","CIA","Jacobinte Swargarajyam","Drishyam","Memories","Iyobinte Pusthakam","Ennu Ninte Moideen","Oru Vadakkan Selfie","Two Countries","Mollywood Times",
          "Pulimurugan","Oppam","Munthirivallikal Thalirkkumbol","Captain","Love Action Drama","Forensic","Operation Java","Kurup","Pada","Saudi Vellakka",
          "Falimy","Ozler","Golam","ARM","Psycho","Batman","Skyfall","Platoon","Marco","The Wild Robot",
          "Sinners","How to Train Your Dragon","Officer on Duty","Thudarum","Alappuzha Gymkhana","Kishkindha Kaandam","Deadpool & Wolverine","Nayakan ","Anbe Sivam","Asuran"]

movie = random.choice(MOVIES)
guessed_letters = set()
letter_strikes = 0
movie_strikes = 0

print(" Movie Hangman! ")
print("Type 1 letter to guess a letter (Max 5 wrong).")
print("Type the whole title to solve (Max 2 wrong).")

while letter_strikes < 5 and movie_strikes < 2:
    display = [
        char if (char.lower() in guessed_letters or char == " ") else "_"
        for char in movie
    ]
    print(f"\nMovie: {' '.join(display)}")
    print(
        f"Wrong letters: {letter_strikes}/5 | Wrong movie guesses: {movie_strikes}/2"
    )

    if "_" not in display:
        print(f" You won! The movie was: {movie}")
        break

    guess = input("Enter your guess: ").strip()

    if not guess:
        continue

    if len(guess) > 1:
        if guess.lower() == movie.lower():
            print(f" Correct! The movie was: {movie}")
            break
        else:
            print(" Wrong movie guess!")
            movie_strikes += 1
    else:
        guess = guess.lower()
        if guess in guessed_letters:
            print(" You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in movie.lower():
            print(" Correct letter!")
        else:
            print(" Wrong letter!")
            letter_strikes += 1
else:
    print(f"\n Game over! The movie was: {movie}")