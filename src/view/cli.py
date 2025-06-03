class CLI:
  def display_main_menu(self):
    print("\n╔═════════════════════════════╗")
    print("║     🎮 GAME 🎮                ║")
    print("╠═══════════════════════════════╣")
    print("║ 1. 회원가입                     ║")
    print("║ 2. 로그인                      ║")
    print("║ 3. 종료                        ║")
    print("╚═══════════════════════════════╝")
    while(True):
      choice = input("  원하는 작업의 번호를 입력하세요: ").strip()
      if choice in ['1', '2', '3']:
        return choice
      else:
        self.display_message("잘못된 입력입니다. 1, 2, 3 중 하나를 입력해주세요.", "error")

  def display_logged_in_menu(self, username):
    print(f"\n╔═════════════════════════════╗")
    print(f"║ {username}님, 환영합니다!      ║")
    print(f"╠═════════════════════════════╣")
    print(f"║ 1. 로그아웃                  ║")
    print(f"║ 2. 구현중                  ║")
    print(f"╚═════════════════════════════╝")
    while True:
      choice = input("메뉴를 선택하세요.").strip()
      if choice == "1":
        return "1"
      else:
        self.display_message("잘못된 입력입니다. 메뉴를 확인해주세요.", "error")



  def get_register_details(self):
    print("\n--- 회원가입 ---")
    username = input("아이디 : ").strip()
    password = input("비밀번호 : ").strip()
    password_confirm = input("비밀번호 확인 : ").strip()
    return username, password, password_confirm

  def get_login_details(self):
    print("\n--- 로그인 ---")
    username = input("아이디: ").strip()
    password = input("비밀번호: ").strip()
    return username, password

  def display_message(self, message, message_type="info"):
    if message_type == "success":
      print(f"[성공] {message}")
    elif message_type == "error":
      print(f"[에러] {message}")
    else:
      print(f"{message}")

if __name__ == "__main__":
  view = CLI()
  # view.display_main_menu()

  # reg_username, reg_password, reg_confirm = view.get_register_details()
  # view.display_message(f"입력한 아이디 : {reg_username}, 비밀번호 : {reg_password}, 확인 : {reg_confirm}")

  # 로그인 정보 입력 테스트
  # login_username, login_password = view.get_login_details()
  # view.display_message(f"입력된 아이디: {login_username}, 비밀번호: {login_password}")

  view.display_message("일반 메세지")
  view.display_message("성공 메세지", "success")
  view.display_message("에러 메세지", "error")



