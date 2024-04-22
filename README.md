Box_SimpleOne
====
> 國防大學理工學院資工系 助理教授陳佑全

# 壹、Asset運用想定

## 一、Asset運用目標

* 提供一組Docker相關腳本，運行腳本後可建立簡單紅隊靶機，作為示範教學使用。

## 二、Asset運用架構

* Assets From this Repo
  - **BoxSetting.sh**：將Ubuntu設定ssh弱密碼及cp提權弱點，可做為簡單滲透提權使用。
  - **DockerFile**：可初始化一個Ubuntu容器，並將上述**BashScript**複製進去後執行。
* Users
  - **BoxAdmin**：管理者
  - **BoxUser**：使用者
* Entities
  - **BoxImage**：執行**DockerFile**後，會在本地端DockerHub自動產生的Docker映像檔。
  - **BoxContainer**：執行**BoxImage**後，實際運作的Box服務。
  - **user.txt**：置於 /home/allen 內之user flag，為外部滲透之證明。
  - **root.txt**：置於 /root 內之root flag，為提權之證明。
  
## 三、Asset運作流程

1. **BoxAdmin**執行**DockerFile**，完成**BoxImage**製作。
2. **BoxAdmin**將**BoxImage**依Docker運用方式執行**BoxContainer**。
3. **BoxUser**可遠端連線練習破密及提權靶機。

## 四、Asset測試個案

1. 個案：**BoxAdmin**可遠端連線**BoxContainer**並具備管理權。
2. 個案：**BoxUser**可遠端連線**BoxContainer**並以弱密碼登入後，讀取user.flag。
3. 個案：**BoxUser**可遠端連線**BoxContainer**登入後，操作cp提權讀取root.flag。

# 貳、REPO內容結構

📁.github  <br/>
　└📁actions  <br/>
　　　└🗎 BuildTest.yml *<= 組建測試* <br/> 
　　　└🗎 DockerizationTest.yml *<= 容器化測試* <br/>
　　　└🗎 ModuleTest.yml *<= 模組功能測試* <br/>
　　　└🗎 PublishZip.yml *<= 發佈腳本壓縮檔* <br/>
📁.vs<br/>
📁doc<br/>
📁source<br/>
　└📁Docker<br/>
　│　└🗎 dockerfile_Prompt.md<br/>
　│　└🗎 dockerfile.txt<br/>
　└📁Scr_SimpleBox<br/>
　│　└🗎 BoxSetting_Prompt.md<br/>
　│　└🗎 BoxSetting.sh<br/>
　└📁Scr_SimpleBox_ModTest<br/>
　　　└🗎 Scr_SimpleBox_ModTest_Prompt.txt<br/>
　　　└🗎 Scr_SimpleBox_ModTest.sh<br/>
🗎 .gitignore<br/>
🗎 README.md<br/>

# 參、REPO使用方法

## 一、需求分析 & 二、系統設計

適用於Docker單一或區網靶機教學。

## 三、模組設計

設計(滾修)後直接於Readme註記。

## 四、模發測佈

### (一)模組發展

主要是dockerfile包含bash腳本，完成後直接存檔source下。

### (二)模組組建

* 主要是檢整Docker腳本檔案。
* 利用github action做自動化測試。

### (三)模組封裝

* 以Docker Image為封裝標的，故須提供dockerfile。
* 利用github action做自動化發佈。

### (四)模組測試

利用github action做自動化測試。

### (五)模組發佈

利用github action做自動化發佈。

## 五、系測版控

### (一)手動作法

TBD

### (二)Docker-compose作法

TBD
