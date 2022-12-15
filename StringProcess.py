import re

eng_dict =  {
    ' one ': '1',
    ' two ': '2',
    ' three ': '3',
    ' four ': '4',
    ' five ': '5',
    ' six ': '6',
    ' seven ': '7',
    ' eight ': '8',
    ' nine ': '9',
    ' ten ': '10',
    ' zero ': '0',
}
error_code_eng = {
    -1: 'Sorry, maybe you have entered to few number of digits. Please try again',
    -2: 'Sorry, maybe you have entered to many number of digits. Please try again',
}
error_code_vie = {
    -1: 'Xin lỗi, bạn có thể đã đưa vào quá ít số. Vui lòng thử lại',
    -2: 'Xin lỗi, bạn có thể đã đưa vào quá nhiều số. Vui lòng thử lại',
}


def no_accent_vietnamese(s):
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    return s

def ConnectProcess(str, lang):
    if (lang == 'vi-VN'):
        str= no_accent_vietnamese(str)
    str = re.sub(r'[^a-zA-Z0-9]', ' ', str).lower()
    str = str.replace('  ', ' ')
    print(str)
    for key in eng_dict:
        str = str.replace(key, eng_dict[key])
    print(str)
    num = re.findall(r'\d+', str)
    print(num)
    if (len(num) < 2 ):
        if (lang == 'vi-VN'):
            return error_code_vie[-1],-1,-1
        return error_code_eng[-1],-1,-1
    if (len(num) > 2 ):
        if (lang == 'vi-VN'):
            return error_code_vie[-2],-2,-2
        return error_code_eng[-2],-2,-2 
    return num[0], num[1],0