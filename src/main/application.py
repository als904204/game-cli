from src.user.user_manager import UserManager
from src.view.cli import CLI

def application():
  user_manager = UserManager()
  view = CLI()

  logged_in_user = None

  while True:
    # 로그인 상태
    if logged_in_user:
      choice = view.display_logged_in_menu(logged_in_user.username)

      if choice == "1":
        view.display_message(f"'{logged_in_user.username}'님이 로그아웃 되었습니다.", "info")
        logged_in_user = None

    # 비 로그인 상태
    else:
      choice = view.display_main_menu()

      if choice == "1":
        username, password, password_confirm, = view.get_register_details()
        success, message = user_manager.register(username, password, password_confirm)

        if success:
          view.display_message(message, "success")
        else:
          view.display_message(message, "error")

      elif choice == "2":
        if logged_in_user:
          view.display_message(f"이미 '{logged_in_user.username}'님으로 로그인되어 있습니다.", "info")
          continue # 메인 메뉴로 다시 돌아감

        username, password = view.get_login_details()
        success, message, obj = user_manager.login(username, password)
        if success:
          logged_in_user = obj
          view.display_message(message, "success")
        else:
          view.display_message(message, "error")

      elif choice == "3":
        view.display_message("프로그램을 종료합니다...")
        break

if __name__ == "__main__":
  application()