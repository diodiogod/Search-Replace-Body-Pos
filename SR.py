import os
import re

# Define the replacement pairs

replacements = {
    # Phrases with prepositions for right side
    "on his right side": "on the side on the right",
    "on her right side": "on the side on the right",
    "on their right side": "on the side on the right",
    "to his right side": "to the side on the right",
    "to her right side": "to the side on the right",
    "to their right side": "to the side on the right",

    # Phrases without prepositions for right side
    "his right side": "his side on the right",
    "her right side": "her side on the right",
    "their right side": "their side on the right",

    # Phrases with prepositions for left side
    "on his left side": "on the side on the left",
    "on her left side": "on the side on the left",
    "on their left side": "on the side on the left",
    "to his left side": "to the side on the left",
    "to her left side": "to the side on the left",
    "to their left side": "to the side on the left",

    # Phrases without prepositions for left side
    "his left side": "his side on the left",
    "her left side": "her side on the left",
    "their left side": "their side on the left",

    # Phrases with prepositions for right hand
    "on his right hand": "on the hand on the right side",
    "on her right hand": "on the hand on the right side",
    "on their right hand": "on the hand on the right side",
    "to his right hand": "to the hand on the right side",
    "to her right hand": "to the hand on the right side",
    "to their right hand": "to the hand on the right side",

    # Phrases without prepositions for right hand
    "his right hand": "his hand on the right side",
    "her right hand": "her hand on the right side",
    "their right hand": "their hand on the right side",

    # Phrases with prepositions for left hand
    "on his left hand": "on the hand on the left side",
    "on her left hand": "on the hand on the left side",
    "on their left hand": "on the hand on the left side",
    "to his left hand": "to the hand on the left side",
    "to her left hand": "to the hand on the left side",
    "to their left hand": "to the hand on the left side",

    # Phrases without prepositions for left hand
    "his left hand": "his hand on the left side",
    "her left hand": "her hand on the left side",
    "their left hand": "their hand on the left side",

    # Phrases with prepositions for right leg
    "on his right leg": "on the leg on the right side",
    "on her right leg": "on the leg on the right side",
    "on their right leg": "on the leg on the right side",
    "to his right leg": "to the leg on the right side",
    "to her right leg": "to the leg on the right side",
    "to their right leg": "to the leg on the right side",

    # Phrases without prepositions for right leg
    "his right leg": "his leg on the right side",
    "her right leg": "her leg on the right side",
    "their right leg": "their leg on the right side",

    # Phrases with prepositions for left leg
    "on his left leg": "on the leg on the left side",
    "on her left leg": "on the leg on the left side",
    "on their left leg": "on the leg on the left side",
    "to his left leg": "to the leg on the left side",
    "to her left leg": "to the leg on the left side",
    "to their left leg": "to the leg on the left side",

    # Phrases without prepositions for left leg
    "his left leg": "his leg on the left side",
    "her left leg": "her leg on the left side",
    "their left leg": "their leg on the left side",

    # Phrases with prepositions for right arm
    "on his right arm": "on the arm on the right side",
    "on her right arm": "on the arm on the right side",
    "on their right arm": "on the arm on the right side",
    "to his right arm": "to the arm on the right side",
    "to her right arm": "to the arm on the right side",
    "to their right arm": "to the arm on the right side",

    # Phrases without prepositions for right arm
    "his right arm": "his arm on the right side",
    "her right arm": "her arm on the right side",
    "their right arm": "their arm on the right side",

    # Phrases with prepositions for left arm
    "on his left arm": "on the arm on the left side",
    "on her left arm": "on the arm on the left side",
    "on their left arm": "on the arm on the left side",
    "to his left arm": "to the arm on the left side",
    "to her left arm": "to the arm on the left side",
    "to their left arm": "to the arm on the left side",

    # Phrases without prepositions for left arm
    "his left arm": "his arm on the left side",
    "her left arm": "her arm on the left side",
    "their left arm": "their arm on the left side",

    # Phrases with prepositions for right foot
    "on his right foot": "on the foot on the right side",
    "on her right foot": "on the foot on the right side",
    "on their right foot": "on the foot on the right side",
    "to his right foot": "to the foot on the right side",
    "to her right foot": "to the foot on the right side",
    "to their right foot": "to the foot on the right side",

    # Phrases without prepositions for right foot
    "his right foot": "his foot on the right side",
    "her right foot": "her foot on the right side",
    "their right foot": "their foot on the right side",

    # Phrases with prepositions for left foot
    "on his left foot": "on the foot on the left side",
    "on her left foot": "on the foot on the left side",
    "on their left foot": "on the foot on the left side",
    "to his left foot": "to the foot on the left side",
    "to her left foot": "to the foot on the left side",
    "to their left foot": "to the foot on the left side",

    # Phrases without prepositions for left foot
    "his left foot": "his foot on the left side",
    "her left foot": "her foot on the left side",
    "their left foot": "their foot on the left side",

    # Additional body parts (right cheek, left cheek, etc.)
    "on his right cheek": "on the cheek on the right side",
    "on her right cheek": "on the cheek on the right side",
    "on their right cheek": "on the cheek on the right side",
    "his right cheek": "his cheek on the right side",
    "her right cheek": "her cheek on the right side",
    "their right cheek": "their cheek on the right side",

    "on his left cheek": "on the cheek on the left side",
    "on her left cheek": "on the cheek on the left side",
    "on their left cheek": "on the cheek on the left side",
    "his left cheek": "his cheek on the left side",
    "her left cheek": "her cheek on the left side",
    "their left cheek": "their cheek on the left side",

    # For eyebrows, ears, temples, etc.
    "on his right eyebrow": "on the eyebrow on the right side",
    "on her right eyebrow": "on the eyebrow on the right side",
    "his right eyebrow": "his eyebrow on the right side",
    "her right eyebrow": "her eyebrow on the right side",

    "on his left eyebrow": "on the eyebrow on the left side",
    "on her left eyebrow": "on the eyebrow on the left side",
    "his left eyebrow": "his eyebrow on the left side",
    "her left eyebrow": "her eyebrow on the left side",

    "on his right ear": "on the ear on the right side",
    "on her right ear": "on the ear on the right side",
    "his right ear": "his ear on the right side",
    "her right ear": "her ear on the right side",

    "on his left ear": "on the ear on the left side",
    "on her left ear": "on the ear on the left side",
    "his left ear": "his ear on the left side",
    "her left ear": "her ear on the left side",

    # Temples and similar specific parts
    "on his right temple": "on the temple on the right side",
    "on her right temple": "on the temple on the right side",
    "his right temple": "his temple on the right side",
    "her right temple": "her temple on the right side",

    "on his left temple": "on the temple on the left side",
    "on her left temple": "on the temple on the left side",
    "his left temple": "his temple on the left side",
    "her left temple": "her temple on the left side",
	
	# Phrases for buttocks
	"on his right buttock": "on the buttock on the right side",
	"on her right buttock": "on the buttock on the right side",
	"on their right buttock": "on the buttock on the right side",
	"his right buttock": "his buttock on the right side",
	"her right buttock": "her buttock on the right side",
	"their right buttock": "their buttock on the right side",

	"on his left buttock": "on the buttock on the left side",
	"on her left buttock": "on the buttock on the left side",
	"on their left buttock": "on the buttock on the left side",
	"his left buttock": "his buttock on the left side",
	"her left buttock": "her buttock on the left side",
	"their left buttock": "their buttock on the left side",

	# Phrases for ass
	"on his right ass cheek": "on the cheek on the right side",
	"on her right ass cheek": "on the cheek on the right side",
	"his right ass cheek": "his cheek on the right side",
	"her right ass cheek": "her cheek on the right side",

	"on his left ass cheek": "on the cheek on the left side",
	"on her left ass cheek": "on the cheek on the left side",
	"his left ass cheek": "his cheek on the left side",
	"her left ass cheek": "her cheek on the left side",

	# Phrases for knee
	"on his right knee": "on the knee on the right side",
	"on her right knee": "on the knee on the right side",
	"on their right knee": "on the knee on the right side",
	"his right knee": "his knee on the right side",
	"her right knee": "her knee on the right side",
	"their right knee": "their knee on the right side",

	"on his left knee": "on the knee on the left side",
	"on her left knee": "on the knee on the left side",
	"on their left knee": "on the knee on the left side",
	"his left knee": "his knee on the left side",
	"her left knee": "her knee on the left side",
	"their left knee": "their knee on the left side",

	# Phrases for calf
	"on his right calf": "on the calf on the right side",
	"on her right calf": "on the calf on the right side",
	"on their right calf": "on the calf on the right side",
	"his right calf": "his calf on the right side",
	"her right calf": "her calf on the right side",
	"their right calf": "their calf on the right side",

	"on his left calf": "on the calf on the left side",
	"on her left calf": "on the calf on the left side",
	"on their left calf": "on the calf on the left side",
	"his left calf": "his calf on the left side",
	"her left calf": "her calf on the left side",
	"their left calf": "their calf on the left side",

	# Phrases for thighs
	"on his right thigh": "on the thigh on the right side",
	"on her right thigh": "on the thigh on the right side",
	"on their right thigh": "on the thigh on the right side",
	"his right thigh": "his thigh on the right side",
	"her right thigh": "her thigh on the right side",
	"their right thigh": "their thigh on the right side",

	"on his left thigh": "on the thigh on the left side",
	"on her left thigh": "on the thigh on the left side",
	"on their left thigh": "on the thigh on the left side",
	"his left thigh": "his thigh on the left side",
	"her left thigh": "her thigh on the left side",
	"their left thigh": "their thigh on the left side",

}

