# đổi các từ ở đầu câu sang chữ hoa và những từ không phải đầu câu sang chữ thường.
def _captialize(text):
    words = text.split()
    for i, word in enumerate(words):
        words[i] = word[0].upper() + word[1:].lower()
    return ' '.join(words)


# đảo ngược thứ tự các từ có trong chuỗi.
def _reverse(text):
    return ' '.join(text.split()[::-1])


#  tìm kiếm ký tự xuất hiện nhiều nhất trong chuỗi.
def _most_appeared(text):
    for char in text:
        if text.count(char) == max([text.count(c) for c in text]):
            return char


# nhập một chuỗi bất kỳ, liệt kê số lần xuất hiện của mỗi ký tự.
def _count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# kiểm tra xem trong chuỗi có ký tự số hay không. Nếu có, tách các số đó ra thành một mảng riêng.
def _extract_numbers(text):
    return [char for char in text if char.isdigit()]

# cắt chuỗi họ tên thành chuỗi họ lót và chuỗi tên.
def _split_name(full_name):
    parts = full_name.split()
    if len(parts) < 2:
        return full_name, ''
    return ' '.join(parts[:-1]), parts[-1]


# chuyển ký tự đầu tiên của mỗi từ trong chuỗi thành chữ in hoa.
def _captialize_upper(text):
    words = text.split()
    for i, word in enumerate(words):
        words[i] = word[0].upper() + word[1:]
    return ' '.join(words)


# đổi chữ xen kẽ: một chữ hoa và một chữ thường.
def _alternate_case(text):
    result = []
    for i, char in enumerate(text):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    return ''.join(result)


# nhập vào một chuỗi ký tự, kiểm tra xem chuỗi đó có đối xứng không.
def _is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

# nhập vào một số có 3 chữ số, xuất ra dòng chữ mô tả giá trị con số đó.
def _describe_number(num):
    if not (100 <= num <= 999):
        return "Số không hợp lệ, vui lòng nhập số có 3 chữ số."
    
    units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["", "mười", "hai mươi", "ba mươi"]
    
    hundreds_digit = num // 100
    tens_digit = (num // 10) % 10
    units_digit = num % 10
    
    description = []
    
    if hundreds_digit > 0:
        description.append(units[hundreds_digit] + " trăm")
    
    if tens_digit > 0:
        description.append(tens[tens_digit])
    
    if units_digit > 0:
        description.append(units[units_digit])
    
    return ' '.join(description).strip()


