import yfinance as yf
from textblob import TextBlob
import datetime

# première fonction permettant de récupérer les news via l'API yahoo finance

def get_company_news(ticker_symbol):
    print(f"\n** 1. Get data for {ticker_symbol} **")
    # API yahoo finance
    stock = yf.Ticker(ticker_symbol) # -> prix/bilan/news
          
    try:
        news_list = stock.news # définition d'un objet "stock" avec news comme attribut -> stock dans news list direct
    except Exception as e:
        print("API connection error")
        return []

    if not news_list:
        print("No news available")
        return []
        # J'ai choisi 5 news pour l'exemple (seul les articles seront pris en comptes)
    return news_list[:5]

# deuxième fonction permettant d'analyser le risque via textblob

def analyze_risk(news_data):
    print("\n** 2. AI analytics (NLP) and risk detection **")
    risk_score = 0 
    analyzed_count = 0 #Compteur pour le calcul du ratio final (on ne compte que les articles lisibles pour ne pas fausser le score)

    #conception du tableau du terminal
    print(f"{'news title':<60} | {'feeling'}")
    print("-" * 80)

    for item in news_data:
            # On essaie de trouver le titre qui est souvent caché dans 'content'
        try:
                # CAS 1 : Le titre est rangé dans une sous-boîte 'content' 
            if 'content' in item and 'title' in item['content']:
                title = item['content']['title']
                
                # CAS 2 : Le titre est rangé directement à la racine 
            elif 'title' in item:
                title = item['title']
                    
            else:
                    # Si on ne trouve pas de titre on ignore cet article
                print("No title found for this article, we'll move on.")
                continue

        except Exception as e: # Sécurité anti-plantage
            continue
            # Utilisation de la librairie TextBlob pour analyser le sentiment
        blob = TextBlob(title)
        polarity = blob.sentiment.polarity

        if polarity < -0.1:  # je met 0.1 pour éviter les faux négatif 
            sentiment = "Negative"
            risk_score += 1 

        elif polarity > 0.1:
            sentiment = "Positive"

        else:
            sentiment = "Neutral"

        print(f"{title[:58]:<60} | {sentiment}")
        analyzed_count += 1

    return risk_score, analyzed_count

#troisième fonction pour générer le rapport 

def generate_report(ticker, risk_score, total_news):
    print("\n\n** 3. IDD Report **")
    print(f"Action analyzed : {ticker}")
    print(f"Date of report : {datetime.date.today()}")

    if total_news == 0:
        print("Not enough data to conclude")
        return
    
    #calcul du ratio de risque 
    risk_ratio = risk_score / total_news

    #Création d'un seuil d'alerte si + de 40% des news sont négatives
    if risk_ratio >= 0.4:
        status = "High risk detected"
        action = "Investigation required"
    else:
        status = "Low risk"
        action = "Standard IDD procedure authorized"

    print(f"Risk Score : {risk_score}/{total_news} negative news")
    print(f"IDD status : {status}")
    print(f"Recommendation : {action}")
    print("********************************************")

#Exécution du programme

if __name__ == "__main__":
    print("*** BUCKLER.AI PROTOTYPE IDD BOT ***")
    user_ticker = input("Enter the stock symbol (e.g., AAPL, TSLA, MSFT) : ").upper()

    news = get_company_news(user_ticker)

    if news: 
        score, count = analyze_risk(news)
        generate_report(user_ticker, score, count)
    else:
        print("End of the program")



            


          