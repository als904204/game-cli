"""
사용자 등록, 로그인 및 사용자 데이터 관리를 담당하는 클래스입니다.
초기에는 사용자 정보를 메모리 내 딕셔너리에 저장합니다.
"""
from src.user.user import User


class UserManager:
  """
  UserManager 객체를 초기화합니다.
  users 딕셔너리는 사용자 이름을 키로, User 객체를 값으로 저장합니다.
  예: {'testuser': User('testuser', 'password123')}
  """
  def __init__(self):
    self.users = {}


  def is_username_exists(self, username):
    """
    유저네임 중복검사
    """
    return username in self.users

  def register(self, username, pwd, pwd_confirm):
    if not username or not pwd or not pwd_confirm:
      return False, "아이디나 비밀번호가 공백입니다."
    if pwd!=pwd_confirm:
      return False, "비밀번호가 일치하지 않습니다.",
    if self.is_username_exists(username):
      return False, "중복된 아이디입니다."

    new_user = User(username, pwd)
    self.users[username] = new_user
    return True, f"'{username}'님, 회원가입이 성공적으로 완료되었습니다."

  def login(self, username, pwd):
    if not username or not pwd:
      return False, "아이디나 비밀번호가 공백입니다.", None
    if not self.is_username_exists(username):
      return False, "잘못된 아이디 또는 비밀번호입니다.", None

    user = self.users[username]
    if user.password == pwd:
      return True, f"'{username}'님, 환영합니다! 로그인되었습니다.", user
    else:
      return False, "알 수 없는 에러입니다.", None

  def __str__(self):
    if not self.users:
      return "UserManager : 현재 등록된 사용자가 없습니다."
    user_list = ", ".join(self.users.keys())
    return f"UserManager : 등록된 사용자 ({len(self.users)}명) - [{user_list}]"

if __name__ == "__main__":
  manager = UserManager()
  print(manager)

  print("\n--- 회원가입 성공 테스트1 ---")
  result, message = manager.register("testUser1", "password", "password")
  print(f" 결과 : {result}, 메시지 : {message}")
  print(manager)

  print("\n--- 회원가입 성공 테스트2 ---")
  result, message = manager.register("testUser2", "password", "password")
  print(f" 결과 : {result}, 메시지 : {message}")
  print(manager)

  print("\n--- 회원가입 중복 아이디 테스트 ---")
  result, message = manager.register("testUser1", "pwd", "pwd")
  print(f" 결과 : {result}, 메시지 : {message}")
  print(manager)

  print("\n--- 회원가입 비밀번호 불일치 테스트 ---")
  result, message = manager.register("testUser3", "pwd1", "pwd2")
  print(f" 결과 : {result}, 메시지 : {message}")
  print(manager)

  print("\n--- 회원가입 아이디 공백 테스트 ---")
  result, message = manager.register("", "test", "test")
  print(f"결과: {result}, 메시지: {message}")

  print("\n--- 로그인 성공 테스트 ---")
  success, message, user = manager.login("testUser1", "password")
  print(f"로그인 여부 : {success}, 메시지 : {message}, 사용자 : {user}")

  print("\n--- 로그인 아이디 없음 실패 테스트 ---")
  success, message, user = manager.login("testUser123", "password")
  print(f"로그인 여부 : {success}, 메시지 : {message}, 사용자 : {user}")

  print("\n--- testUser1 객체 직접 접근 확인 ---")
  if "testUser1" in manager.users:
    print(f"testUser1 비밀번호 : {manager.users['testUser1'].password}")



