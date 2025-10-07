import time
from datetime import datetime # datetime과 비교하기 위해 import

# Unix 타임스탬프 (float형)
current_timestamp = time.time()
print(f"현재 Unix 타임스탬프: {current_timestamp}")

# datetime 객체와 비교
print(f"datetime.now() 객체: {datetime.now()}")

# 시간 지연 (프로그램 실행 멈춤)
print("\n10초 동안 실행을 멈춥니다...")
time.sleep(10) # 3초 대기
print("10초 후 프로그램이 다시 실행되었습니다.")

# 성능 측정
start_time = time.perf_counter()
# 시간이 걸리는 작업 (예: 큰 리스트의 합계 계산)
result = sum(i**2 for i in range(10**7)) # 1천만 개의 제곱 합산
# i goes from 0 to 9,999,999
end_time = time.perf_counter()

execution_time = end_time - start_time
# 소수점 4자리까지 출력
print(f"\n작업 실행 시간: {execution_time:.4f}초")

# 로컬 시간과 UTC 시간 확인
local_time_struct = time.localtime()
utc_time_struct = time.gmtime()

# asctime으로 보기 좋게 변환
print(f"\n현지 시간 (asctime): {time.asctime(local_time_struct)}")
print(f"UTC 시간 (asctime): {time.asctime(utc_time_struct)}")
# Convert a struct_time object into an ASCII-formatted string