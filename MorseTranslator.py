from gpiozero import LED
import time

'''
Morse codes:
dots & dashes
dots take one beat & dashes take up 3 of those beats
space between letters is three beats, spaces between words is 7 beats
'''
class LedOutput:
    
    def __init__(self, letter_tempo):
        self.led = LED(18) # Make this specifc to your gpio pin
        self.letter_tempo = letter_tempo

    def dot(self):
        self.led.on()
        time.sleep(self.letter_tempo)
        self.led.off()
        time.sleep(0.1)

    def dash(self):
        self.led.on()
        time.sleep(self.letter_tempo * 3)
        self.led.off()
        time.sleep(0.1)

    
class MorseTranslator:
    
    knowledge = { 'A':'.-','B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

    def __init__(self, letter_beat):
        self.led_output = LedOutput(letter_beat)
        self.letter_beat = letter_beat
        self.word_beat = letter_beat*7

    def encrypt(self, message):
        words_list = message.split(' ')
        for word in words_list:
            for letter in word:
                if letter in self.knowledge:
                    print(letter)
                    for instruction in self.knowledge[letter]:
                        if instruction == '.':
                            print(instruction)
                            self.led_output.dot()
                        else:
                            print(instruction)
                            self.led_output.dash()
                        
                else:
                    exit(1)

                time.sleep(self.letter_beat)
            time.sleep(self.word_beat)
            
                            
def main():
    letter_tempo = float(input('Enter a value in secinds, that defines beat per letter: '))
    translator = MorseTranslator(letter_tempo)
    print('Translator is initalized, enter quit at any time to exit')
    while True:
        translate_from = input('Enter the word, sentence, or paragraph you want to have translated: ')
        if translate_from == 'quit':
            break
        translator.encrypt(translate_from)


if __name__ == '__main__':
    main()
