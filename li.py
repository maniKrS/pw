import streamlit as st
import joblib
import numpy as np
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import urllib  # Import urllib to handle URLs

map_pokemon = ['bulbasaur', 'ivysaur', 'venusaur', 'charizard', 'butterfree',
       'weedle', 'kakuna', 'beedrill','charmander', 'pidgey', 'pidgeotto', 'pidgeot',
       'spearow', 'fearow', 'nidoqueen', 'nidoking', 'jigglypuff',
       'wigglytuff', 'zubat', 'golbat', 'oddish', 'gloom', 'vileplume',
       'paras', 'parasect', 'venonat', 'venomoth', 'poliwrath',
       'bellsprout', 'weepinbell', 'victreebel', 'tentacool',
       'tentacruel', 'geodude', 'graveler', 'golem', 'slowpoke',
       'slowbro', 'magnemite', 'magneton', 'farfetchd', 'doduo', 'dodrio',
       'dewgong', 'cloyster', 'gastly','pikachu', 'haunter', 'gengar', 'onix',
       'exeggcute', 'exeggutor', 'rhyhorn', 'rhydon', 'starmie',
       'mr-mime', 'scyther', 'jynx', 'gyarados', 'lapras', 'omanyte',
       'omastar', 'kabuto', 'kabutops', 'aerodactyl', 'articuno',
       'zapdos', 'moltres', 'dragonite', 'hoothoot', 'noctowl', 'ledyba',
       'ledian', 'spinarak', 'ariados', 'crobat', 'chinchou', 'lanturn',
       'igglybuff', 'togetic', 'natu', 'xatu', 'marill', 'azumarill',
       'hoppip', 'skiploom', 'jumpluff', 'yanma', 'wooper', 'quagsire',
       'murkrow', 'slowking', 'girafarig', 'forretress', 'gligar',
       'steelix', 'qwilfish', 'scizor', 'shuckle', 'heracross', 'sneasel',
       'magcargo', 'swinub', 'piloswine', 'corsola', 'delibird',
       'mantine', 'skarmory', 'houndour', 'houndoom', 'kingdra',
       'smoochum', 'larvitar', 'pupitar', 'tyranitar', 'lugia', 'ho-oh',
       'celebi', 'combusken', 'blaziken', 'marshtomp', 'swampert',
       'beautifly', 'dustox', 'lotad', 'lombre', 'ludicolo', 'nuzleaf',
       'shiftry', 'taillow', 'swellow', 'wingull', 'pelipper', 'ralts',
       'kirlia', 'gardevoir', 'surskit', 'masquerain', 'breloom',
       'nincada', 'ninjask', 'shedinja', 'azurill', 'sableye', 'mawile',
       'aron', 'lairon', 'aggron', 'meditite', 'medicham', 'roselia',
       'carvanha', 'sharpedo', 'numel', 'camerupt', 'vibrava', 'flygon',
       'cacturne', 'swablu', 'altaria', 'lunatone', 'solrock', 'barboach',
       'whiscash', 'crawdaunt', 'baltoy', 'claydol', 'lileep', 'cradily',
       'anorith', 'armaldo', 'tropius', 'spheal', 'sealeo', 'walrein',
       'relicanth', 'salamence', 'beldum', 'metang', 'metagross',
       'latias', 'latios', 'rayquaza', 'jirachi', 'torterra', 'monferno',
       'infernape', 'empoleon', 'starly', 'staravia', 'staraptor',
       'bibarel', 'budew', 'roserade', 'shieldon', 'bastiodon',
       'wormadam-plant', 'mothim', 'combee', 'vespiquen', 'gastrodon',
       'drifloon', 'drifblim', 'honchkrow', 'stunky', 'skuntank',
       'bronzor', 'bronzong', 'mime-jr', 'chatot', 'spiritomb', 'gible',
       'gabite', 'garchomp', 'lucario', 'skorupi', 'drapion', 'croagunk',
       'toxicroak', 'mantyke', 'snover', 'abomasnow', 'weavile',
       'magnezone', 'rhyperior', 'togekiss', 'yanmega', 'gliscor',
       'mamoswine', 'gallade', 'probopass', 'froslass', 'rotom', 'dialga',
       'palkia', 'heatran', 'giratina-altered', 'victini', 'pignite',
       'emboar', 'pidove', 'tranquill', 'unfezant', 'woobat', 'swoobat',
       'excadrill', 'palpitoad', 'seismitoad', 'sewaddle', 'swadloon',
       'leavanny', 'venipede', 'whirlipede', 'scolipede', 'cottonee',
       'whimsicott', 'sandile', 'krokorok', 'krookodile', 'dwebble',
       'crustle', 'scraggy', 'scrafty', 'sigilyph', 'tirtouga',
       'carracosta', 'archen', 'archeops', 'ducklett', 'swanna',
       'deerling', 'sawsbuck', 'emolga', 'escavalier', 'foongus',
       'amoonguss', 'frillish', 'jellicent', 'joltik', 'galvantula',
       'ferroseed', 'ferrothorn', 'litwick', 'lampent', 'chandelure',
       'stunfisk', 'golett', 'golurk', 'pawniard', 'bisharp', 'rufflet',
       'braviary', 'vullaby', 'mandibuzz', 'durant', 'deino', 'zweilous',
       'hydreigon', 'larvesta', 'volcarona', 'cobalion', 'terrakion',
       'virizion', 'thundurus-incarnate', 'reshiram', 'zekrom',
       'landorus-incarnate', 'kyurem', 'keldeo-ordinary', 'meloetta-aria',
       'genesect', 'chesnaught', 'delphox', 'greninja', 'diggersby',
       'fletchling', 'fletchinder', 'talonflame', 'vivillon', 'litleo',
       'pyroar', 'pangoro', 'honedge', 'doublade', 'aegislash-blade',
       'inkay', 'malamar', 'binacle', 'barbaracle', 'skrelp', 'dragalge',
       'helioptile', 'heliolisk', 'tyrunt', 'tyrantrum', 'amaura',
       'aurorus', 'hawlucha', 'dedenne', 'carbink', 'klefki', 'phantump',
       'trevenant', 'pumpkaboo-average', 'gourgeist-average', 'noibat',
       'noivern', 'yveltal', 'zygarde-50', 'diancie', 'hoopa-confined',
       'volcanion', 'rowlet', 'dartrix', 'decidueye', 'incineroar',
       'primarina', 'pikipek', 'trumbeak', 'toucannon', 'charjabug',
       'vikavolt', 'crabominable', 'oricorio-baile', 'cutiefly',
       'ribombee', 'mareanie', 'toxapex', 'dewpider', 'araquanid',
       'morelull', 'shiinotic', 'salandit', 'salazzle', 'stufful',
       'bewear', 'oranguru', 'wimpod', 'golisopod', 'sandygast',
       'palossand', 'minior-meteor', 'turtonator', 'togedemaru',
       'mimikyu', 'bruxish', 'drampa', 'dhelmise', 'hakamo-o', 'kommo-o',
       'tapu-koko', 'tapu-lele', 'tapu-bulu', 'tapu-fini', 'solgaleo',
       'lunala', 'nihilego', 'buzzwole', 'pheromosa', 'celesteela',
       'kartana', 'guzzlord', 'magearna', 'marshadow', 'naganadel',
       'stakataka', 'blacephalon']

