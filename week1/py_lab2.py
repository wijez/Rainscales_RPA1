import time

def generate_number():
    return int((time.time() * 1000) % 999) + 1

def get_user_guess():
    while True:
        try:
            guess = int(input("Nhập số bạn đoán (1–999): "))
            if 1 <= guess <= 999:
                return guess
            else:
                print("Số phải nằm trong khoảng từ 1 đến 999.")
        except:
            print("Vui lòng nhập một số nguyên hợp lệ.")

def main():
    print("🎮 Trò chơi đoán số (1–999)")
    number = generate_number()
    wrong_guesses = 0

    while True:
        guess = get_user_guess()

        if guess == number:
            print(f"Bạn đã dự đoán chính xác số {number}")
            break
        elif abs(guess - number) <= 10:
            print("Bạn đoán gần đúng rồi!")
        else:
            wrong_guesses += 1
            print(f"Sai rồi! Bạn đã trả lời sai {wrong_guesses} lần.")

        if wrong_guesses >= 5:
            number = generate_number()
            wrong_guesses = 0
            print("Bạn đoán trật tất cả năm lần, kết quả đã thay đổi. Mời bạn đoán lại.")

main()
