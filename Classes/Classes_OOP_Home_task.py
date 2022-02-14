import time
import random
from datetime import datetime


class News:
    def publish_news(self):
        text_news = input('Enter the text of news: ')
        city = input('Enter the city where the news came from: ')
        with open('newsfeed.txt', 'a+') as f:
            data_now = time.strftime("%d/%m/%Y %H.%M")
            # Move read cursor to the start of file.
            f.seek(0)
            # If file is not empty then append '\n'
            data = f.read(100)
            if len(data) > 0:
                f.write(3 * "\n")
            # Append text at the end of file
            # elements = enter_news()
            f.write('News ' + '-' * 25)
            f.write('\n')
            # f.write(elements[0])
            f.write(text_news)
            f.write('\n')
            # f.write(elements[1] + ', ' + time_str)
            f.write(city + ', ' + data_now)
            f.write('\n')
            # for line in elements:
            #     f.write(line +', ' + time_str)
            #     f.write('\n')
            f.write('-' * 30)
        print(f'\nThis news is published\n')


class PrivateAd:
    def publish_ad(self):
        text_ad = input('Enter the text of ad: ')
        expiration_date = input('Enter the expiration date for this ad (format - dd/mm/yyyy): ')
        with open('newsfeed.txt', 'a+') as f:
            delta = str((datetime.strptime(expiration_date, '%d/%m/%Y') - datetime.now()).days)
            # Move read cursor to the start of file.
            f.seek(0)
            # If file is not empty then append '\n'
            data = f.read(100)
            if len(data) > 0:
                f.write(3 * "\n")
            # Append text at the end of file
            f.write('Private Ad ' + '-' * 19)
            f.write('\n')
            f.write(text_ad)
            f.write('\n')
            f.write('Actual until: ' + expiration_date + ', ' + delta + ' days left.')
            f.write('\n')
            f.write('-' * 30)
        print(f'\nThis ad is published\n')


class PublishTips:
    def publish_tips(self):
        text_tip = input('Enter the text of ad: ')
        with open('newsfeed.txt', 'a+') as f:
            # Move read cursor to the start of file.
            f.seek(0)
            # If file is not empty then append '\n'
            data = f.read(100)
            temp = random.randint(0, 10)
            if len(data) > 0:
                f.write(3 * "\n")
            # Append text at the end of file
            f.write('Tip of the day ' + '-' * 15)
            f.write('\n')
            f.write(text_tip)
            f.write('\n')
            f.write('Usefulness of tip: ' + str(temp) + ' of 10.')
            f.write('\n')
            f.write('-' * 30)
        print(f'\nThis tip is published\n')


class Choose_element(News, PrivateAd, PublishTips):
    @staticmethod
    def choose_ele():
        while True:
            try:
                print(f'Select what data type you want to add. \nAvaliable list: \n1. News \n2. Private Ad \n3. Advice '
                      f'\n4. Exit')
                element = int(input('Enter the required number: '))
                if element == 1:
                    obj = News()
                    n = obj.publish_news()
                elif element == 2:
                    obj = PrivateAd()
                    n = obj.publish_ad()
                elif element == 3:
                    obj = PublishTips()
                    n = obj.publish_tips()
                elif element == 4:
                    break
                else:
                    print(f"\nThis number is not on the list, please try again.\n")
            except ValueError:
                print(f"\nError! It's not a number, please try again.\n")
        return element


start = Choose_element()
start.choose_ele()