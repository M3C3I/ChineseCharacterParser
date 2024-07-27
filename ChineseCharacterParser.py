import json
import csv
# import dictionary
from hanzipy.decomposer import HanziDecomposer
decomposer = HanziDecomposer()
# import decomposer
from hanzipy.dictionary import HanziDictionary
dictionary = HanziDictionary()

def load_unihan_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_primary_radical(data, kRSUnicode):
    radical_code = kRSUnicode.split('.')[0] + '.0'
    for char, details in data.items():
        if details['kRSUnicode'] == radical_code:
            return char, details
    return None, None

def main():
    unihan_data = load_unihan_data('UnihanLite.json')
    input_characters = []

    # Load characters from the input file
    with open('input.txt', 'r', encoding='utf-8') as file:
        input_characters = [line.strip() for line in file.readlines()]

    # Prepare to write to the CSV
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['number', 'character', 'Mandarin', 'Definition', 'primaryRadical',
                      'radicalMandarin', 'hanzipyStrokes', 'hanzipyRadicals']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for idx, char in enumerate(input_characters, 1):
            char_data = unihan_data.get(char, {})
            decomposition = decomposer.decompose(char)

            # Find primary radical
            primary_radical_char, primary_radical_data = find_primary_radical(unihan_data, char_data.get('kRSUnicode', ''))

            # Write base information
            writer.writerow({
                'number': idx,
                'character': char,
                'Mandarin': char_data.get('kMandarin', ''),
                'Definition': char_data.get('kDefinition', ''),
                'primaryRadical': primary_radical_char,
                'radicalMandarin': primary_radical_data.get('kMandarin', '') if primary_radical_data else '',
                'hanzipyStrokes': ', '.join(decomposition['graphical']),
            })

            # Write radicals
            for radical_idx, radical in enumerate(decomposition['radical'], 1):
                radical_data = unihan_data.get(radical, {})
                writer.writerow({
                    'number': f'{idx}{chr(96 + radical_idx)}',  # Generates '1a', '1b', etc.
                    'character': radical,
                    'Mandarin': radical_data.get('kMandarin', ''),
                    'Definition': radical_data.get('kDefinition', ''),
                })

if __name__ == '__main__':
    main()
