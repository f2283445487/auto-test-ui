import time

from base.base import Base


class PageLogin(Base):
    permission = "com.asf.singa:id/btn_ok"
    permission_accept = "com.lbe.security.miui:id/permission_allow_foreground_only_button"
    text_accept = "com.asf.singa:id/btn_sure"
    go_login = "com.asf.singa:id/borrow_money_now"
    phone_text = "com.asf.singa:id/phoneEditTextLogin"
    password_text = "com.asf.singa:id/password"
    login_button = "com.asf.singa:id/loginButton"

    def accept(self):
        self.id_base_click(self.permission)

    def accept_permission(self):
        self.id_base_click(self.permission_accept)

    def accept_text(self):
        self.id_base_click(self.text_accept)

    def page_click_login(self):
        self.id_base_click(self.go_login)

    def input_phone(self, username):
        self.send_keys(self.phone_text, username)

    def click_login(self):
        self.id_base_click(self.login_button)

    def input_password(self, password):
        self.send_keys(self.password_text, password)

    def page_login(self, username, password):
        self.accept()
        self.accept_permission()
        self.accept_text()
        self.page_click_login()
        self.input_phone(username)
        self.click_login()
        self.input_password(password)
        self.click_login()
