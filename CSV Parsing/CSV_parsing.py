import time
import random
from datetime import datetime
import Functions_Home_task
import os
import csv
import re
import string


class Publish:
    def publish(self, header, text, footer):
        with open('newsfeed.txt', 'a+') as f:
            # Move read cursor to the start of file.
            f.seek(0)
            # If file is not empty then append '\n'
            data = f.read(100)
            if len(data) > 0:
                f.write(3 * "\n")
            # Append text at the end of file
            f.write(header)
            f.write('\n')
            f.write(text)
            f.write('\n')
            f.write(footer)
            f.write('\n')
            f.write('-' * 30)
        # return (print(f'\nThis news is published\n'))


class News(Publish):
    def publish_news(self):
        text = input('Enter the text of news: ')
        city = input('Enter the city where the news came from: ')
        self.text = text
        self.header = str('News ' + '-' * 25)
        self.footer = str(city + ', ' + time.strftime("%d/%m/%Y %H.%M"))
        result = Publish()
        result.publish(self.header, self.text, self.footer)
        print(f'\nThis news is published\n')


class PrivateAd:
    def publish_ad(self):
        text_ad = input('Enter the text of ad: ')
        expiration_date = input('Enter the expiration date for this ad (format - dd/mm/yyyy): ')
        self.header = 'Private Ad ' + '-' * 19
        self.text = text_ad
        delta = str((datetime.strptime(expiration_date, '%d/%m/%Y') - datetime.now()).days)
        self.footer = 'Actual until: ' + expiration_date + ', ' + delta + ' days left.'
        result = Publish()
        result.publish(self.header, self.text, self.footer)
        print(f'\nThis ad is published\n')


class PublishTips:
    def publish_tips(self):
        self.header = 'Tip of the day ' + '-' * 15
        text_tip = input('Enter the text of ad: ')
        self.text = text_tip
        self.footer = 'Usefulness of tip: ' + str(random.randint(0, 10)) + ' of 10.'
        result = Publish()
        result.publish(self.header, self.text, self.footer)
        print(f'\nThis tip is published\n')


class UploadFile:
    def upload_file(self):
        print(f'Define file path for downloading file: \nAvaliable list: \n1.Default folder \n2.User provided file paths')
        default_folder = '''C:/Users/Stepan_Zhuk/PycharmProjects/Python for Data Quality Engineers #5/load_folder'''
        path_folder = default_folder
        enter_path = int(input('Enter the required number: '))
        if enter_path == 1:
            path_folder = default_folder
        elif enter_path == 2:
            path_folder = input('Enter the path to load data from file: ')
        else:
            print(f"Choose correct number! Try again!")
        for file in os.listdir(path_folder):
            # Check whether file is in text format or not
            if file.endswith(".txt"):
                file_path = f"{path_folder}/{file}"
                # print(file_path)
                with open(file_path, 'r') as f:
                    for row in f:
                        row = row.split(',')
                        normalize_text = str(Functions_Home_task.fix_issues(row))
                        with open('newsfeed.txt', 'a+') as f:
                            f.write(normalize_text)
                            f.write("\n")
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print("File was successfully processed. File deleted !")
                else:
                    print("File does not exist !")


class CsvParsing:
    def csv_word_count(self):
        list_words = []
        with open('newsfeed.txt', 'r') as f:
            for line in f:
                words = line.split(' ')
                for item in words:
                    if re.search('[a-zA-Z]', item):
                        list_words.append(item)
        with open('word_count.csv', 'w', newline='') as csvfile:
            headers = ['word', 'count']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            d = dict()
            for word in list_words:
                word = re.sub(r"[^\w\s'-]", '', word)
                word = word.lower().replace('\n', '').replace(',', '').replace("'", '')
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1
            for key in list(d.keys()):
                writer.writerow({'word': key, 'count': d[key]})

        with open('letter_count.csv', 'w', newline='') as csvfile:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage,%']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            let = dict()
            upper_case = {}
            upper_case_letters = ''
            for word in list_words:
                word = re.sub(r"[^\w\s'-]", '', word)
                word = word.replace('\n', '').replace(',', '').replace("'", '')
                for letter in word:
                    if re.search('[A-Z]', letter):
                        upper_case_letters += letter
                    letter = str(letter).lower()
                    if letter in let:
                        let[letter] = let[letter] + 1
                    else:
                        let[letter] = 1
            for letter in upper_case_letters:
                if re.search('[A-Z]', letter) and upper_case.get(letter):
                    upper_case[letter] += 1
                elif re.search('[A-Z]', letter):
                    upper_case[letter] = 1
            for key in list(let.keys()):
                if upper_case.get(key.upper()):
                    writer.writerow({'letter': key, 'count_all': let[key],
                                 'count_uppercase':  upper_case.get(key.upper()),
                                 'percentage,%':  round(upper_case.get(key.upper())/let[key] * 100,0)})
                else:
                    writer.writerow({'letter': key, 'count_all': let[key],
                                     'count_uppercase': 0,
                                     'percentage,%': 0.0})


class ChooseElement(News, PrivateAd, PublishTips, UploadFile):
    @staticmethod
    def choose_ele():
        while True:
            try:
                print(f'Select what data type you want to add. \nAvaliable list: \n1. News \n2. Private Ad \n3. Advice '
                      f'\n4. Upload file' f' \n5. CSV_Parsing' f'\n6. Exit')
                element = int(input('Enter the required number: '))
                if element == 1:
                    obj = News()
                    n = obj.publish_news()
                    print('\n')
                elif element == 2:
                    obj = PrivateAd()
                    n = obj.publish_ad()
                    print('\n')
                elif element == 3:
                    obj = PublishTips()
                    n = obj.publish_tips()
                    print('\n')
                elif element == 4:
                    obj = UploadFile()
                    n = obj.upload_file()
                    print('\n')
                elif element == 5:
                    obj = CsvParsing()
                    n = obj.csv_word_count()
                    print('\n')
                elif element == 6:
                    break
                else:
                    print(f"\nThis number is not on the list, please try again.\n")
            except ValueError:
                print(f"\nError! It's not a number, please try again.\n")
        return element

if __name__ == '__main__':
    start = ChooseElement()
    start.choose_ele()