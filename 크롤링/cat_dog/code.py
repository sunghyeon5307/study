from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
import urllib.request 
import os
from selenium.webdriver.common.by import By

search = "dog image"   # 이미지 검색어
count = 1000       # 크롤링할 이미지 개수
save_dir = "/Users/bagseonghyeon/Desktop/study/크롤링/cat_dog/dog_data"  # 이미지를 저장할 폴더 경로

driver = webdriver.Chrome()  
driver.get("https://www.google.com/imghp?hl=ko&tab=wi") 
elem = driver.find_element(By.NAME, "q") 
elem.send_keys(search)
elem.send_keys(Keys.RETURN) 

# 페이지 스크롤하여 추가 이미지 로드
SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()  # '더보기' 버튼 클릭하여 추가 이미지 로드
            time.sleep(1)
        except:
            print('여기서 막혔습니다')
            break
    last_height = new_height


time.sleep(1)
# 이미지 검색 결과에서 이미지 요소 찾기
try:
    images = driver.find_elements(By.CSS_SELECTOR, ".YQ4gaf")
except:
    print('이번엔 여기서 오류')

# 저장할 폴더가 없다면 생성
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 이미지 다운로드 및 저장
for i, image in enumerate(images[:count], 1):
    try: 
        # image.click()  # 이미지 클릭하여 확대
        # # time.sleep(1)
        # imgUrl = driver.find_element(By.CSS_SELECTOR,".sFlh5c.pT0Scc.iPVvYb").get_attribute("src")  # 이미지 URL 가져오기
        imgUrl = image.get_attribute("src")  # 이미지 URL 가져오기
        filename = os.path.join(save_dir, f"{search}_{i}.jpg")  # 이미지 저장 경로 설정
        urllib.request.urlretrieve(imgUrl, filename)  # 이미지 다운로드
        print(f"{i}번 이미지 다운로드 완료")
    except Exception as e:
        print(f"{i}번 이미지 다운로드 실패:", e)
# 웹 드라이버 종료
driver.quit()

