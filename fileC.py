def counter(fname):
    num_words = 0
    num_charc = 0
    num_spaces = 0
    ch = ["*", "@", "#", "$", "%", "&", ".", "?", ",", "<", ">", ";", ":", "/", "|", "[", "]", "{", "}", "=", "+", "_",
          "-", "(", ")", "^", "!", "`", "~"]
 
    with open(fname, 'r') as f:
        for line in f:
            split_var = line.split(' ')
            low_list = [each_string.lower() for each_string in split_var]
            set_list = set(low_list)
            if len(low_list) != len(set_list):
                num_dup= (len(low_list) - len(set_list)) + 1
            else:
                num_dup =0

            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    num_words += 1

                    word = 'N'
                elif (letter == ' '):
                    num_spaces += 1

                    word = 'Y'
                for i in letter:
                    if i in ch:
                        num_charc += 1

            print("\nTotal number of words in text file: ", num_words)
            print("Total number of duplicate words in text file: ", num_dup)
            print('Total number of special characters in text file: ', num_charc)
            print('Total number of spaces in text file: ', num_spaces)

if __name__ == '__main__':
    fname=(input("Enter the file path: "))
    try:
        counter(fname)
    except:
        print('File not found')

