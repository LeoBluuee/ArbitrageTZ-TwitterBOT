import os
import tweepy
from secrets import *
from time import gmtime, strftime


# ====== Individual bot configuration ==========================
bot_username = 'Dexter Arbitrage BOT'
logfile_name = bot_username + ".log"

# ==============================================================

# #
# #
# Aqui vem a parte complicada. 
# Dar query em duas APIs (X e Y) e comparar os dois valores.
# Gera 3 condições: Valores iguais, X>Y, e X<Y.
# No primeiro caso, enviar texto1. No segundo, texto2...
# #
# #


# Uma coisa que não entendi é esse comentário da desenvolvedora na função debaixo. "Replace this with your code!"
# Que "code"?? A Condicional vai ali?
# Então aqui em cima eu só pego os 2 valores e salvo em 2 variáveis?
# Aqui na função de baixo vai a comparação dos 2 valores e a função condicional?
# #

# O que pensei: Definir 3 variaveis com os 3 textos. (onde? em C coloca no começo do código, mas e Python?)
# if x > y text = texto1    if x < y text = texto2      else text = texto3
# Mas aí como eu declaro uma variável "text" tipo string, sem valor, pra ser preenchida pela condicional? É necessário isso em Python?

def create_tweet():
    """Create the text of the tweet you want to send."""
    # Replace this with your code!
   
    text = ""
    return text


# Essa aqui quase fez sentido pra mim. Claramente é a função de tweetar.
# Mas e esse texto? Pra que um texto dentro se já vai a variável "text" como parâmetro na função??


def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log("Tweeted: " + text)


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)
