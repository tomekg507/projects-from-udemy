import requests
from flask import Flask, render_template, request

API_KEY = 'RGAPI-0770ca3c-4f87-4889-8a27-8e69042d9afe'
URL_cont = "https://europe.api.riotgames.com"
URL_region = "https://euw1.api.riotgames.com"
parameters = {'api_key': API_KEY}


def check_rank(gameName, tagLine):

    puuid = f'/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}'
    response_puuid = requests.get(url=URL_cont + puuid, params=parameters)

    if 400 <= response_puuid.status_code < 500:
        return False, 'Summoner does not exist.'

    elif response_puuid.status_code >= 500:
        return False, 'Technical issues, please try again later.'

    else:
        encryptedPUUID = response_puuid.json()[('puuid')]

        summoner_id = f'/lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}'
        response_summoner_id = requests.get(url=URL_region + summoner_id, params=parameters)

        try:
            encryptedSummonerId = response_summoner_id.json()['id']
        except KeyError:
            return False, 'Summoner does not exist.'
        else:
            data_endpoint = f'/lol/league/v4/entries/by-summoner/{encryptedSummonerId}'
            response = requests.get(url=URL_region + data_endpoint, params=parameters)

            tier = response.json()[0]['tier']
            rank = response.json()[0]['rank']
            lp = response.json()[0]['leaguePoints']
            wins = response.json()[0]['wins']
            losses = response.json()[0]['losses']

            return True, tier, rank, lp, wins, losses

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    data = ()
    if request.method == 'POST':
        data = check_rank(request.form['name'], request.form['tag'])
    return render_template('index.html', data=data)

app.run(debug=True)


















print()

