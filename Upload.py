"""
@ Coded By : Altalimul Islam 
@ Github : github.com/MITUL-588
"""
import os, requests, sys, time
from rich.console import Console
from rich.panel import Panel
console = Console()
logo = """[bold]
┏┓┳┓ ┏┓  ┳┳┏┓┓ ┏┓┏┓┳┓┏┓┳┓   ●  Coded By  : Altalimul Islam
┣ ┃┃ ┣   ┃┃┃┃┃ ┃┃┣┫┃┃┣ ┣┫   ●  Tool Type : Any File Uploader
┻ ┻┗┛┗┛  ┗┛┣┛┗┛┗┛┛┗┻┛┗┛┛┗   ●  Github    : MITUL-588[/bold]
"""
line = '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
def upload_to_fileio(file_path):
    url = 'https://file.io/'
    try:
      with open(file_path, 'rb') as file:
        files = {'file': file}
        console.print(f"\n{line}\nWait Uploading the file.......\n{line}\n", justify="center")
        response = requests.post(url, files=files)
        if response.status_code == 200:
            data = response.json()
            if 'success' in data and data['success']:
                file_url = data['link']
                console.print(Panel.fit(f"File uploaded successfully.                           \n\nDownload link: {file_url}"), justify="center")
                print("\n\n")
                return file_url
            else:
                print("Failed to upload file. Error:", data)
                return None
        else:
            print(f"Failed to upload file. HTTP Error code: {response.status_code}")
            return 
    except FileNotFoundError :
      console.print(f"\n{line}\nError : The file {file_path} could not be found. ", justify="center");time.sleep(2);console.print(f"\nRestarting The Tool........\n{line}", justify="center");time.sleep(2)
      Main()
def Main():
  os.system('clear')
  console.print(Panel(logo))
  console.print(Panel("ENTER FILE PATH", subtitle='╭─────', subtitle_align="left"))
  file_path = console.input('   ╰─> ')
  upload_to_fileio(file_path)
if __name__ == "__main__":
  Main()
