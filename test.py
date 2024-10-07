import os
import glob
import pandas as pd

# Google Drive에 있는 폴더 경로 (폴더 구조에 맞게 변경)
main_folder_path = r'C:\Users\kangmin\Desktop\FeatData'

# 데이터를 저장할 리스트 초기화
data = []

# 폴더 내 모든 이미지 파일 불러오기
for label_folder in os.listdir(main_folder_path):
    folder_path = os.path.join(main_folder_path, label_folder)

    if os.path.isdir(folder_path):  # 하위 폴더인지 확인
        image_files = glob.glob(os.path.join(folder_path, '*.jpg'))  # .jpg 확장자의 이미지 파일들

        for image_path in image_files:
            # 레이블과 이미지 경로를 저장
            data.append({'label': label_folder, 'path': image_path})

# DataFrame 생성
df = pd.DataFrame(data)

# DataFrame을 CSV 파일로 저장
csv_path = r'C:\Users\kangmin\Desktop\FeatData\image_data.csv'
df.to_csv(csv_path, index=False)

print(f'DataFrame이 생성되고, {csv_path}에 저장되었습니다.')