Request Prompt to ChatGPT
========
> ...

# 目的

## 未來運用構想：
I've prepared a vulnerable Ubuntu that with weak ssh password and cp-privilege vulnerabilities. I need a python test script.

## 擬請ChatGPT提供：
please provide a python script to test following functions.

# 需求項目

## 測試個案-管理設定
  * connect the ssh service in port 9527 with  uid/pwd:boxadmin/boxadmin, the result should show that boxadmin is in sudo group.。

## 測試個案-外部滲透
  * connect the ssh service in port 9527 with  uid/pwd:allen/allen, the result should show login attempt fail.
  * connect the ssh service in port 9527 with  uid/pwd:allen/password, the result should show login attempt success.
  * read ~/user.txt, the result should show file access success.。

## 測試個案-內部提權
  * connect the ssh service in port 9527 with  uid/pwd:allen/password, the result should show login attempt success.
  * use cp-previlege escallation tech to get root authority then read root.txt in root home directory,  the result should show file access success. 

# ChatGPT回復格式:

## 注意事項：
  * Please use PyTest for test work.
  * do the work step by step.make it easy to understand for students.
  * provide limited echo lines with traditional Chinese I show you in following reference.
  * Each Python function should contains detailed docstrings including A brief description of what the function does.

## 回復範例：

```
import pytest
import ...

# 測試個案1
@pytest.fixture(params=["hello", "pytest", "12345", "空字符串"])
def string_fixture(request):
    """測試個案1：提供多個測試用例"""
    return request.param

# 測試個案2
def test_reverse_string(string, expected):
    """測試個案2：測試字符串反轉功能"""
    assert reverse_string(string) == expected, "字符串反轉結果不正確"

# 測試個案3
def test_is_substring(string_fixture):
    """測試個案3：測試子字符串檢查功能"""
    assert is_substring("hellopytest", string_fixture), f"{string_fixture} 應該是 'hellopytest' 的子字符串"
```