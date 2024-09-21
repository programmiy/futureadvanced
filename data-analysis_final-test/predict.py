import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np
import datetime as dt
# CSV 파일 로드
df = pd.read_csv('Source.csv')
# 날짜와 시간을 숫자형으로 변환
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].map(dt.datetime.toordinal)
# 'direction' 열을 원-핫 인코딩
df = pd.get_dummies(df, columns=['direction'])

# 이제 'direction' 열은 여러 개의 숫자형 열로 변환되었습니다.
# 'region' 열을 원-핫 인코딩
df = pd.get_dummies(df, columns=['region'])

# 이제 'region' 열은 여러 개의 숫자형 열로 변환되었습니다.
# 예측하려는 열을 선택 (여기서는 'target'이라고 가정)
target = df['AQI']

# 'target' 열을 제외한 모든 열을 특성으로 사용
features = df.drop('AQI', axis=1)

# 데이터를 훈련 세트와 테스트 세트로 분할
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=1)

# 선형 회귀 모델 생성 및 훈련
model = LinearRegression()
model.fit(features_train, target_train)

# 테스트 세트에 대한 예측 수행
target_pred = model.predict(features_test)

# 예측의 정확도 평가
print('Mean Absolute Error:', metrics.mean_absolute_error(target_test, target_pred))
print('Mean Squared Error:', metrics.mean_squared_error(target_test, target_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(target_test, target_pred)))