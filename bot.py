import praw
import random
import datetime
import time
from textblob import TextBlob


def generate_comment_0():
    whoList = ["Many people", "A lot of Americans", "People around the world", "Most citizens"]
    who = random.choice(whoList)
    nameList = ["Biden", "Joe Biden", "Daddy Biden", "Joseph Biden"]
    name = random.choice(nameList)
    jobList = ["president", "head of the USA", "supreme ruler of America", "white supremacy destroyer"]
    job = random.choice(jobList)
    exampleList = ["For example", "For instance", "To illustrate", "In particular"]
    example = random.choice(exampleList)
    planList = ["plans", "strategy", "commitment", "determination"]
    plan = random.choice(planList)
    text = who + " support " + name + " as a " + job + " because he has real plans fo the future. " + example + ", look at " + name + "'s " + plan + " to fight the climate change."
    return text
def generate_comment_1():
    nameList = ["Biden", "Joe Biden", "Daddy Biden", "Joseph Biden"]
    name = random.choice(nameList)
    whatList = ["decent human being", "respectful person", "thoughtful man", "rational guy"]
    what = random.choice(whatList)
    whoList = ["people of any background", "citizens of different countries", "people of varying cultures", "aliens"]
    who = random.choice(whoList)
    jobList = ["president", "head of the USA", "supreme ruler of America", "white supremacy destroyer"]
    job = random.choice(jobList)
    actionList = ["respect", "be considerate to", "understanding of", "patient with"]
    action = random.choice(actionList)
    text = name + " continues proving that he is a " + what + " being by carying about " + who + ". It is important for the " + job + " to " + action + " others."
    return text
def generate_comment_2():
    nameList = ["Biden", "Joe Biden", "Daddy Biden", "Joseph Biden"]
    name = random.choice(nameList)
    whatList = ["a depp background", "a lot of knowledge", "interesting thoughts", "a lot of experience"]
    what = random.choice(whatList)
    whereList = ["foreign policy", "foreign affairs", "international relations", "diplomatic policy"]
    where = random.choice(whereList)
    whoList = ["foreign leaders", "representatives from other countries", "international communities", "presidents of many countries"]
    who = random.choice(whoList)
    whichList = ["multi-cultural", "diverse", "broad-based", "multiethnic"]
    which = random.choice(whichList)
    text = name + " has " + what + " in " + where + " and understands the importance of cultivating relationships with " + who + " He will help create a " + which + " America!"
    return text
def generate_comment_3():
    nameList = ["Donald Trump", "Trump", "Orange Man", "The Racist Guy"]
    name = random.choice(nameList)
    whereList = ["America", "the United States", "the US", "USA"]
    where = random.choice(whereList)
    insultList = ["stupid", "unintelligent", "uneducated", "brainless"]
    insult = random.choice(insultList)
    text = name + " is the worst thing that happened to " + where + ". He is much more " + insult + " than he thinks."
    return text
def generate_comment_4():
    nameList = ["Donald Trump", "Trump", "Orange Man", "The Racist Guy"]
    name = random.choice(nameList)
    actionList = ["disregarded", "ignored", "neglected", "shut down"]
    action = random.choice(actionList)
    whatList = ["president", "head of the country", "politican", "authority figure"]
    what = random.choice(whatList)
    problemList = ["systematic racism", "police brutality", "white supremacy", "COVID-19"]
    problem = random.choice(problemList)
    text = name + " has completely " + action + " current problems such as " + problem + ", climate change and homelessness. He has no business being a " + what
    return text
def generate_comment_5():
    nameList = ["Donald Trump", "Trump", "Orange Man", "The Racist Guy"]
    name = random.choice(nameList)
    whoList = ["ordinary Americans", "normal citizens", "regualr humans", "American citizens"]
    who = random.choice(whoList)
    whenList = ["first 100 days", "first few months", "first few weeks", "first few hours (lol)"]
    when = random.choice(whenList)
    whichList = ["corporations and the wealthiest few", "big companies", "rich people", "billionairs"]
    which = random.choice(whichList)
    which2List = ["everyone else", "poor people", "middle class workers", "regular citizens"]
    which2 = random.choice(which2List)
    text = "After months of campaign promises to help " + who + ", " + name + "'s " + when + " have revealed that his true policy priorities are benefitting " + which + " at the expense of " + which2 + "!"
    return text

def generate_comment():
    return random.choice([generate_comment_5(), generate_comment_4(), generate_comment_3(), generate_comment_2(), generate_comment_1(), generate_comment_0()])




# connect to reddit and choose an intial submission
reddit = praw.Reddit('bot1')

reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhmj34/from_hoangs_bot_1_dare_we_dream_of_a_joe_biden/'
submission = reddit.submission(url=reddit_debate_url)



