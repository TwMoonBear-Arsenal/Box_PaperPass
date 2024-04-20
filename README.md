App_SimpleBox
====

# 壹、REPO內容說明

## 一、Asset運用目標

* 提供一個腳本，執行後可建立簡單靶機環境。

## 二、Asset運用架構

* Release Assets
  - **BashScript**：將Ubuntu設定ssh弱密碼及cp提權弱點，可做為簡單滲透提權使用。
  - **DockerFile**：可初始化一個Ubuntu容器，並將上述**BashScript**複製進去後執行。
* Users
  - **BoxAdmin**：管理者
  - **BoxUser**：使用者
* Entities
  - **BoxImage**：執行**DockerFile**後，會在本地端DockerHub自動產生的Docker映像檔。
  - **BoxContainer**：執行**BoxImage**後，實際運作的Box服務。
  
## 三、Asset運作流程

1. **BoxAdmin**執行**DockerFile**，完成**BoxImage**製作。
2. **BoxAdmin**將**BoxImage**依Docker運用方式執行**BoxContainer**。
3. **BoxUser**可遠端連線練習破密及提權靶機。

## 四、Asset測試個案

1. 個案：**BoxAdmin**可遠端連線**BoxContainer**並具備管理權。
2. 個案：**BoxUser**可遠端連線**BoxContainer**練習ssh破密。
3. 個案：**BoxUser**可遠端連線**BoxContainer**練習cp提權。

# 貳、REPO內容結構

* Github Repo<br/>
  📁.github<br/>
  └ 📁actions<br/>
  　└ ◻️ModuleTest.yml<br/>
  　└ ◻️PublishZip.yml<br/>  　
  📁.vs<br/>
  📁source<br/>
  ◻️.gitignore<br/>
  ◻️docker-compose.yml<br/>
  ◻️Dockerfile<br/>
  ◻️README.md<br/>

# 參、REPO使用方法

## 一、需求分析 & 二、系統設計

None

## 三、模組設計

設計(滾修)後直接於Readme註記。

## 四、模發測佈

### (一)模組發展

主要是dockerfile包含bash腳本，完成後直接存檔source下。

### (二)模組測試

利用github action做自動化測試。

### (三)模組發佈

利用github action做自動化發佈。

## [待修正]五、系測版控

### (一)獨立使用

* [方法]執行image
  * 利用docker直接建置，將新增image至本地registry
    ```bash
    # -t: tag
    # . : 單點表示目前目錄
    # --no-cache: 避免在Build時被cache，造成沒有讀到最新的Dockerfile
    docker build -t neo4j . --no-cache
    ```
  * 檢視本地images
    ```bash
    docker images
    ```  
  * 使用本地image起容器
    ```
    docker run --publish=7474:7474 --publish=7687:7687 --volume=$HOME/neo4j/data:/data neo4j
    ```
* 瀏覽器開啟 
* [方法]執行dockercompose
  * 直接執行dockercompose
    ```powershell
    docker-compose up
    ```
* 登入瀏覽器確認運作正常
* http://localhost:7474/browser/

* 使用UI關閉container並刪除image

### (二)併入SOA使用

* 將dockercompose內容複製至系統dockercompose使用。
