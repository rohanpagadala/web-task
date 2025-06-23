from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME = "dummy.test.ig123"
PASSWORD = "bot"#Incorrect Password here

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

driver.get("https://www.instagram.com/accounts/login/")
wait.until(EC.presence_of_element_located((By.NAME, "username")))

driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
except:
    pass

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
except:
    pass

try:
    home_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/' and descendant::div[text()='Home']]")))
    home_btn.click()
    time.sleep(2)
except:
    print("Home button click failed")

try:
    search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/explore/search/']")))
    search_btn.click()
    time.sleep(2)
except:
    print("Search button click failed")

try:
    search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    search_input.send_keys("cbitosc")
    time.sleep(2)
    search_input.send_keys(Keys.DOWN)
    time.sleep(1)
    search_input.send_keys(Keys.RETURN)
    time.sleep(2)
    search_input.send_keys(Keys.RETURN)
except:
    print("Search failed.")
    driver.quit()
    exit()

try:
    wait.until(EC.presence_of_element_located((By.XPATH, "//header")))
except:
    print("Profile didn't load.")
    driver.quit()
    exit()

try:
    follow_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//header//button[1]")))
    if follow_btn.text.lower() == "follow":
        follow_btn.click()
        time.sleep(2)
except:
    print("Follow button issue")

try:
    bio_elem = wait.until(EC.presence_of_element_located((By.XPATH, "//header/following-sibling::div//div")))
    bio = bio_elem.get_attribute("innerText").strip()
except:
    bio = "Bio not found"

try:
    stats_blocks = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul/li/div/span/span")))
    posts = stats_blocks[0].text
    followers = stats_blocks[1].get_attribute("title") or stats_blocks[1].text
    following = stats_blocks[2].text
except:
    posts = followers = following = "N/A"

with open("profile_info.txt", "w", encoding="utf-8") as f:
    f.write("CBITOSC Instagram Profile Info\n")
    f.write(f"Bio: {bio}\n")
    f.write(f"Posts: {posts}\n")
    f.write(f"Followers: {followers}\n")
    f.write(f"Following: {following}\n")

driver.quit()
