# Main python file; Run this
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os


def read_csv(filename):
    # Read it as a normal file
    with open(filename, "r") as f:
        # Strip additional lines so it does not run into errors later on then split by new line so we know each line is a different row
        csv_raw_data = f.read().strip().split("\n")

    csv_data = []
    for csv in csv_raw_data[1:]:
        csv_data.append(csv.split(","))

    columns = csv_raw_data[0].split(",")

    # We are returning a list of all names
    return csv_data, columns


def generator(template, data, locations, font=None, font_size=None, font_color=(0, 0, 0)):
    # font
    font = ImageFont.truetype("Kalam-Regular.ttf", 84)

    # open the template file
    img = Image.open(template)
    draw = ImageDraw.Draw(img)

    draw.text((locations[0][0], locations[0][1]), data[0], font_color, font=font)

    font = ImageFont.truetype("Kalam-Regular.ttf", 44)

    for i in range(len(data)):
        if i != 0:
            draw.text((locations[i][0], locations[i][1]), data[i], font_color, font=font)

    # Check if output destination exists
    if not os.path.exists("issuedCertificates/"):
        os.system("mkdir issuedCertificates")

    name = data[0]
    outfilename = "issuedCertificates/" + "-".join(name.split()) + "-certificate." + template.split(".")[-1]
    img.save(outfilename)


locations = []

def onclick(event):
    x = event.xdata
    y = event.ydata
    plt.scatter(x, y)
    locations.append([x, y])
    plt.show()

# Get all necessary inputs from the user
filename = input("Enter CSV filename: ")
csv_data, columns = read_csv(filename)

'''
additional_n = int(input("Your data has {} columns; If you have static data to add enter the number (Enter 0 if you have none): ".format(len(columns))))
additional_data = []
print("Enter your static data: ")
for _ in range(additional_n):
    additional_data.append(input("::: "))
csv_data = [(data + additional_data) for data in csv_data]
'''


template_name = input("Enter the Template path: ")

im = plt.imread(template_name)
fig, ax = plt.subplots()
ax.plot(0)
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.imshow(im)
plt.title("Click the {} points on the image".format(len(csv_data[0])))
plt.xlabel("Exit the editor to start the generation...")
plt.show()

for data in csv_data:
    print("Editing", data[0], "Certificate")
    generator(template_name, data, locations, font=None, font_size=None, font_color=(0, 0, 0))

print("Done!")
