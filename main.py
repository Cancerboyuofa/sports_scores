import time
import smtp

while(True):

    import scrape
    from imap_tools import MailBox, AND
    with MailBox('imap.gmail.com').login('kylesgeemail@gmail.com', 'trvzxacwfybnsskp', 'INBOX') as mailbox:
    
# Declare Gobals

        scores_sent = False
        sport = None
        team = None
        email_subject = None

        def scrape_send(sport, team, email_subject, reciever):

            # Scrape proper stuff

            message = str(scrape.scrape_scores(sport,team))

            # Send actual email

            smtp.send_mail(reciever, message,email_subject)
                                
            print("E-Mail Sent....waiting for next request")



# Get new unread emails from INBOX folder with scores or teams

        for msg in mailbox.fetch(AND(seen=False)):
            
            subject = str(msg.subject)
            subject = subject.upper()
            sender = str(msg.from_ )
            
            if subject == 'SCORES':
                    
                scores_sent = True
                print("Matching Scores Request Found: ",msg.date, msg.subject, msg.uid)
                email_subject = 'Here Are The Scores You Requested!'
                uid=msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'MLB SCORES':
                    
                scores_sent = True
                print("Matching MLB Request Found: ", msg.date, msg.subject, msg.uid)
                sport = 'mlb'
                email_subject = 'Here Are The MLB Scores You Requested!'
                uid=msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'NFL SCORES':
                    
                scores_sent = True
                print("Matching NFL Request Found: ", msg.date, msg.subject, msg.uid)
                sport = 'nfl'
                email_subject = 'Here Are The NFL Scores You Requested!'
                uid=msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'NBA SCORES':
                    
                scores_sent = True
                print("Matching NBA Request Found: ",msg.date, msg.subject, msg.uid)
                sport = 'nba'
                email_subject = 'Here Are The NBA Scores You Requested!'
                uid=msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'DBACKS':
                team = 'dbacks'
                scores_sent = True
                print("Matching Scores Request Found: ",msg.date, msg.subject, msg.uid)
                email_subject = 'Here is the Dbacks info You Requested!'
                uid=msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'RAIDERS':
                team = 'raiders'
                scores_sent = True
                print("Matching Scores Request Found: ",msg.date, msg.subject, msg.uid)
                email_subject = 'Here is the Raiders info You Requested!'
                uid=msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            elif subject == 'SUNS':
                team = 'suns'
                scores_sent = True
                print("Matching Scores Request Found: ",msg.date, msg.subject, msg.uid)
                email_subject = 'Here is the Suns info You Requested!'
                uid=msg.uid
                scrape_send(sport, team, email_subject, sender)
                mailbox.delete(msg.uid)

            else:
                scores_sent = False


    if scores_sent == False:
        print("No scores requested, will check in another 10 minutes...")

    time.sleep(30)