map_type1 = {
    'Grass': 1, 'Fire': 2, 'Bug': 3, 'Normal': 4, 'Poison': 5, 'Water': 6, 'Rock': 7,
    'Electric': 8, 'Ghost': 9, 'Ground': 10, 'Psychic': 11, 'Ice': 12, 'Dragon': 13, 'Fairy': 14,
    'Dark': 15, 'Steel': 16, 'Fighting': 17, 'Flying': 18
}


pokemon_map = {name: i for i, name in enumerate(map_pokemon)}

model = joblib.load('C:/Users/mani manak/OneDrive/Desktop/pw/pokemon_model.joblib')


def get_pokemon_image(pokemon_name):
    try:
       
        url = f"https://bulbapedia.bulbagarden.net/wiki/{pokemon_name}_(Pokémon)"

        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

     
        img_tag = soup.find('table', {'class': 'roundy'}).find('img')
        if img_tag:
            img_url = img_tag['src']
            img_url = urllib.parse.urljoin(url, img_url)

            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))
            return img
            

    except Exception as e:
        st.write(f"Error: {e}")
        return None


st.title("Machine Learning Pokémon Type Predictor")

user_input = st.text_input("Enter a Pokémon name:")

if st.button("Predict Type"):
  
    if user_input in map_pokemon:
     
        numeric_value = pokemon_map[user_input]

        input_features_numeric = np.array([numeric_value]).reshape(1, -1)

        predicted_pokemon_numeric = model.predict(input_features_numeric)

        predicted_type = [key for key, value in map_type1.items() if value == predicted_pokemon_numeric][0]

        st.write(f"The predicted type for {user_input} is {predicted_type}.")

        pokemon_image = get_pokemon_image(user_input)
        if pokemon_image:
            st.image(pokemon_image, caption=f"Image of {user_input}", use_column_width=True)
            st.balloons()
        else:
            st.write("Image not found.")
    else:
        st.write("Pokémon not found in the dataset")
