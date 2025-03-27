# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-i2c-lcd-display-micropython/

from machine import Pin, SoftI2C, PWM
from pico_i2c_lcd import I2cLcd
from time import sleep
import time

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
# Setup buzzer
buzzer = PWM(Pin(15))

# Happy tones
celebratory_notes = [659, 784, 1047, 784]  # E5, G5, C6, G5
celebratory_durations = [0.2, 0.2, 0.2, 0.2]
# Milky tones
sad_notes = [392, 349, 330, 294]  # G4, F4, E4, D4
sad_durations = [0.3, 0.3, 0.3, 0.3]

# Play a tune
def play_tune(notes, durations):
    for note, duration in zip(notes, durations):
        if note > 0:
            buzzer.freq(note)
            buzzer.duty_u16(1000)
        else:
            buzzer.duty_u16(0)
        time.sleep(duration)
    buzzer.duty_u16(0)

# Initialize I2C and LCD objects
i2c = SoftI2C(sda=Pin(4), scl=Pin(5), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.putstr("It's working :)")
sleep(4)

try:
    while True:
        # Clear the LCD
        lcd.clear()
        # Display two different messages on different lines
        # By default, it will start at (0,0) if the display is empty
        lcd.putstr("Hello Eklavya!")
        sleep(2)
        lcd.clear()
        # Starting at the second line (0, 1)
        lcd.move_to(0, 1)
        lcd.putstr("Hello EKUuuU!")
        play_tune(celebratory_notes, celebratory_durations)
        sleep(2)

        lcd.move_to(0, 1)
        lcd.putstr("Hello Shirshti!")
        play_tune(celebratory_notes, celebratory_durations)
        sleep(2)

        lcd.clear()
        lcd.move_to(0, 1)
        lcd.putstr("Hello Milky!")
        play_tune(celebratory_notes, celebratory_durations)
        sleep(1)

except KeyboardInterrupt:
    # Turn off the display
    print("Keyboard interrupt")
    lcd.backlight_off()
    lcd.display_off()