# Use Case: System Interaction - Image Conversion

This use case illustrates how the Gemini CLI can interact directly with the local file system to identify, count, and manipulate image files using system tools.

### Prompts

```bash
# Identify and count files
identify .jpeg, .jpg files
count the number of .jpeg and .jpg files

# Convert a single file
convert the selected .jpeg file to png

# Perform a batch operation
Convert all the images in this directory to png, and rename them to use dates from the exif data.
