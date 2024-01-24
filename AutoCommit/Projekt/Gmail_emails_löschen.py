import time
from utils import open_browser,click_at_position

def main():
    open_browser("https://mail.google.com/mail/u/0/#inbox")
    time.sleep(5)
    click_at_position(1834,358)
    time.sleep(2)
    click_at_position(1518,660)
    time.sleep(2)
    for i in range(5):
        click_at_position(486,287)
        time.sleep(1)
        click_at_position(707,282)
        time.sleep(1)

main()