# Track the number of replacements for each key
replacement_counts = {key: 0 for key in replacements}

# Function to preserve the case of the original text
def preserve_case(match, replacement):
    if match.group(0).isupper():
        return replacement.upper()
    elif match.group(0)[0].isupper():
        return replacement.capitalize()
    else:
        return replacement.lower()

# Function to replace text in a file
def replace_text_in_file(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Perform the replacements
    for key, value in replacements.items():
        pattern = re.compile(re.escape(key), re.IGNORECASE)
        matches = len(re.findall(pattern, content))
        if matches > 0:
            print(f"Found {matches} match(es) for '{key}' in {file_path}")
        # Append ' <!######>' to the replacement string and preserve case
        content = re.sub(pattern, lambda m: preserve_case(m, value + ' <!###---------###>'), content)
        replacement_counts[key] += matches
    
    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Function to get all .txt files recursively from a directory
def get_all_text_files(dir_path):
    txt_files = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    return txt_files

# Process all text files in the folder
def process_files(folder_path):
    # Step 1: Verify folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder path '{folder_path}' does not exist.")
        return
    
    # Step 2: Retrieve all .txt files in the directory
    txt_files = get_all_text_files(folder_path)
    
    if not txt_files:
        print("No .txt files found in the specified folder.")
        return
    
    print(f"Found {len(txt_files)} .txt files in the folder '{folder_path}':")
    
    # Step 3: Process each file
    for file_path in txt_files:
        replace_text_in_file(file_path)
    
    # Step 4: Display the replacement counts (only those that had replacements)
    print("\nReplacement Summary (only non-zero replacements):")
    for key, count in replacement_counts.items():
        if count > 0:  # Only print replacements where something was found
            print(f'{key}: {count} replacements')

# Run the process
if __name__ == "__main__":
    # Ask user for the folder path
    folder_path = input("Enter the path to the folder containing .txt files: ")
    process_files(folder_path)