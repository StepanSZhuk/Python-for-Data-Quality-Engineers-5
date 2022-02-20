import time
import random
from datetime import datetime


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


class ChooseElement(News, PrivateAd, PublishTips):
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

if __name__ == '__main__':
    start = ChooseElement()
    start.choose_ele()
