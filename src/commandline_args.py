import argparse


class CommandlineArgs:

    def __init__(self):
        # Create an ArgumentParser object
        parser = argparse.ArgumentParser()

        # Add arguments to the parser
        parser.add_argument("-t", "--text", help="Text for ElevenLabs to generate an mp3 for")

        # Parse the command-line arguments
        self.args = parser.parse_args()

    def get_text(self):
        text = self.args.text

        if text is None:
            raise Exception("Use --text to specify the text to generate an mp3 for.")

        return text
