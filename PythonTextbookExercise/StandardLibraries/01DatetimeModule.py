from datetime import datetime, date, time, timedelta

# 현재 날짜와 시간 얻기
now = datetime.now()
today = date.today()

print(f"현재 날짜와 시간: {now}") # 예: 2023-10-27 10:30:55.123456
print(f"오늘 날짜: {today}")     # 예: 2023-10-27

# 특정 날짜/시간 객체 생성
birthday = date(1995, 5, 15)
meeting_time = datetime(2024, 3, 15, 14, 30, 0) # 2024년 3월 15일 오후 2시 30분

print(f"생일: {birthday}")
print(f"회의 시간: {meeting_time}")

# 날짜 연산 (timedelta 사용)
tomorrow = today + timedelta(days=1)
next_week = now + timedelta(weeks=1)
one_hour_ago = now - timedelta(hours=1)

print(f"내일: {tomorrow}")
print(f"다음 주 이 시간: {next_week}")
print(f"한 시간 전: {one_hour_ago}")

# 날짜 형식 변환 (strftime)
formatted_date = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
print(f"형식화된 날짜: {formatted_date}") # 예: 2023년 10월 27일 10시 30분 55초

# 문자열에서 날짜 파싱 (strptime)
date_string = "2024-03-15 14:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"문자열 '{date_string}'로부터 파싱된 날짜: {parsed_date}")
print(parsed_date.date())
print(parsed_date.year)
print(parsed_date.month)
print(parsed_date.day)
print(parsed_date.hour)
print(parsed_date.minute)
# This method parses a string into a full datetime object, not just a date.