while True:

        ##### EXTRA CREDIT ######
        # Upvote pro biden and anti trump submissions. Downvote pro trump and anti biden submissions
    submission_text = TextBlob(submission.title)
    if ("biden" in submission_text.lower() and submission_text.sentiment.polarity>0.5) or ("trump" in submission_text.lower() and submission_text.sentiment.polarity<-0.5):
        submission.upvote()
    elif ("biden" in submission_text.lower() and submission_text.sentiment.polarity<-0.5) or ("trump" in submission_text.lower() and submission_text.sentiment.polarity>0.5):
        submission.downvote()
    # polarity between -0.5 and 0.5 is not that accurate


    # printing the current time will help make the output messages more informative
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    if submission.title == "2020 Debate Thread":
        print("2020 Debate Thread does not work .... continue")
        #continue
    #2020 Debate Thread stopped working for me, I think it's overloaded

    # create a list of ALL comments at a given submission
    all_comments = []
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        all_comments.append(comment)
    print('len(all_comments)=',len(all_comments))


    # filter all_comments to remove comments that were generated by your bot
    not_my_comments = []
    myComments = 0
    for comment in all_comments:
        try:
            if comment.author.name != 'cs40-test-bot':
                not_my_comments.append(comment)
            else:
                myComments += 1
                continue
        except:
            not_my_comments.append(comment) #we need this line because without it Deleted comments would count as my comments
            continue
            

            ##### EXTRA CREDIT ######
            # Upvote pro biden and anti trump comments. Downvote pro trump and anti biden comments
        text = TextBlob(comment.body)
        if ("biden" in text.lower() and text.sentiment.polarity>0.5) or ("trump" in text.lower() and text.sentiment.polarity<-0.5):
            comment.upvote()
        elif ("biden" in text.lower() and text.sentiment.polarity<-0.5) or ("trump" in text.lower() and text.sentiment.polarity>0.5):
            comment.downvote()


    print('len(not_my_comments)=',len(not_my_comments))
    print("Number of my comments:", myComments)

    has_not_commented = len(not_my_comments) == len(all_comments)




    if has_not_commented:
        # if you have not made any comment in the thread, then post a top level comment
        try:
        #### EXTRA CREDIT ###### 
            if ("biden" in submission_text.lower() and submission_text.sentiment.polarity > 0.5):
                submission.reply("I agree, Biden is amazing. " + generate_comment())
            elif ("biden" in submission_text.lower() and submission_text.sentiment.polarity < -0.5):
                submission.reply("Biden is not that bad. " + generate_comment())
            elif ("trump" in submission_text.lower() and submission_text.sentiment.polarity > 0.5):
                submission.reply("Trump is horrible. " + generate_comment())
            elif ("trump" in submission_text.lower() and submission_text.sentiment.polarity < -0.5):
                submission.reply("I agree. Trump is an asshole. " + generate_comment())
            
            print("I LEFT A COMMENT")

        except Exception as e:
            print(e)
            print("YOU CAN'T POST A COMMENT AT THE MOMENT")
            time.sleep(10)
    else:
        # filter the not_my_comments list to also remove comments that you've already replied to
        comments_without_replies = []
        for comment in not_my_comments:
            this_reply_works = True
            for reply in comment.replies:
                try:
                    if reply.author.name == 'cs40-test-bot':
                        this_reply_works = False
                        break
                except:
                    pass
            if this_reply_works:
                comments_without_replies.append(comment)


        print('len(comments_without_replies)=',len(comments_without_replies))

        #randomly select a comment from the comments_without_replies list and reply to that comment
        try:
            #### EXTRA CREDIT ###### 
            current_comment = random.choice(comments_without_replies)
            current_text = TextBlob(current_comment.body)
            if ("biden" in current_text.lower() and current_text.sentiment.polarity > 0.5):
                current_comment.reply("Yes I agree, Biden is amazing. " + generate_comment())
            elif ("biden" in current_text.lower() and current_text.sentiment.polarity < -0.5):
                current_comment.reply("No, Biden is not that bad. " + generate_comment())
            elif ("trump" in current_text.lower() and current_text.sentiment.polarity > 0.5):
                current_comment.reply("No, Trump is horrible. " + generate_comment())
            elif ("trump" in current_text.lower() and current_text.sentiment.polarity < -0.5):
                current_comment.reply("Yes I agree. Trump is an asshole. " + generate_comment())
            print("I LEFT A REPLY")

        except Exception as e:
            print(e)
            print("YOU CAN'T POST A COMMENT AT THE MOMENT")
            time.sleep(10)


    # select a new submission for the next iteration;
    rand = random.random()
    submissionList = []
    if rand<0.5:
        reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhmj34/from_hoangs_bot_1_dare_we_dream_of_a_joe_biden/'
        submission = reddit.submission(url=reddit_debate_url)
    else:
        subreddit = reddit.subreddit("csci040temp")
        for submission in subreddit.top("day"):
            submissionList.append(submission)
        submission = random.choice(submissionList)