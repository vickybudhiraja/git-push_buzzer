# Pico-W git-push-buzzer

## Your pico-W will sound an alarm as soon as somone pushes the code in your git repo.

Run via VS Extension.

If you get permission denied error, use this:
sudo chmod 666 /dev/ttyACM0

good idea to first use your Pico via USB:
minicom -o -D /dev/ttyACM0

This should open the comm channel between your pico and your comp. If nothing happens after this command, use sudo or chamod as stated above.

# Refrences
https://randomnerdtutorials.com/raspberry-pi-pico-i2c-lcd-display-micropython/
https://nevercode.blogspot.com/2025/02/build-your-own-youtube-subscriber.html?m=1
