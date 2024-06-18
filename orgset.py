import pyautogui
import time
import pyperclip

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def read_manager_org_set(file_path):
    with open(file_path, 'r') as file:
        manager_org_set = file.read()
    return manager_org_set

def log_update(message, log_file):
    with open(log_file, 'a') as file:
        file.write(message + '\n')
    print(message)

def automate_tasks(input_file, manager_org_set_file, log_file):
    lines = read_input_file(input_file)
    manager_org_set = read_manager_org_set(manager_org_set_file)
    
    # Store the ManagerOrgSet text in the clipboard
    pyperclip.copy(manager_org_set)

    for line in lines:
        columns = line.strip().split('|')
        col0 = columns[0]

        # Click Mouse Coordinate 1905,321
        pyautogui.click(1905, 321)
        time.sleep(1)

        # Press Ctrl+A to select all text
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)

        # Press Backspace to delete the text
        pyautogui.press('backspace')
        time.sleep(0.5)

        # Write Col0
        pyautogui.typewrite(col0)
        time.sleep(1)

        # Press Tab
        pyautogui.press('tab')
        time.sleep(0.5)

        # Press Enter
        pyautogui.press('enter')
        time.sleep(1)

        # Mouse Click 1910,393
        pyautogui.click(1910, 393)
        time.sleep(1)

        # Edit - Mouse Click 1910,289
        pyautogui.click(1910, 289)
        time.sleep(1)

        # Open Console - Mouse Click 95,128
        pyautogui.click(95, 128)
        time.sleep(1)

        # Press Ctrl+V to paste text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Press Enter
        pyautogui.press('enter')
        time.sleep(1)

        # Mouse Click 44,70
        pyautogui.click(44, 70)
        time.sleep(1)

        # Log the update
        log_message = f'Org set :{col0} has been updated sir!!'
        log_update(log_message, log_file)

if __name__ == "__main__":
    input_file_path = 'input.txt'
    manager_org_set_file_path = 'ManagerOrgSet.txt'
    log_file_path = 'Log.txt'
    automate_tasks(input_file_path, manager_org_set_file_path, log_file_path)
