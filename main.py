#Breach Bot Starter Code
breachYear = 2019
#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook data breach.")


#Introduces breach
print("Would you like to learn about the Facebook data 2019 breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Personal information of 530 million people was stolen from user profiles on Facebook including phone numbers, full names, locations, and email addresses. The hack was by malicious actors  who took data by exploiting a feature that allowed users to find each other by phone number.")
  
  elif topic.lower() == "b":
    print("Facebook found and fixed the issue in August 2019, the breached information is already publicly available and it was not an issue users could fix themselves. Recommended by cybersecurity expert, check the data tracking tool HaveIBeenPwned.com to see if your data has been breached.")
  
  elif topic.lower() == "c":
    break    
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("The Facebook data 2019 breach relates to confidentiality because it ensures only authorized users to have access to data.")
  
  elif topic.lower() == "b":
    print("I disagree with the organization's response because I think Facebook should have let users know that their personal information was being used so users could have been alert. Intruders can do an enormous amount with little information.")
  
  elif topic.lower() == "c":
    print("My advice would be to change any account that use the same password and to monitor their information through a security tracking website to see if their data has been pawned.")
    

  elif topic.lower() == "d":
    break    
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")