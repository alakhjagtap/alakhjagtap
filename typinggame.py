import time
import random

paragraphs = [
    "Dragons don't exist they said. They are the stuff of legend and people's imagination. Greg would have agreed with this assessment without a second thought 24 hours ago. But now that there was a dragon staring directly into his eyes, he questioned everything that he had been told.",
    "It was a simple tip of the hat. Grace didn't think that anyone else besides her had even noticed it. It wasn't anything that the average person would notice, let alone remember at the end of the day. That's why it seemed so unbelievable that this little gesture would ultimately change the course of the world.",
    "There was something in the tree. It was difficult to tell from the ground, but Rachael could see movement. She squinted her eyes and peered in the direction of the movement, trying to decipher exactly what she had spied. The more she peered, however, the more she thought it might be a figment of her imagination. Nothing seemed to move until the moment she began to take her eyes off the tree. Then in the corner of her eye, she would see the movement again and begin the process of staring again.",
    "The opened package of potato chips held the answer to the mystery. Both detectives looked at it but failed to realize it was the key to solve the crime. They passed by it assuming it was random trash ensuring that the case would never be solved.",
    "She nervously peered over the edge. She understood in her mind that the view was supposed to be beautiful, but all she felt was fear. There had always been something about heights that disturbed her, and now she could feel the full force of this unease. She reluctantly crept a little closer with the encouragement of her friends as the fear continued to build. She couldn't help but feel that something horrible was about to happen.",
    "There were a variety of ways to win the game. James had played it long enough to know most of them and he could see what his opponent was trying to do. There was a simple counterattack that James could use and the game should be his. He began deploying it with the confidence of a veteran player who had been in this situation a thousand times in the past. So, it was with great surprise when his opponent used a move he had never before seen or anticipated to easily defeat him in the game.",
    "She needed glasses. It wasn't that she couldn't see without them, but what she could see with them. When she wore glasses, her eyes focused so deeply that she could see not only the physical but also beyond. It was like a superpower. But she needed glasses.",
    "It was a concerning development that he couldn't get out of his mind. He'd had many friends throughout his early years and had fond memories of playing with them, but he couldn't understand how it had all stopped. There was some point as he grew up that he played with each of his friends for the very last time, and he had no idea that it would be the last.",
    "Was it a whisper or was it the wind? He wasn't quite sure. He thought he heard a voice but at this moment all he could hear was the wind rustling the leaves of the trees all around him. He stopped and listened more intently to see if he could hear the voice again. Nothing but the wind rustling the leaves could be heard. He was about to continue his walk when he felt a hand on his shoulder, and he quickly turned to see who it was. There was nobody there, but he heard the voice again.",
    "\"Are you getting my texts???\" she texted to him. He glanced at it and chuckled under his breath. Of course he was getting them, but if he wasn't getting them, how would he ever be able to answer? He put the phone down and continued on his project. He was ignoring her texts and he planned to continue to do so."
]


def get_paragraph():
    return random.choice(paragraphs)


def calculate_speed(start_time, end_time, input_text):
    total_time = end_time - start_time
    words = len(input_text.split())
    speed = (words / total_time) * 60
    return speed


def main():
    print("Welcome to the Typing Speed Game!")
    input("Press Enter to start...")
    print("Type the following paragraph:")
    paragraph = get_paragraph()
    print(paragraph)

    input("Press Enter when you're ready to start typing...")
    start_time = time.time()
    typed_text = input("Type the paragraph: ")
    end_time = time.time()

    typing_speed = calculate_speed(start_time, end_time, typed_text)
    print(f"\nYour typing speed: {typing_speed:.2f} words per minute.")


if __name__ == "__main__":
    main()
