import pyautogui
import time
import pyperclip

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def update_egao_file(col0):
    with open('egao.txt', 'r') as file:
        content = file.read()
    
    updated_content = content.replace('OrgSet-', col0)
    pyperclip.copy(updated_content)

def log_update(col0, log_file):
    message = f'The org set {col0} has been updated, SIR!'
    joke_message = f'--> Employee group {col0} is now up to date. Why don’t programmers like nature? It has too many bugs!'
    with open(log_file, 'a') as file:
        file.write(message + '\n')
    print(message)
    print(joke_message)

def automate_tasks(input_file, log_file):
    lines = read_input_file(input_file)

    for line in lines:
        columns = line.strip().split('|')
        col0 = columns[0]

        # Perform mouse clicks and keyboard actions
        pyautogui.click(1827, 230)
        time.sleep(1)

        pyautogui.click(1815, 349)
        time.sleep(1)

        pyautogui.typewrite(col0)
        time.sleep(1)

        pyautogui.click(1810, 394)
        time.sleep(1)

        pyautogui.click(3397, 234)
        time.sleep(1)

        # Update egao.txt and copy to clipboard
        update_egao_file(col0)
        time.sleep(1)

        # Click console and paste content
        pyautogui.click(95, 128)
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.click(44, 70)
        time.sleep(1.5)

        # Log the update
        log_update(col0, log_file)

        pyautogui.click(3414, 206)
        time.sleep(1)

if __name__ == "__main__":
    input_file_path = 'input.txt'
    log_file_path = 'empGrpupdatelog.txt'
    automate_tasks(input_file_path, log_file_path)
