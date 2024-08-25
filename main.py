import scrape
import time
from datetime import datetime, timedelta, date  # Import date class from datetime module
from imap_tools import MailBox, AND
import smtp  # Assuming you have an smtp.py with send_mail function

while True:
    # Calculate timestamp for past few minutes (e.g., past 5 minutes)
    past_few_minutes = datetime.now() - timedelta(minutes=5)
    
    with MailBox('imap.gmail.com').login('kylesgeemail@gmail.com', 'egwpdzorrzchvjxr', initial_folder='INBOX') as mailbox:
        scores_sent = False
        sport = None
        team = None
        email_subject = None

        def scrape_send(sport, team, email_subject, receiver):
            # Scrape proper stuff
            message = str(scrape.scrape_scores(sport, team))

            # Send actual email
            smtp.send_mail(receiver, message, email_subject)
            print("E-Mail Sent....waiting for next request")

        # Fetch unread emails that arrived in the past few minutes
        for msg in mailbox.fetch(AND(seen=False, date_gte=past_few_minutes.date()), mark_seen=False):
            subject = str(msg.subject).upper()
            sender = str(msg.from_)
            
            if subject == 'SCORES':
                scores_sent = True
                print("Matching Scores Request Found: ", msg.date, msg.subject, msg.uid)
                email_subject = 'Here Are The Scores You Requested!'
                uid = msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'MLB SCORES':
                scores_sent = True
                print("Matching MLB Request Found: ", msg.date, msg.subject, msg.uid)
                sport = 'mlb'
                email_subject = 'Here Are The MLB Scores You Requested!'
                uid = msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'NFL SCORES':
                scores_sent = True
                print("Matching NFL Request Found: ", msg.date, msg.subject, msg.uid)
                sport = 'nfl'
                email_subject = 'Here Are The NFL Scores You Requested!'
                uid = msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'NBA SCORES':
                scores_sent = True
                print("Matching NBA Request Found: ", msg.date, msg.subject, msg.uid)
                sport = 'nba'
                email_subject = 'Here Are The NBA Scores You Requested!'
                uid = msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'DBACKS':
                team = 'dbacks'
                scores_sent = True
                print("Matching Scores Request Found: ", msg.date, msg.subject, msg.uid)
                email_subject = 'Here is the Dbacks info You Requested!'
                uid = msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'RAIDERS':
                team = 'raiders'
                scores_sent = True
                print("Matching Scores Request Found: ", msg.date, msg.subject, msg.uid)
                email_subject = 'Here is the Raiders info You Requested!'
                uid = msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'SUNS':
                team = 'suns'
                scores_sent = True
                print("Matching Scores Request Found: ", msg.date, msg.subject, msg.uid)
                email_subject = 'Here is the Suns info You Requested!'
                uid = msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            else:
                scores_sent = False

    if not scores_sent:
        print("No scores requested, will check in another 10 minutes...")

    time.sleep(100)