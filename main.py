import pyautogui
import time

# Function to read input file
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# Function to read unassign text file
def read_unassign_file(file_path):
    with open(file_path, 'r') as file:
        unassign_text = file.read()
    return unassign_text

# Main function to automate the tasks
def automate_tasks(input_file, unassign_file):
    lines = read_input_file(input_file)
    unassign_text = read_unassign_file(unassign_file)

    # Store the unassign text in the clipboard
    pyperclip.copy(unassign_text)

    for line in lines:
        columns = line.strip().split('|')
        col0 = columns[0]

        # Click on Mouse coordinates 109, 232
        pyautogui.click(1827, 232)
        time.sleep(1)

        # Click on Mouse coordinates 53, 350
        pyautogui.click(1773, 352)
        time.sleep(1)

        # Write col0
        pyautogui.typewrite(col0)
        time.sleep(1)

        # Click on Mouse coordinates 195, 399
        pyautogui.click(1828, 399)
        time.sleep(1)
        pyautogui.click(1828, 399)
        time.sleep(1)

        # Click on Edit 918, 232
        pyautogui.click(3395, 235)
        time.sleep(1)

        # Click on Mouse coordinates 1023, 108
        pyautogui.click(63, 101)
        time.sleep(1)

        # Paste Unassign.txt content using ctrl+v
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter') 
        time.sleep(1)

        # Click on Mouse coordinates 1005, 72
        pyautogui.click(43, 68)
        time.sleep(1)

        #pyautogui.click(923, 298)
        time.sleep(3)

        pyautogui.click(3415, 204)
        time.sleep(1)

        print(f'Commander Sir we have processed:'+ col0)

if __name__ == "__main__":
    import pyperclip
    input_file_path = 'input.txt'
    unassign_file_path = 'Unassign.txt'
    automate_tasks(input_file_path, unassign_file_path)
