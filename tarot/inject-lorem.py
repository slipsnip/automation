import pandas
import numpy
from lorem.text import TextLorem
import lorem
from pathlib import Path

def bullet_lorem(num_bullets, words_per):
    bullet = TextLorem(trange=(3), srange=(6,7))
    return bullet.sentence()

if __name__ == '__main__':
    CSV = str(Path('./generators.csv').resolve())
    fields = 'id,title_x,number,tarot_card_image,astrological,alchemical,intelligence,hebrew_letter,letter_meaning,description_x,galileo_content,f_loss_content,st_paul_content,f_loss_bullets,galileo_bullets,st_paul_bullets,description_bullets,slashdot_position,watchtower_position,title_y,description_y,tarot_card_thumbnail'.split(',')
    bullet_fields = ['description_bullets','galileo_bullets','f_loss_bullets','st_paul_bullets']
    lorem_full_fields = ['description','galileo_content','f_loss_content','st_paul_content']
    lorem_single_fields =  'astrological,alchemical,intelligence,hebrew_letter,letter_meaning'.split(',')
    image_fields = ['tarot_card_thumbnail']
    field_types = {
        'title':numpy.object,
        'number':numpy.int64,
        'tarot_card_image':numpy.object,
        'tarot_card_thumbnail':numpy.object,
        'astrological':numpy.object,
        'alchemical':numpy.object,
        'intelligence':numpy.object,
        'hebrew_letter':numpy.object,
        'letter_meaning':numpy.object,
        'watchtower_position':numpy.int64,
        'slashdot_position':numpy.int64,
        'description':numpy.object,
        'description_bullets':numpy.object,
        'galileo_content':numpy.object,
        'galileo_bullets':numpy.object,
        'f_loss_content':numpy.object,
        'f_loss_bullets':numpy.object,
        'st_paul_content':numpy.object,
        'st_paul_bullets':numpy.object
        }
    cards = pandas.read_csv(CSV, dtype=field_types, keep_default_na=True)
    bullet = bullet_lorem(7,3)
    print(bullet)
    # for index, card in cards.iterrows():
    #     for column in cards.columns:
    #         if (pandas.isna(card[column])):
    #             print(type(card[column].astype(str)))
                # cards.at[index, column] = lorem.text()
    # cards.to_csv("lorem.csv", index=False)