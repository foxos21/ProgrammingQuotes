from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import textwrap

def add_text_with_outline(image_path, text, blur=7,
                          font_path="fonts/UbuntuMono-Bold.ttf", font_size=100,
                          outline_width=20, color=(255, 255, 255), outline_color=(0, 0, 0)):
    
    img = Image.open(image_path)
    img = img.filter(ImageFilter.BoxBlur(blur))
    
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    
    # New text wrapping logic
    char_width, char_height = draw.textsize("A", font=font)
    max_chars_per_line = img.size[0] // char_width
    
    wrapped_text = textwrap.fill(text, width=max_chars_per_line)
    lines = wrapped_text.split('\n')
    combined_text_height = len(lines) * char_height
    y_offset = (img.size[1] - combined_text_height) // 2

    for i, line in enumerate(lines):
        line_width, line_height = draw.textsize(line, font=font)
        x = (img.size[0] - line_width) / 2
        y = y_offset + i * line_height
        draw.text((x, y), line, font=font, fill=color,
                  stroke_width=outline_width, stroke_fill=outline_color)
    
    #img.save('wallpaper_image.jpg')
    img.show()

# Set up the random seed
random.seed()

# Quotes and image selection
quotes = [
    "*Why didn't you just do it in a few hours, than coding for 2 months straight to automate it?* Because we are programmers and thats what we do.", 
    "Use your brain NOT AI, Trust me.", 
    "Use your brain NOT AI", 
    "Without requirements or design, programming is the art of adding bugs to an empty text file.", 
    "There are two ways to write error-free programs; only the third one works.", 
    "Simplicity is the soul of efficiency.",
    "Every successful program was once a failed idea.",
    "Any fool can write code that a computer can understand; Good programmers write code that humans can understand.",
    "Programming isn't about what you do with your fingers; it's about what you do with your mind.",
    "Coffee, code, repeat.",
    "The best way to predict the future is to invent it.",
    "The only true wisdom is in knowing you know nothing.",
    "The function of code should be to express thoughts, not to hide them.",
    "If you make it foolproof, someone will make a better fool.",
    "Code never lies, comments sometimes do.",
    "Sometimes the best code is no code at all.",
    "Bugs are inevitable, debugging is optional.",
    "Software development is like archaeology - you spend most of your time digging through dirt.",
    "Programming is like writing a recipe. You have to get all the ingredients and steps just right, or the dish will be a disaster.",
    "Learning is not compulsory... neither is breathing.",
    "Code is poetry.",
    "If debugging is the art of removing bugs, then programming must be the art of putting them in.",
    "The more I learn, the more I realize how much I don't know.",
    "Don't be afraid to fail. It's the only way to succeed.",
    "It's not a bug, it's a feature.",
    "The code doesn't lie, but sometimes it does obfuscate.",
]

for _ in range(1):
    text = random.choice(quotes)
    image_number = random.randint(1, 12)
    image_path = f"images/image_{image_number}.jpg"
    add_text_with_outline(image_path, text)
