# git-push_buzzer

## Your pico-W will sound an alarm as soon as somone pushed the code in your git repo.

Run via VS Extension.

If you get permission denied error, use this:
sudo chmod 666 /dev/ttyACM0

good idea to first use your Pico via USB:
minicom -o -D /dev/ttyACM0

This should open the comm channel between your pico and your comp. If nothing happens after this command, use sudo or chamod as stated above.

