# SmartSensorHub_ToyProject
### 🚨🚦PyQt5 TOYPROJECT 리포지토리 : SmartSensorHub 

<img src="https://github.com/Juhyi/SmartSensorHub_toyproject/blob/main/images/title.png" higth= "400" width="500">

## 🧾프로젝트 소개
- 스마트홈 연동 클래스의 미니프로젝트는 WPF(Windows Presentation Foundation) 애플리케이션을 사용하여 MQTT(MQ Telemetry Transport) 프로토콜을 통해 수신한 데이터를 처리하고 시각화합니다.
- 이 프로젝트는 스마트홈 환경에서의 데이터 수집, 실시간 모니터링, 장치 제어 및 데이터 히스토리 확인을 할 수 있습니다.

## 🛠️기능 구현을 위해 패키지 및 툴
|개발 환경|Visual Studio|
|---|---|
|프로그래밍 언어|C#, Python|
|UI 프레임워크|WPF (Windows Presentation Foundation)|
|데이터베이스|SQL Server|
|차트 라이브러리|OxyPlot|

## 🚀개발 기간

## ✨주요 기능
### 1. WPF 애플리케이션을 통한 MQTT 데이터 수신 및 DB 저장
- MQTT 데이터 수신:
  -  WPF 애플리케이션은 MQTT 브로커로부터 데이터를 수신합니다. 이 데이터는 주로 스마트홈 환경에서 수집된 센서 데이터입니다.
- DB 저장
  -  수신된 데이터를 로컬 데이터베이스에 저장하여 나중에 조회 및 분석할 수 있도록 합니다.
    
|데이터 모니터링|
|----------|
|<img src="https://github.com/Juhyi/SmartSensorHub_toyproject/blob/main/images/mp002.png" higth= "600" width="700">|

### 2. MQTT 데이터 실시간 모니터링
- 온습도 모니터링
  -  실시간으로 온도 데이터와 습도 데이터를 모니터링하여 사용자에게 현재 상태를 시각적으로 제공합니다.

### 3. MQTT를 통한 RPi 제어 (LED 제어)
- LED 제어: Raspberry Pi와 연동하여 MQTT 메시지를 통해 LED를 제어합니다. 사용자는 WPF 애플리케이션을 통해 LED의 상태를 변경할 수 있습니다.

|데이터 실시간 모니터링 & LED 제어|
|----------|
|<img src="https://github.com/Juhyi/SmartSensorHub_toyproject/blob/main/images/mp003.png" higth= "600" width="700">|

### 4. WPF 애플리케이션에서의 MQTT 데이터 히스토리 확인
- 데이터 히스토리
  - 수신된 MQTT 데이터를 히스토리 형식으로 확인할 수 있습니다. 과거 데이터를 조회하여 분석할 수 있는 기능을 제공합니다.

### 5. 차트 라이브러리
- OxyPlot 사용
  - 프로젝트 초기에는 LiveChart2 대신 OxyPlot을 사용하여 데이터를 시각화합니다. OxyPlot은 WPF 애플리케이션에서 차트 및 그래프를 쉽게 그릴 수 있는 강력한 도구입니다.

|데이터 히스토리 시각화 차트|
|----------|
|<img src="https://github.com/Juhyi/SmartSensorHub_toyproject/blob/main/images/mp003.png" higth= "600" width="700">|









