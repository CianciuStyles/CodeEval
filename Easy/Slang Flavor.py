import sys

slangs = [', yeah!', ', this is crazy, I tell ya.', ', can U believe this?',
          ', eh?', ', aw yea.', ', yo.', '? No way!', '. Awesome!']

with open(sys.argv[1], 'r') as test_cases:
    correct, slang_index = False, 0

    for test in test_cases:
        if test == '':
            continue

        text, new_text = test.strip(), ''
        for char in text:
            if char == '.' or char == '?' or char == '!':
                if correct is False:
                    correct = True
                    new_text += char
                else:
                    new_text += slangs[slang_index]
                    slang_index = (slang_index + 1) % len(slangs)
                    correct = False
            else:
                new_text += char

        print(new_text)