#!/bin/bash

# 使用說明
# 1. 將此腳本複製到您的Ubuntu系統上。
# 2. 打開終端機。
# 3. 使用命令行導航到腳本所在的目錄。
# 4. 給腳本執行權限: chmod +x setup_vulnerable.sh
# 5. 以root權限運行此腳本: sudo ./setup_vulnerable.sh

# 靶機管理設定
echo "正在進行靶機管理設定..."
sudo useradd -m -s /bin/bash -p $(openssl passwd -1 boxadmin) boxadmin
sudo usermod -aG sudo boxadmin

# SSH服務設定
echo "設定SSH服務..."
sudo sed -i 's/#Port 22/Port 9527/' /etc/ssh/sshd_config
echo "Port 9527" | sudo tee -a /etc/ssh/sshd_config
sudo service ssh restart

# 外部滲透設定
echo "正在設定外部滲透弱點..."
sudo useradd -m -s /bin/bash -p $(openssl passwd -1 password) allen
echo "user's flag" | sudo tee /home/allen/user.txt
sudo chown allen:allen /home/allen/user.txt

# 內部提權設定
echo "正在設定內部提權弱點..."
echo "root's flag" | sudo tee /root/root.txt
echo "ALL ALL=(ALL) NOPASSWD: /bin/cp" | sudo tee -a /etc/sudoers

# 完成設定
echo "完成設定，系統已設定完成，可以開始進行滲透測試。"
