from PIL import Image

# Load the image
img = Image.open("grad.jpg")

# Define the size of the smaller images (cards)
card_size = (100, 100)

# Split the image into a grid of smaller images
cards = []
for y in range(0, img.height, card_size[1]):
    for x in range(0, img.width, card_size[0]):
        # Crop a smaller image from the original image
        card = img.crop((x, y, x + card_size[0], y + card_size[1]))
        cards.append(card)

# Duplicate each smaller image
doubled_cards = []
for card in cards:
    # Create a copy of the card image
    copy_card = card.copy()
    doubled_cards.append(card)
    doubled_cards.append(copy_card)

# Calculate the number of columns in the reassembled image
num_cols = img.width // card_size[0]

# Calculate the number of rows in the reassembled image
num_rows = (len(doubled_cards) // 2) // num_cols

# Create a new image to hold the reassembled cards
output_img = Image.new("RGB", (img.width, img.height))

# Paste the cards into the output image
for i, card in enumerate(doubled_cards):
    # Calculate the x and y coordinates of the card in the output image
    x = (i % num_cols) * card_size[0]
    y = (i // num_cols) * card_size[1]
    # Paste the card into the output image
    output_img.paste(card, (x, y))

# Save the reassembled image
output_img.save("output_image.jpg")
