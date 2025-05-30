import math

def is_perfect_square(n):
    return int(math.sqrt(n)) ** 2 == n

def get_valid_integer(x):
    while True:
        try:
            value = int(input(x))
            return value
        except:
            print("Vui lòng nhập một số nguyên hợp lệ.")

def main():
    print("Tìm các số chia hết cho 3 nhưng không phải số chính phương")

    # Nhập và kiểm tra dữ liệu
    while True:
        a = get_valid_integer("Nhập số nguyên a: ")
        b = get_valid_integer("Nhập số nguyên b: ")
        if a < b:
            break
        else:
            print("a phải nhỏ hơn b. Vui lòng nhập lại.")

    result = []
    for i in range(a, b + 1):
        if i % 3 == 0 and not is_perfect_square(i):
            result.append(str(i))

    print("Kết quả:", ",".join(result))

main()
