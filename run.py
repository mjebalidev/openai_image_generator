import os
import openai
import requests

title = "Image OpenAI Generator"

# generate ascii art title with figlet
#os.system(f"figlet {title}")

# generate ascii art title with figlet with random font
os.system(f"figlet -f $(ls /usr/share/figlet | shuf -n 1) {title}")

# set openai api key
openai.api_key = "ENTER_YOUR_OPEN_AI_API_KEY_HERE"
#openai.Model.list()

# ask user to enter the desired generated image
prompt = input("Enter the desired image: ")

# generate the image
def generate_image(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

try:
    image_url = generate_image(prompt)
except:
    print("Error: Please try again.")
    os.system("sleep 4")
    os.system("clear")
    os.system("python3 run.py")

# replace space with underscore
clear_prompt = prompt.replace(" ", "_")

#display url
print("Image URL:")
print(image_url)

# get current time and date short version
current_time_date = os.popen("date +%Y-%m-%d_%H-%M-%S").read()
# delete last \n
current_time_date = current_time_date[:-1]


# save the image with the current time and date
response = requests.get(image_url)
with open(f"images/{clear_prompt}_{current_time_date}.png", "wb") as f:
    f.write(response.content)

# display file path
print("File path:")
print(f"images/{clear_prompt}_{current_time_date}.png")

# sleep for 2 second
os.system("sleep 2")

# display the image with ubuntu image viewer
os.system(f"xdg-open images/{clear_prompt}_{current_time_date}.png")

# clear the terminal
os.system("clear")

# restart the script
os.system("python3 run.py")

