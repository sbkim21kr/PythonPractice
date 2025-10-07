from datetime import datetime, date, timedelta
import calendar # 요일 이름을 얻는 다른 방법 제공 (하지만 weekday() + list가 더 직관적일 수 있음)

def get_age(birth_date: date) -> int:
    """주어진 생년월일(date 객체)로부터 만 나이를 계산합니다."""
    today = datetime.now().date()
    # 생일이 아직 안 지났으면 (month, day) 튜플 비교
    birthday_passed = (today.month, today.day) >= (birth_date.month, birth_date.day)
    age = today.year - birth_date.year - (0 if birthday_passed else 1)
    return age

def get_weekday_name(date_obj: date, lang='ko') -> str:
    """주어진 날짜 객체의 요일 이름을 반환합니다. (기본: 한국어)"""
    # date_obj.weekday()는 월요일=0, 화요일=1, ..., 일요일=6 을 반환
    weekdays_ko = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    weekdays_en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    weekday_index = date_obj.weekday()
    
    if lang == 'ko':
        return weekdays_ko[weekday_index]
    else: # 기본값 또는 'en'이면 영어 반환
        return weekdays_en[weekday_index]

def is_business_day(date_obj: date) -> bool:
    """주어진 날짜가 주말(토, 일)이 아닌지 확인합니다."""
    # weekday()는 월요일=0, ..., 토요일=5, 일요일=6
    return date_obj.weekday() < 5 # 0, 1, 2, 3, 4 (월~금) 이면 True

def add_business_days(start_date: date, days_to_add: int) -> date:
    """시작 날짜부터 지정된 'days_to_add' 만큼의 영업일을 더한 날짜를 반환합니다."""
    current_date = start_date
    added_days = 0
    while added_days < days_to_add:
        current_date += timedelta(days=1)
        if is_business_day(current_date):
            added_days += 1
    return current_date

# 사용 예시
birth = date(1995, 5, 15)
print(f"생년월일 {birth} 기준 나이: {get_age(birth)}세")

today_date = datetime.now().date()
print(f"오늘({today_date})은 {get_weekday_name(today_date)}입니다.")
print(f"오늘은 영업일인가? {is_business_day(today_date)}")

# 다음 주 월요일(영업일)까지 5일 더하기
next_monday = date(2023, 10, 30) # 예시 날짜 (월요일)
target_date = add_business_days(next_monday, 5) # 다음 주 금요일까지 5 영업일
print(f"{next_monday}로부터 5 영업일 뒤는 {target_date} ({get_weekday_name(target_date)}) 입니다.")
