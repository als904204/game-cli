"""
사용자

Attributes:
    username (str): 사용자의 아이디
    password (str): 사용자의 비밀번호 (초기에는 평문으로 저장)
"""
class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def __str__(self):
    return f"User(username='{self.username}')"

if __name__ == "__main__":
  user1 = User("testUser", "password")
  print(f"테스트 사용자 아이디: {user1.username}")
  print(f"테스트 사용자 비밀번호: {user1.password}")
