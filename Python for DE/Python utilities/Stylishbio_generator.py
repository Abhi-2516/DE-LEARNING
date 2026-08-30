# """
# Challenge: Stylish Bio Generator for Instagram/Twitter

# Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

# Your program should:
# 1. Prompt the user to enter their:
#    - Name
#    - Profession
#    - One-liner passion or goal
#    - Favorite emoji (optional)
#    - Website or handle (optional)


import textwrap


name = input("Enter your name : ").strip()

profession = input("Enter your proffesion : ").strip()

passion = input("Enter your passion of goal : ").strip()

emoji = input("Fav emoji : ").strip()

website = input("enter you web or handle : ").strip()

print("\nChoose your style: ")
print("1. Simple lines ")
print("2. Vertical flair ")
print("3. Emoji sandwich ")

style = input("Enter 1, 2 or 3: ")

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n💡 {passion}\n {website}" 
    elif style == "2":
        return f"{emoji} {name}\n {profession}🔥\n {passion} \n {website}🔥"
    elif style == "3":
        return f"{emoji*3}\n {name} - {profession}\n {passion}\n {website} \n {emoji*3}"

bio_gen = generate_bio(style)

print("\n Your Stylish bio is :")
print("*" * 50)
print(textwrap.dedent(bio_gen))
print("*" * 50)

filesave = input("Do you want to save the output file press y or n").lower()

if(filesave == 'y'):
    with open("Bio.txt" , "w") as file:
        file.write(bio_gen)
    print("File saved tyou can view it")
else:
    print("Thanks")
      



# 2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

# 3. Add optional hashtags or emojis for flair.

# Example:
# Input:
#   Name: Riya
#   Profession: Designer
#   Passion: Making things beautiful
#   Emoji: 🎨
#   Website: @riya.design

# Output:
#   🎨 Riya | Designer  
#   💡 Making things beautiful  
#   🔗 @riya.design

# Bonus:
# - Let the user pick from 2-3 different layout styles.
# - Ask the user if they want to save the result into a `.txt` file.
# """

