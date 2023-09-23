from github import Github

# Replace with your personal access token
token = "TOKEN"

def main():
    g = Github(token)
    user = g.get_user()
    notifications = user.get_notifications()
    
    for notification in notifications:
        print(notification.subject.title)

if __name__ == '__main__':
    main()
