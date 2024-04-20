#!/bin/bash

# 使用說明
# 1. 將此腳本複製到靶機上。
# 2. 打開終端機。
# 3. 使用 'cd' 命令進入腳本所在目錄。
# 4. 執行 'chmod +x setup_vulnerable_box.sh' 使腳本可執行。
# 5. 使用 './setup_vulnerable_box.sh' 命令運行腳本。

# 靶機管理設定
echo ""
echo "靶機管理設定開始"
sudo useradd -m boxadmin
sudo usermod -aG sudo boxadmin
echo "boxadmin:boxadmin" | sudo chpasswd

# 檢查並修改SSH配置以使用特定端口
SSH_CONFIG="/etc/ssh/sshd_config"
if ! grep -q "Port 9527" "$SSH_CONFIG"; then
  echo "Port 9527" | sudo tee -a "$SSH_CONFIG"
fi
sudo systemctl restart ssh

# 外部滲透設定
echo ""
echo "外部滲透設定開始"
sudo useradd -m allen
echo "allen:password" | sudo chpasswd

# 在allen的主目錄創建 user.txt 文件並寫入內容
echo "user's flag" | sudo tee /home/allen/user.txt

# 檢查並修改SSH配置以使用預設端口22
if ! grep -q "Port 22" "$SSH_CONFIG"; then
  echo "Port 22" | sudo tee -a "$SSH_CONFIG"
fi
sudo systemctl restart ssh

# 內部提權設定
echo ""
echo "內部提權設定開始"
echo "root's flag" | sudo tee /root/root.txt

# 賦予所有用戶sudo執行cp命令的權限
echo "ALL ALL=(ALL) NOPASSWD: /bin/cp" | sudo tee /etc/sudoers.d/custom-cp

# 完成設定
echo ""
echo "完成設定"
echo "靶機配置已完成，請開始進行滲透測試。"
