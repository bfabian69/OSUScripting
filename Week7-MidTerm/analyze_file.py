
import os
import string

def process_file(input_filename):
    """Process the input file and calculate required statistics."""
    
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File '{input_filename}' not found. Please make sure the file exists.")
        return

    output_filename = "Analysis-" + os.path.basename(input_filename)
    

    translator = str.maketrans('', '', string.punctuation + string.digits)
    cleaned_content = content.translate(translator)
    
    lines = content.splitlines()
    words = cleaned_content.split()
    total_characters = len(content)  
    num_lines = len(lines)
    num_words = len(words)

    word_freq = {}
    for word in words:
        word = word.lower()  
        word_freq[word] = word_freq.get(word, 0) + 1

    word_pairs = []
    for i in range(len(words) - 1):
        word_pairs.append((words[i].lower(), words[i + 1].lower()))

    pair_freq = {}
    for pair in word_pairs:
        pair_freq[pair] = pair_freq.get(pair, 0) + 1

    repeating_pairs = {pair: count for pair, count in pair_freq.items() if count > 1}

    total_unique_words = len(word_freq)
    avg_word_length = sum(len(word) for word in words) / num_words if num_words > 0 else 0
    avg_unique_word_length = sum(len(word) for word in word_freq.keys()) / total_unique_words if total_unique_words > 0 else 0
    num_repeating_pairs = len(repeating_pairs)

    with open(output_filename, 'w') as output_file:

        output_file.write(f"Number of lines: {num_lines}\n")
        output_file.write(f"Number of words: {num_words}\n")
        output_file.write(f"Number of characters: {total_characters}\n\n")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {total_characters}")
        
        output_file.write("Word Frequencies:\n")
        for word in sorted(word_freq.keys()):
            output_file.write(f"{word} ({word_freq[word]})\n")
        
        output_file.write("\nRepeating Word Pairs:\n")
        for pair, count in sorted(repeating_pairs.items()):
            output_file.write(f"{pair[0]} {pair[1]} ({count})\n")
        print("Repeating word pairs calculated.")

        output_file.write("\nSummary:\n")
        output_file.write(f"Total number of words: {num_words}\n")
        output_file.write(f"Average word length: {avg_word_length:.2f}\n")
        output_file.write(f"Number of unique words: {total_unique_words}\n")
        output_file.write(f"Average length of unique words: {avg_unique_word_length:.2f}\n")
        output_file.write(f"Number of word pairs with frequency 2 or more: {num_repeating_pairs}\n")
        print("Summary statistics calculated.")

    print(f"Analysis complete. Results saved to {output_filename}")

if __name__ == "__main__":
    
    input_file = input("Enter the name of the file to analyze (speech.txt): ").strip()
    process_file(input_file)
