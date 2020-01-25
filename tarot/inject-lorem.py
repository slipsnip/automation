import pandas
import lorem

if __name__ == '__main__':
    CSV = ('generators.csv')
    fields = 'id,title_x,number,tarot_card_image,astrological,alchemical,intelligence,hebrew_letter,letter_meaning,description_x,galileo_content,f_loss_content,st_paul_content,f_loss_bullets,galileo_bullets,st_paul_bullets,description_bullets,slashdot_position,watchtower_position,title_y,description_y,tarot_card_thumbnail'.split(',')
    bullet_fields = ['description_bullets','galileo_bullets','f_loss_bullets','st_paul_bullets']
    lorem_full_fields = ['description','galileo_content','f_loss_content','st_paul_content']
    lorem_single_fields =  'astrological,alchemical,intelligence,hebrew_letter,letter_meaning'.split(',')
    image_fields = ['tarot_card_thumbnail']
    field_types = {
        'title':'object',
        'number':'int64',
        'tarot_card_image':'object',
        'tarot_card_thumbnail':'object',
        'astrological':'object',
        'alchemical':'object',
        'intelligence':'object',
        'hebrew_letter':'object',
        'letter_meaning':'object',
        'watchtower_position':'int64',
        'slashdot_position':'int64',
        'description':'object',
        'description_bullets':'object',
        'galileo_content':'object',
        'galileo_bullets':'object',
        'f_loss_content':'object',
        'f_loss_bullets':'object',
        'st_paul_content':'object',
        'st_paul_bullets':'object'
        }
    cards = pandas.read_csv(CSV, dtype=field_types)
    lorem_bullet = lorem.TextLorem(srange=(6,7))
    for index, card in cards.iterrows():
        for column in cards.columns:
            if (pandas.isna(card[column])):
                print(type(card[column].astype(str)))
                # cards.at[index, column] = lorem.text()
    # cards.to_csv("lorem.csv", index=False)